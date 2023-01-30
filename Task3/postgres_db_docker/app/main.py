"""Script connect to postgres database.
   Data can be added by using external text files."""
import logging
import os
import re
import sys
import time
from dbpool import DBPool

import handlingfiles as hf
import database as db


# Path to files on docker
PATH = '/db_data/'

def main():
    """Main function of module."""

    # Loading credential from env
    password = os.environ["POSTGRES_PASSWORD"]
    user = os.environ["POSTGRES_USER"]
    database = os.environ["POSTGRES_DB"]
    host = os.environ["HOST"]
    port = os.environ["PORT"]

    # Logging configuration
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger('docker_app')

    # Creating connection pool object
    with  DBPool(3,10, password, user, database, host, port) as pool:

        # Creating log and users_DB files, store actual user table in file
        hf.create_files(PATH)
        connection = pool.get_connection()
        users_data = db.get_db_users(connection)
        pool.return_connection(connection)
        hf.store_users_file(users_data, PATH)
        
        # Main loop
        while True:
            logging.info('________________________WAITING FOR FILES________________________')
            # files_list - contain all files name in data folder
            files_list = list(os.listdir(PATH))
            # Searching for files with name "add_"
            for file in files_list:
                records_to_add = []
                # variable add_check indicates that currect file contains "^add_"
                add_check = re.search("^add_", file)
                if add_check is not None:
                    records_to_add, log_list = hf.add_records(file, PATH)
                    # file contains correct data
                    if records_to_add:
                        # attempt to get connection
                        connection = pool.get_connection()
                        # free connection not available - file will be checked in next loop
                        if connection is None:
                            logging.info('Free connection are not availabe')
                            log_list = None
                        # free connection availabe - data will be stored in DB
                        else:
                            db.update_db_users(connection, records_to_add)
                            users_data = db.get_db_users(connection)
                            pool.return_connection(connection)
                            hf.store_users_file(users_data, PATH)
                            os.remove("".join([PATH,file]))
                            logging.info('Data from %s was successfuly updated on database', file)
                    # file do not contain correct data or is empty
                    else:
                        logging.info('File %s do not have correct data', file)
                        os.remove("".join([PATH,file]))
                    if log_list:
                        hf.store_log_file(log_list, PATH)
                # elif delete_check is not None
                    # In progress
                    # hf.delete_records(file, path)
            time.sleep(5)

if __name__ == "__main__":
    sys.exit(main())
