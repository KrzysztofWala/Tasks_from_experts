""" Connection pool class with singleton pattern"""
import psycopg2  

class DB_Pool:
    def __new__(cls, *args):
        """ Singleton pattern """
        if not hasattr(cls, 'instance'):
            cls.instance = super(DB_Pool, cls).__new__(cls)
        return cls.instance

    def __init__(self, conn_min, conn_max):
        self.__conn_min = conn_min
        self.__conn_max = conn_max
        self.__conn_current = 0
        self.__conn_list = []

        ''' Basic validation number of connection '''
        if (self.__conn_min < 0 or self.__conn_max < 0 or self.__conn_min > self.__conn_max):
            self.__conn_min = 0
            self.__conn_max = 10

        ''' Initializing connection list '''
        for i in range(0,self.__conn_min):
            self.__conn_list.append(psycopg2.connect(user ='username',
                                                     password ='secret',
                                                     database ='database',
                                                     host ='172.24.0.3',
                                                     port = '5432'))                                    
        ''' Set current number of connection '''
        self.__conn_current = self.__conn_min


    def __get_connection(self):
        ''' Function get free connection from pool '''

        # Free connections are available in connection list
        if len(self.__conn_list) > 0:
            connection = self.__conn_list.pop()

        # Free connections are NOT available
        # but it's possible to create new one
        elif self.__conn_current < self.__conn_max:
            connection = psycopg2.connect(user='username',
                                          password='secret',
                                          database='database',
                                          host='172.24.0.3',
                                          port = '5432')
            self.__conn_current+=1

        # Free connections are NOT available
        # Not possible to create new connection
        else:
            connection = None
        return connection


    def __return_connection(self, connection):
        ''' Function return connection to the pool '''
        self.__conn_list.append(connection)


    def send_to_db(self, query, list):
        ''' Function sending data to database'''
        connection = self.__get_connection()
        if connection is not None:
            with connection.cursor() as cursor:
                cursor.execute(query, list)
            connection.commit()
            self.__return_connection(connection)


    def load_from_db(self, query, list):
        ''' Function loading data from database'''
        received_data = None
        connection = self.__get_connection()
        if connection is not None:
            with connection.cursor() as cursor:
                cursor.execute(query, list)
                received_data = cursor.fetchone()
                print("Data", received_data)
            self.__return_connection(connection)
        return received_data