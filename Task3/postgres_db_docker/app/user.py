""" User class represents records in database"""
class User:
    """ User class represents records in database"""
    def __init__(self, id_user, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id_user = id_user

    def __repr__(self):
        return "\nUser record: \nID: {} " \
               "\nFirst name: {}" \
               "\nLast name: {}"\
            .format(self.id_user, self.first_name, self.last_name,)

    def save_to_db(self,pool):
        """ Store data in database"""
        connection=pool.get_connection()
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO users (id_user, first_name, last_name) VALUES (%s, %s, %s)',
                                   (self.id_user, self.first_name, self.last_name))
        pool.close_connection(connection)

    @classmethod
    def load_user_from_db(cls, pool, id_user):
        """ Load user record from database"""
        connection=pool.get_connection()
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE id_user=%s', (id_user,))
            user_data = cursor.fetchone()
            pool.close_connection(connection)
            return cls(id_user=user_data[0],
                       first_name=user_data[1],
                       last_name=user_data[2])
