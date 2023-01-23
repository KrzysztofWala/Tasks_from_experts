"""Functions allows execute SQL particular queries."""
# import psycopg2

def get_db_users(connection):
    '''Function getting all records from user table.

    :Parameters:
        - connection - connection to DBPool, needed for creating cursor
                       and execute sql query

    :Return:
        - received_data - records from user table, stored as a list
    '''
    received_data = None
    query = ' SELECT * FROM users'
    with connection.cursor() as cursor:
        cursor.execute(query)
        received_data = cursor.fetchall()
    return received_data

def update_db_users(connection, records_to_add):
    '''Function send new records to the user table.

    :Parameters:
        - connection - connection to DBPool, needed for creating cursor
                       and execute sql query
        - records_to_add - list of records which will be added to users table
    '''
    query = 'INSERT INTO users (id_user, first_name, last_name) VALUES (%s, %s, %s)'
    with connection.cursor() as cursor:
        for line in records_to_add:
            cursor.execute(query, line)
    connection.commit()
