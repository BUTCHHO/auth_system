from hasher import Hasher
from time_handler import TimeHandler

class SessionMaker:
    def __init__(self, session_expire_time, session_access, cacher):
        """
        :param session_expire_time: expire time in days
        :param session_access: access to model Session in your database
        :param cacher: your cache system (redis, memcache, doesn't matter
        but it must implement method 'put_data(key, value)')
        """
        self.expire_time = session_expire_time
        self._access = session_access
        self.cacher = cacher

    def _get_expire_date(self):
        return TimeHandler.add_days_to_current_date(self.expire_time)

    def _create_session_id(self):
        hashed_id = Hasher.create_session_id_hash()
        return hashed_id

    def _create_session_obj(self, user_id):
        session_id = self._create_session_id()
        expire_date = self._get_expire_date()
        session_record = self._access.create_record(id=session_id, expire_date=expire_date, user_id=user_id)
        return session_record

    def make_session(self, user_id):
        session = self._create_session_obj(user_id)
        session_id = session.id
        self._access.write_record_to_db(session)
        self.cacher.put_data(session_id, user_id)
        return session_id