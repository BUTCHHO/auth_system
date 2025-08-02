import pytest
from django.contrib.auth import authenticate

from auth.pydantic_models import User
from auth.authentication import Authenticator

def get_mocks(mocker):
    user_getter = mocker.Mock()
    hasher = mocker.Mock()
    session_maker = mocker.Mock()
    return user_getter, hasher, session_maker


def test_auth_by_name_and_psw_and_return_session_success(mocker):
    user = User(id=333, name='tester', password='super_long_hash')
    user_getter, hasher, session_maker = get_mocks(mocker)
    user_getter.get_by_name.return_value = user
    hasher.compare_password_hashes.return_value = True
    session_maker.make_session_and_save.return_value = True
    authenticator = Authenticator(user_getter, hasher, session_maker)
    result = authenticator.auth_by_name_and_psw_and_return_session(user.name, user.password)
    assert result is True
