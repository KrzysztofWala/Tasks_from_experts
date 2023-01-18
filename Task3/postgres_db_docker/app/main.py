""" Script connect to postgres database"""
import logging
import time
import sys

from database import DB_Pool
from user import User

def main():
    """ Main function """
    
    # Waiting for db start
    time.sleep(15)

    # Logging configuration
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    # Creating connection pool object
    pool = DB_Pool(1,3)

    # Sending data test
    sql_query = 'INSERT INTO users (id_user, first_name, last_name) VALUES (%s, %s, %s)'
    data = ['4','Tadeusz', 'Norek']
    pool.send_to_db(sql_query, data)

    # Singleton pattern test
    pool2 = DB_Pool(1,10)
    logging.info(pool is pool2)


if __name__ == "__main__":
    sys.exit(main())
