from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from secrets import token_urlsafe

class Hasher:

    @staticmethod
    def check_psw_hash(password, orig_password):
        return check_password_hash(orig_password, password)

    @staticmethod
    def generate_psw_hash(password):
        return generate_password_hash(password)

    @staticmethod
    def create_session_id_hash():
        return token_urlsafe(32)