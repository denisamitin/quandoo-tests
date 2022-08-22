from enums.enums import Url
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SecurePage(BasePage):
    LOGIN_HEADER = (By.XPATH, '//h2[text()="Secure Area"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')


    def verify_successful_login(self):
        self.find_element(self.LOGIN_HEADER)
        text = "Welcome to the Secure Area. When you are done click logout below"
        for i in text.split():
            self.verify_text_present(i)

    def click_logout(self):
        self.click_element(self.LOGOUT_BUTTON)

    def verify_secure_page_without_login(self):
        self.visit(Url.secure)
        text = "You must login to view the secure area"
        for i in text.split():
            self.verify_text_present(i)
