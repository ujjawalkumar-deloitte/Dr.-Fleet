import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.CreateTrips import CreateTrips

class Test_004_CreateTrip:
    baseURL = "https://d170ul3ls6wwyw.cloudfront.net/drfleet/"
    username = "kujjawal049@gmail.com"
    password = "123"
    startDate= "15-02-2023"
    endDate = "05-03-2023"
    source = "London"
    destination = "clock tower"


    @pytest.mark.sanity
    def test_createTrip(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.tr=CreateTrips(self.driver)
        self.tr.trip()
        self.tr.createtrip()
        self.tr.startcalendar()
        self.tr.selectdate()
        self.tr.endcalendar()
        self.tr.nextmonth()
        self.tr.endselectdate()
        self.tr.source(self.source)
        self.tr.destination(self.destination)
        self.tr.sourceClickState()
        self.tr.sourceSelectState()
        self.tr.sourceClickCity()
        self.tr.sourceSelectCity()
        self.tr.destinationClickState()
        self.tr.destinationSelectState()
        self.tr.destinationClickCity()
        self.tr.destinationSelectCity()
        self.tr.assignDriver()
        self.tr.selectDriver()
        self.tr.assignVehicle()
        self.tr.selectvehicle()
        self.tr.clickCreate()
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'Trip saved successfully' in self.msg:
            assert True
            self.driver.save_screenshot(".\\Screenshots\\" + "Trip_created.png")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Not Trip_created.png")
            assert False

        # self.tr.cancel()
        # self.tr.Yescancel()
        #self.tr.Nocancel()
