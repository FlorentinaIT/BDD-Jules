from selenium.webdriver.common.by import By

from base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/div/input')
    PASSWORD = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input')
    BUTTON = (By.CLASS_NAME, 'class="css-17qmje5"')
    def navigate_to_login_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def insert_correct_email(self):
        self.chrome.find_element(*self.EMAIL).send_keys('florentina.burnuz@gmail.com')

    def insert_correct_password(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('Jules@123')

    def click_login_button(self):
        self.chrome.find_element(*self.BUTTON).click()