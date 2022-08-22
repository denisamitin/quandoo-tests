from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.secure_page import SecurePage


class Chrome:
    def __init__(self):
        chrome_options = Options()
        # chrome_options.headless = True
        chrome_options.add_argument('--enable-automation')
        chrome_options.add_argument('window-size=1920,1080')
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.login_page = LoginPage(self.driver)
        self.secure_page = SecurePage(self.driver)
