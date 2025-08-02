class UserAlreadyExists(Exception):
    def __init__(self, name=''):
        msg = f'User {name} already exists'
        super().__init__(msg)