from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.VideoFeeds import VideoFeeds



class Test_002_VideoFeed:
    baseURL = "https://d170ul3ls6wwyw.cloudfront.net/drfleet/"
    username = "kujjawal049@gmail.com"
    password = "123"




    @pytest.mark.sanity
    def test_videofeed(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.vf = VideoFeeds(self.driver)
        self.vf.videofeed()
        self.vf.ongoingtrip()
        self.vf.completedtrip()
        self.vf.dateDropdown()
        self.vf.violation()
        self.vf.sorting()
        self.vf.dateDropdown()
        self.vf.dates()
        self.vf.video()
        self.vf.violationDropdown()
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        if 'Currently there are no videos available for this trip' in self.msg:
            self.driver.save_screenshot(".\\Screenshots\\" + "No video feeds.png")
            assert True

        else:
            self.vf.playvideo()
            self.vf.pausevideo()
            self.lp.logouticon()
            self.lp.logout()
            self.driver.close()
            assert True



    @pytest.mark.sanity
    def test_searchBox(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.vf = VideoFeeds(self.driver)
        self.vf.videofeed()
        self.vf.ongoingtrip()
        self.vf.completedtrip()
        self.vf.search()
        self.vf.clicksearch()
        self.lp.logouticon()
        self.lp.logout()
