import pytest
from auth.registration import Registrator
from auth.pydantic_models import User
from auth.exceptions import UserAlreadyExists

def get_mocks(mocker):
    user_actor = mocker.AsyncMock()
    user_reader = mocker.AsyncMock()
    hasher = mocker.Mock()
    return user_actor, user_reader, hasher

@pytest.mark.asyncio
async def test_registrate_user_success(mocker):
    user = User(name='tester', password='password')
    user_actor, user_reader, hasher = get_mocks(mocker)
    user_reader.get_record_by.return_value = None
    hasher.make_hash.return_value = 'super_long_hash'
    registrator = Registrator(user_actor, user_reader, hasher)
    result = await registrator.registrate_user(user)
    assert result is True

@pytest.mark.asyncio
async def test_registrate_user_already_exists(mocker):
    user = User(name='tester_who_already_exists', password='123')
    user_actor, user_reader, hasher = get_mocks(mocker)
    user_reader.get_record_by.return_value = 'not none'
    registrator = Registrator(user_actor, user_reader, hasher)
    with pytest.raises(UserAlreadyExists):
        await registrator.registrate_user(user)