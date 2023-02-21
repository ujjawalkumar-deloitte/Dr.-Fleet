import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.Dashboard import Dashboard


class Test_005_Dashboard:
    baseURL="https://d170ul3ls6wwyw.cloudfront.net/drfleet/"
    username="kujjawal049@gmail.com"
    password="123"

    @pytest.mark.sanity
    def test_dashboard(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.db=Dashboard(self.driver)
        self.db.bestRatedDriver()
        self.db.Video()
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        #print(self.msg)
        if 'Currently there are no videos available for this trip' in self.msg:
            self.driver.save_screenshot(".\\Screenshots\\" + "No videos.png")
            assert True

        else:
            self.db.driver_Video()
            self.db.driver_Video()
            self.db.violationDropdown()
            self.driver.save_screenshot(".\\Screenshots\\" + "Driver Videos.png")

            assert True
        self.db.click_on_Dashboard()
        self.db.lastWeek()
        self.db.Totalviolation()
        self.lp.logouticon()
        self.lp.logout()