import pytest

from enums.enums import LoginData


@pytest.mark.login
@pytest.mark.frontend
def test_login(frontend):
    # regular login as correct user
    frontend.login_page.go_to_login_page()
    frontend.login_page.login_to_site(email=LoginData.login, password=LoginData.password)
    frontend.secure_page.verify_successful_login()


@pytest.mark.login
@pytest.mark.frontend
@pytest.mark.parametrize("email, password, expected_message", [
    [LoginData.login, "", "password"],
    ["", LoginData.password, "login"],
    [LoginData.login, "123", "password"],
    ["123", LoginData.password, "login"],
    ["123", "123", "login"]])
def test_wrong_credentials(frontend, email, password, expected_message):
    # login with empty and wrong credentials
    frontend.login_page.go_to_login_page()
    frontend.login_page.login_to_site(email=email, password=password)
    frontend.login_page.verify_unsuccessful_login(expected_message)


@pytest.mark.login
@pytest.mark.frontend
def logout_test(frontend):
    # check the successful logout
    frontend.login_page.go_to_login_page()
    frontend.login_page.login_to_site(email=LoginData.login, password=LoginData.password)
    frontend.secure_page.verify_successful_login()
    frontend.secure_page.click_logout()
    frontend.login_page.verify_page_elements()

@pytest.mark.login
@pytest.mark.frontend
def test_get_to_secure_page(frontend):
    # check that we actually need to login to see a secure page
    frontend.secure_page.verify_secure_page_without_login()
