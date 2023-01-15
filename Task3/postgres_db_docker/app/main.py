""" Script connect to postgres database"""
import logging
import time
import sys

from database import Pool
from user import User

def main():
    """ Main function """
    
    # Waiting for db start
    time.sleep(15)

    # logging configuration
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    # Creating connection pool object
    pool = Pool()
   
    # Creating object user which represent record from db
    my_user = User('4','Tadeusz', 'Norek')

    # Store my_user record in database
    my_user.save_to_db(pool)

    # Loading and display record from db
    my_user = User.load_user_from_db(pool, '3')
    logging.info(my_user)

    # Singleton test
    pool2 = Pool()
    logging.info(pool is pool2)


if __name__ == "__main__":
    sys.exit(main())
