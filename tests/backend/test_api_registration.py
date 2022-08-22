import pytest

from api.login_and_registration_api import LoginAndRegistrationAPI


@pytest.mark.login
@pytest.mark.backend
@pytest.mark.parametrize("email, password", [["eve.holt@reqres.in", "pistol"]])
def test_get_user_list(email, password):
    api = LoginAndRegistrationAPI()
    # I couldn't quite get the first part about getting the user because we didn't have any security measures in a requset
    api.get_user()
    api.register_user(email=email, password=password)
    # after that I would have checked if user actually added to user list, but it is mock, so I don't have that step
    api.login(email=email, password=password)
