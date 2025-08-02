from .exceptions import UserDontExists

class UserGetter:
    def __init__(self, user_reader, session_reader, cache_client):
        self.user_reader = user_reader
        self.session_reader = session_reader
        self.cache_client = cache_client

    async def get_by_session_id(self, session_id):
        user_id = self.cache_client.get_data(session_id)
        if user_id is not None:
            user = await self.user_reader.get_by_kwargs(id=user_id)
            if not user:
                raise UserDontExists(user_id)
            return user
        user = await self.user_reader.get_by_kwargs(session_id=session_id)
        if not user:
            raise UserDontExists(user_id)
        return user

    def get_by_name(self, name):
        user = await self.user_reader.get_by_kwargs(name=name)
        if not user:
            raise UserDontExists()
        return user