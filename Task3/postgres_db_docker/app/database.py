""" Connection pool class with singleton pattern"""
from psycopg2 import pool


class Pool:
    """ Connection pool class """
    def __new__(cls):
        """ Singleton pattern """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Pool, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.__connection_pool = pool.ThreadedConnectionPool(1,
                                                             10,
                                                             user='username',
                                                             password='secret',
                                                             database='database',
                                                             host='db',
                                                             port = '5432')

    def get_connection(self):
        """ Function get connection from connection pool"""
        connection = self.__connection_pool.getconn()
        return connection

    def close_connection(self, connection):
        """ Function return connection to connection pool"""
        connection.commit()
        self.__connection_pool.putconn(connection)