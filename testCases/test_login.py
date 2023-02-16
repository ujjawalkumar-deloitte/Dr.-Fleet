
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig



class Test_001_Login:
    baseURL="https://d170ul3ls6wwyw.cloudfront.net/drfleet/"
    username="kujjawal049@gmail.com"
    password="123"
    email="kujjawal049@gmail.com"



    def test_homePagetitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Dr. Fleet":
            self.driver.save_screenshot(".\\Screenshots\\" + "Title.png")
            assert True
            self.driver.close()

        else:
            self.driver.close()
            assert False



    def test_forgotPassword(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.lp.forgotPassword()
        self.lp.email(self.email)
        self.lp.submit()

        act_title = self.driver.title

        if act_title == "Forgot Your Password?":
            self.driver.save_screenshot(".\\Screenshots\\" + "Forgot_Password.png")
            assert True
            self.driver.close()

        else:
            self.driver.close()
            assert False


        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        #print(self.msg)
        if 'Link sent successfully' in self.msg:
            assert True
            self.driver.save_screenshot(".\\Screenshots\\" + "Link_sent.png")
        else:
            self.lp.backLogin()
            #self.driver.save_screenshot(".\\Screenshots\\" + "Not Link_sent.png")
            assert False






    @pytest.mark.sanity

    def test_login(self,setup):
        #pytest.skip("skip this test case")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.lp.logouticon()
        self.lp.logout()





