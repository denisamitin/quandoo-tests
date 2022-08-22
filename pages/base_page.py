import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from enums.enums import Wait, Url

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = Wait.MEDIUM

    def visit(self, url):
        self.driver.get(self.get_url(url))
        logger.info(f'Opened page {url}.')

    def click_element(self, locator, name_of_element=None):
        if name_of_element is not None:
            logger.info(f'Click on: "{name_of_element}"')
        self.verify_element_is_clickable(locator).click()

    def fill_input(self, locator, value, name_of_element=None):
        if name_of_element is not None:
            logger.info(f'Fill element: "{name_of_element}" with value: \n{value}')
        self.find_element(locator).send_keys(value)

    def verify_text_present(self, text, error_text=None):
        assert text in self.driver.page_source, error_text

    def verify_element_is_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(locator))
        except Exception as e:
            logger.error(f'Element is not clickable by locator: {locator}, exception:\n {e.args[0]}')

    def find_element(self, locator, visibility=True, timeout=Wait.MEDIUM):
        condition = ec.visibility_of_element_located if visibility else ec.presence_of_element_located
        try:
            return WebDriverWait(self.driver, timeout=timeout).until(condition(locator))
        except Exception as e:
            logger.error(f'Element was not found by locator: {locator}, exception:\n {e.args[0]}')

    @staticmethod
    def get_url(url):
        return f'{Url.base_url}{url}'
