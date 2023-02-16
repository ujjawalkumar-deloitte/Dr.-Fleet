import time

from selenium.webdriver.common.by import By

class Driver_Details:
    driver_details = "//div[contains(text(),'Driver Details')]"
    Flag_sorting = "//th[2]//div[1]//button[1]//*[name()='svg']"
    driver_rating_sorting = "//th[3]//div[1]//button[1]//*[name()='svg']"
    completed_trip_sorting = "//th[4]//div[1]//button[1]//*[name()='svg']"
    driver_Allvideos = "//tbody/tr[1]/td[5]/div[1]/div[1]/button[1]//*[name()='svg']"
    driver_videofeed = "(//div[contains(text(),'Sunil Kumar - 4.3')])[1]"
    driver_video = "//div[@class='custom-player']//div//video"
    violation_dropdown = "(//*[name()='path'])[56]"
    driver_info = "//tbody/tr[1]/td[5]/div[1]/div[2]/button[1]//*[name()='svg']"
    video_feed = "//tbody/tr[1]/td[6]/button[1]//*[name()='svg']"







    def __init__(self, driver):
        self.driver = driver


    def Driver_details(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.driver_details).click()
        time.sleep(3)


    def flaggedStatus(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Flag_sorting).click()
        time.sleep(3)

    def driverRating(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.driver_rating_sorting).click()
        time.sleep(3)

    def completedTrip(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.completed_trip_sorting).click()
        time.sleep(3)

    def Allvideos(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.driver_Allvideos).click()
        time.sleep(3)


    def driver_VideoFeed(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.driver_videofeed).click()
        time.sleep(3)

    def driver_Video(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.driver_video).click()
        time.sleep(3)

    def violationDropdown(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.violation_dropdown).click()
        time.sleep(3)

    def driverInfo(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.driver_info).click()
        time.sleep(3)

    def Videofeed(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.video_feed).click()
        time.sleep(3)