from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class AdminLocators:

    USERNAME_LOCATOR = (By.NAME, 'username')
    PASSWD_LOCATOR = (By.NAME, 'password')
    LOGIN_BUTTON_LOCATOR = (By.NAME, 'login')


class AdminPage(BasePage):

    def login(self, user_name, passwd):
        username_filed = self.find_element(AdminLocators.USERNAME_LOCATOR)
        username_filed.send_keys(user_name)
        passwd_filed = self.find_element(AdminLocators.PASSWD_LOCATOR)
        passwd_filed.send_keys(passwd)
        login_button = self.find_element(AdminLocators.LOGIN_BUTTON_LOCATOR)
        login_button.click()



