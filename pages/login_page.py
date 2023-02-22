from browser import Browser
from selenium.webdriver.common.by import By
from base_page import Base_page

class Login_page(Browser, Base_page):
    USERNAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@class="flash error"]')

    def navigate_login_page(self):
        self.chrome.get('https://the-internet.herokuapp.com/login')

    def correct_user(self):
        self.chrome.find_element(*self.USERNAME).send_keys('tomsmith')

    def correct_pass(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')

    def insert_user(self, username):
        self.chrome.find_element(*self.USERNAME).send_keys(username)

    def insert_pass(self, password):
        self.chrome.find_element(*self.PASSOWRD).send_keys(password)

    def click_login(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def check_loginPage_url(self):
        self.Base_page.check_url()

    def check_login_error_message(self, expected_error_message):
        self.check_error_message(*self.ERROR_MESSAGE, expected_error_message)