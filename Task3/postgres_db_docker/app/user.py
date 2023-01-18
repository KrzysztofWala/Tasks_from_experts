""" User class represents records in database"""
""" UNDER INVESTIGATION """
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
        pass

    @classmethod
    def load_user_from_db(cls, pool, id_user):
        pass
