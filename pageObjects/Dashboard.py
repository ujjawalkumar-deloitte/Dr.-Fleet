import time

from selenium.webdriver.common.by import By


class Dashboard:

    best_rated_driver = "//ul[1]//li[1]//div[1]//div[1]//div[1]//*[name()='svg']"
    video = "//tbody/tr[1]/td[6]"
    select_video = "//div[contains(@class,'flex flex--align-center video-url-btn text text--medium-semi-bold active')]//img[contains(@alt,'thumbnail')]"
    play_video = "//div[contains(@class,'custom-player')]//div//video"
    click_on_dashboard = "/html/body/div/div[2]/div/div/div[1]"
    last_month = "//div[@class='last-month-pie-chart']//canvas[@role='img']"
    last_to_last_month = "//div[@class='last-to-last-month-pie-chart']//canvas[@role='img']"
    driver_video = "//div[@class='custom-player']//div//video"
    violation_dropdown = "(//*[name()='path'])[56]"


    def __init__(self, driver):
        self.driver = driver



    def Video(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.video).click()
        time.sleep(3)

    def select_video(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.select_video).click()
        time.sleep(3)

    def play_video(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.play_video).click()
        time.sleep(3)

    def click_on_Dashboard(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_on_dashboard).click()
        time.sleep(3)

    def lastMonth(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.last_month).click()
        time.sleep(3)

    def last_to_last_Month(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.last_to_last_month).click()
        time.sleep(3)

    def bestRatedDriver(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.best_rated_driver).click()
        time.sleep(3)

    def driver_Video(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.driver_video).click()
        time.sleep(3)

    def violationDropdown(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.violation_dropdown).click()
        time.sleep(3)