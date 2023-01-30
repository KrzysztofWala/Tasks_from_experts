"""Connection pool class with singleton pattern."""
import logging
import sys
import threading
import psycopg2

from dbpool_exception import ConnectionMissingInPool
from dbpool_exception import ConnectionFromOutsidePool


# Logging configuration
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger('docker_app')


class DBPool:
    '''DBPool class provide connection to postgres database pool.'''
    def __new__(cls, *args, **kwargs):
        """Singleton pattern."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBPool, cls).__new__(cls)
        return cls.instance

    def __enter__(self):
        return self

    def __exit__(self, ett, evt, est):
        self.close_connections()

    def __init__(self, conn_min, conn_max, password, user, database, host, port):
        '''Initialazing DBPool obcject.
           Creating creating defined by user number of initial connections.

        :Parameters:
            - conn_min - number of connections
            - conn_max - maximal number of connections in pool
            - password - postgres password
            - user - postgres user
            - database - postgres database name
            - host - postgres host
            - port - postgres port
        '''
        self.__conn_min = conn_min
        self.__conn_max = conn_max
        self.__conn_current = 0
        self.__conn_list = []
        self.__conn_id = []
        self.__user = user
        self.__password = password
        self.__database = database
        self.__host = host
        self.__port = port
        self.lock = threading.Lock()

        # Basic validation number of connection
        if (self.__conn_min < 0 or self.__conn_max < 0 or self.__conn_min > self.__conn_max):
            self.__conn_min = 0
            self.__conn_max = 10
            logging.info('Wrong number of connection, default number will be use instead')

        # Initializing connection list
        for _ in range(0,self.__conn_min):
            connection=(psycopg2.connect(user =self.__user,
                                         password =self.__password,
                                         database =self.__database,
                                         host =self.__host,
                                         port = self.__port))
            self.__conn_list.append(connection)
            self.__conn_id.append(id(connection))
        # Set current number of connection
        self.__conn_current = self.__conn_min


    def get_connection(self):
        '''Function get free connection from pool.'''

        with self.lock:
            # Free connections are available in connection list
            if len(self.__conn_list) > 0:
                connection = self.__conn_list.pop()

            # Free connections are NOT available
            # but it's possible to create new one
            elif self.__conn_current < self.__conn_max:
                connection = psycopg2.connect(user =self.__user,
                                              password =self.__password,
                                              database =self.__database,
                                              host =self.__host,
                                              port = self.__port)
                self.__conn_id.append(id(connection))
                self.__conn_current+=1

            # Free connections are NOT available
            # Not possible to create new connection
            else:
                connection = None
        return connection


    def return_connection(self, connection):
        '''Function return connection to the pool.

        :Parameters:
            - connection - connections which will return to pool
        '''

        with self.lock:
            try:
                if id(connection) in self.__conn_id:
                    self.__conn_list.append(connection)
                else:
                    raise ConnectionFromOutsidePool("Connection don't belongs to current pool!")
            except Exception as exc:
                logging.info(exc)


    def close_connections(self):
        '''Function close all connection inside the pool.
           In case when not all connection returned to the pool
           function will raise an error.
        '''
        try:
            if len(self.__conn_list) != self.__conn_current:
                raise ConnectionMissingInPool("Not all connections returned to DBPool!")
            with self.lock:
                for conn in self.__conn_list:
                    conn.close()
        except Exception as exc:
            logging.info(exc)
