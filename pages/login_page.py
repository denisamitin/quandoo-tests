from enums.enums import Url
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN_HEADER = (By.XPATH, '//h2[text()="Login Page"]')
    LOGIN_INPUT = (By.CSS_SELECTOR, '[id="username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')

    def go_to_login_page(self):
        self.visit(Url.login)
        # Verify that page is loaded
        self.find_element(self.LOGIN_HEADER)

    def login_to_site(self, email, password):
        self.fill_input(self.LOGIN_INPUT, email)
        self.fill_input(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def verify_unsuccessful_login(self, reason="login"):
        text = f"Your {reason} is invalid!"
        # I could put it in method, but sometimes we need exact phrase, so I think it is better to stay that way
        for i in text.split():
            self.verify_text_present(i)

    def verify_page_elements(self):
        self.find_element(self.LOGIN_HEADER)
        text = "This is where you can log into the secure area. Enter tomsmith for the username and " \
               "SuperSecretPassword! for the password. If the information is wrong you should see error messages."
        for i in text.split():
            self.verify_text_present(i)
