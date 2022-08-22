import json

import requests as requests

from models.login_and_registration_model import UserList, User


class LoginAndRegistrationAPI:

    def get_user_list(self, page=2) -> UserList:
        url = f"https://reqres.in/api/users?page={page}"
        response = requests.get(url=url)
        user_list = UserList(user_list=json.loads(response.text)['data'])
        return user_list

    def get_user(self, user_id=2):
        url = f"https://reqres.in/api/users/{user_id}"
        response = requests.get(url=url)
        user = User(**json.loads(response.text)['data'])
        return user

    def register_user(self, email, password):
        url = "https://reqres.in/api/register"
        response = requests.post(url=url, data={"email": email, "password": password})
        assert response.status_code == 200

    def login(self, email, password):
        url = "https://reqres.in/api/login"
        response = requests.post(url=url, data={"email": email, "password": password})
        assert response.status_code == 200
        assert json.loads(response.text).get("token") is not None, \
            "something went wrong, we didn't get a token as response to login"
