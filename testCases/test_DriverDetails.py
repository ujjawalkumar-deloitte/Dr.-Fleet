import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.Driver_Details import Driver_Details


class Test_006_Driver_Details:
    baseURL="https://d170ul3ls6wwyw.cloudfront.net/drfleet/"
    username="kujjawal049@gmail.com"
    password="123"



    def test_driver_videos(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.dd=Driver_Details(self.driver)
        self.dd.Driver_details()
        self.dd.driverRating()
        self.dd.completedTrip()
        self.dd.flaggedStatus()
        self.driver.refresh()
        self.dd.Allvideos()
        self.driver.refresh()
        self.dd.driver_VideoFeed()
        self.dd.violationDropdown()
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        if 'Currently there are no videos available for this trip' in self.msg:
            self.driver.save_screenshot(".\\Screenshots\\" + "No trip video.png")
            assert True

        else:
            self.dd.driver_Video()
            self.dd.driver_Video()
            assert True
        self.lp.logouticon()
        self.lp.logout()
        self.driver.close()

    def test_driver_info(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.dd=Driver_Details(self.driver)
        self.dd.Driver_details()
        self.dd.driverInfo()
        self.dd.Videofeed()
        self.dd.violationDropdown()
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        if 'Currently there are no videos available for this trip' in self.msg:
            self.driver.save_screenshot(".\\Screenshots\\" + "No trip video.png")
            assert True

        else:
            self.dd.driver_Video()
            self.dd.driver_Video()
            assert True
        self.lp.logouticon()
        self.lp.logout()
        self.driver.close()


