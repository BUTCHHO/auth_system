from .exceptions import UserAlreadyHaveSession


class SessionMaker:
    def __init__(self, session_reader, session_actor, time_handler, hasher, cacher, SESSION_EXPIRE_DAYS):
        self.session_reader = session_reader
        self.session_actor = session_actor
        self.hasher = hasher
        self.cacher = cacher
        self.time_handler = time_handler
        self.SESSION_EXPIRE_DAYS = SESSION_EXPIRE_DAYS

    def make_session_and_save(self, user_id):
        if self.session_reader.get_by_kwargs(user_id=user_id):
            raise UserAlreadyHaveSession(user_id)
        session_id = self.hasher.make_urlsafe_hash()
        session_expire_date = self.time_handler.add_days_to_current_date(self.SESSION_EXPIRE_DAYS)
        session = self.session_actor.create_record(id=session_id, user_id=session_id, expire_date=session_expire_date)
        self.session_actor.write_record_to_db(session)
        self.cacher.put_data(session_id, user_id)
        return session
