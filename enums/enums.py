
class Wait:
    EXTRA_SHORT = 1
    SHORT = 3
    MEDIUM = 5
    LONG = 10


class Url:
    base_url = "http://the-internet.herokuapp.com"
    login = "/login"
    secure = "/secure"


class LoginData:
    # it is not a secure way to store logins and passwords for tests, but will work in example
    login = "tomsmith"
    password = "SuperSecretPassword!"
