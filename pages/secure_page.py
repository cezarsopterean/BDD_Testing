from browser import Browser
from selenium.webdriver.common.by import By

class Secure_page(Browser):
    SUCCESS_MESSAGE = (By.XPATH, '//h4[@class="subheader"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')

    def navigate_secure_page(self):
        self.chrome.get('https://the-internet.herokuapp.com/secure')

    def check_success_message(self):
        actual = self.chrome.find_element(*self.SUCCESS_MESSAGE).text
        expected = 'Welcome to the Secure Area'
        assert expected in actual, f'Error: Expected "{expected}" message not in {actual}'

    def click_logout(self):
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()