class UserAlreadyExists(Exception):
    def __init__(self, name=''):
        msg = f'User {name} already exists'
        super().__init__(msg)

class UserDontExists(Exception):
    def __init__(self, id=None):
        msg = f'User with id {id} dont exists'
        super().__init__(msg)

class InvalidPassword(Exception):
    def __init__(self, password=None):
        msg = f'Wrong password {password}'
        super().__init__(msg)