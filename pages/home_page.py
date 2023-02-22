from browser import Browser
from selenium.webdriver.common.by import By
from base_page import Base_page

class Home_page(Browser, Base_page):
    FORM_AUTHENTICATION = (By.XPATH, '//a[@href="/login"]')
    CHECKBOXES = (By.XPATH, '//a[@href="/checkboxes"]')
    DROPDOWN = (By.XPATH, '//a[@href="/dropdown"]')

    def navigate_home_page(self):
        self.chrome.get('https://the-internet.herokuapp.com')

    def click_form_auth(self):
        self.chrome.find_element(*self.FORM_AUTHENTICATION).click()

    def click_checkboxes(self):
        self.chrome.find_element(*self.CHECKBOXES).click()

    def click_dropdown(self):
        self.chrome.find_element(*self.DROPDOWN).click()

    def click_link(self, link):
        link = '*self.' + link
        self.chrome.find_element(link).click()

    def check_link_url(self, expected_url):
        self.check_url(expected_url)