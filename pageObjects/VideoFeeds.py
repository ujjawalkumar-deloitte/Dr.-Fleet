import time

from selenium.webdriver.common.by import By

class VideoFeeds:
    button_click_videofeed_xpath = "//div[contains(text(),'Video Feeds')]"
    button_click_ongoingtrip_xpath = "//button[normalize-space()='Ongoing Trips']"
    button_click_completedtrip_xpath = "//button[normalize-space()='Completed Trips']"
    button_click_dateDropdown_xpath = "//div[@id='sort-cards-dropdown']"
    button_click_violation_xpath = "//li[normalize-space()='No. of violations']"
    button_click_sorting_xpath = "//div[@class='sorting-wrapper flex flex--justify-center flex--align-start']//button[@type='button']//*[name()='svg']"
    button_click_date_xpath = "//li[normalize-space()='Date']"
    button_click_logouticon_xpath = "/html/body/div/div[1]/div/div[2]/div[2]/svg"
    button_click_video_xpath = "//*[@id='root']/div[2]/main/article/div[2]/section[3]/div/div/div/div[1]/li[1]/img"
    button_click_violationdropdown_xpath = "(//*[name()='path'])[56]"
    button_play_video_xpath = "//div[@class='custom-player']//div//video"
    button_searchbox_xpath = "//input[@placeholder='Search…']"
    button_clicksearch_xpath = "(//*[name()='svg'][@type='submit'])[1]"
    button_click_logout_xpath = "//div[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def videofeed(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_videofeed_xpath).click()
        time.sleep(3)

    def ongoingtrip(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_ongoingtrip_xpath).click()
        time.sleep(3)

    def completedtrip(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_completedtrip_xpath).click()
        time.sleep(3)

    def dateDropdown(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_dateDropdown_xpath).click()
        time.sleep(3)

    def violation(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_violation_xpath).click()
        time.sleep(3)

    def dates(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_date_xpath).click()
        time.sleep(3)

    def sorting(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_sorting_xpath).click()
        time.sleep(3)

    def logouticon(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_logouticon_xpath).click()
        time.sleep(3)

    def logout(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_logout_xpath).click()
        time.sleep(3)

    def video(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_video_xpath).click()
        time.sleep(3)

    def violationDropdown(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_violationdropdown_xpath).click()
        time.sleep(3)

    def playvideo(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_play_video_xpath).click()
        time.sleep(3)

    def pausevideo(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_play_video_xpath).click()
        time.sleep(3)

    def search(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_searchbox_xpath).send_keys("ujjw")
        time.sleep(3)

    def clicksearch(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_clicksearch_xpath).click()
        time.sleep(3)