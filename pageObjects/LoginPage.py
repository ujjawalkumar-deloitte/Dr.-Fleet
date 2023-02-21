import time

from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "//input[@type='email']"
    textbox_password_xpath = "//input[@type='password']"
    button_login_xpath = "//button[normalize-space()='Login']"
    button_eyeicon_xpath = "//button[@aria-label='toggle password visibility']//*[name()='svg']"
    button_forgotPassword_xpath = "//a[normalize-space()='Forgot your password?']"
    textbox_email_xpath = "/html/body/div/div/section[2]/div[2]/div[1]/div/input"
    button_click_submit_xpath = "//button[normalize-space()='Submit']"
    button_backLogin_xpath = "//a[normalize-space()='Go back to login page']"
    button_logouticon_xpath = "(//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault avatar css-154ogbs'])[1]"
    button_clicklogout_xpath = "/html/body/div[2]/div[3]/ul/li/div/div[2]"



    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def login(self):
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        time.sleep(7)

    def eye(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_eyeicon_xpath).click()
        time.sleep(3)

    def forgotPassword(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_forgotPassword_xpath).click()
        time.sleep(3)

    def email(self,email):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)
        time.sleep(3)

    def submit(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_submit_xpath).click()
        time.sleep(3)

    def backLogin(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_backLogin_xpath).click()
        time.sleep(3)

    def logouticon(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_logouticon_xpath).click()
        time.sleep(3)

    def logout(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_clicklogout_xpath).click()
        time.sleep(3)

