class Authenticator:
    def __init__(self, user_getter):
        self.user_getter = user_getter



    def auth_by_session_id(self, session_id):
        self.user_getter.get_by_session_id(session_id)

