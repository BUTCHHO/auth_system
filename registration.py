from hasher import Hasher

class UserRegistration:
    def __init__(self,user_actor):
        self._user_actor = user_actor

    def create_user(self, name, password):
        password = Hasher.generate_psw_hash(password)
        self._user_actor.create_and_write_record_to_db(name=name, password=password)



