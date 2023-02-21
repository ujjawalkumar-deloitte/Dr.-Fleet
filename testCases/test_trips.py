from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.Trips import Trips



class Test_003_Trips:
    baseURL = "https://d170ul3ls6wwyw.cloudfront.net/drfleet/"
    username = "kujjawal049@gmail.com"
    password = "123"
    source = " street"
    destination = " street"

    @pytest.mark.sanity
    def test_trips(self,setup):
        #pytest.skip("skip this test case")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.tr=Trips(self.driver)
        self.tr.trips()
        self.tr.scheduledtrips()
        self.tr.delete()
        #self.tr.yesdelete()
        self.tr.cancel()
        self.tr.update()
        self.tr.clickstartdateicon()
        self.tr.selectstartdate()
        self.tr.clickenddateicon()
        self.tr.nextmonth()
        self.tr.selectenddate()
        self.tr.source(self.source)
        self.tr.clicksourcestate()
        self.tr.selectsourcestate()
        self.tr.clicksourcecity()
        self.tr.selectsourcecity()
        self.tr.destination(self.destination)
        self.tr.clickdeststate()
        self.tr.selectdeststate()
        self.tr.clickdestcity()
        self.tr.selectdestcity()
        self.tr.clickassignDriver()
        self.tr.selectDriver()
        self.tr.clickassignVehicle()
        self.tr.selectVehicle()
        self.tr.cancel()
        self.tr.Nocancel()
        #self.tr.Yescancel()
        self.tr.save()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        if 'Trip saved successfully' in self.msg:
            self.driver.save_screenshot(".\\Screenshots\\" + "Trip_updated.png")
            assert True

        else:
            self.lp.logouticon()
            self.lp.logout()
            self.driver.close()

        