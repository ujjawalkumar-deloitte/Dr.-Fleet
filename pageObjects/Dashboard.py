import time

from selenium.webdriver.common.by import By


class Dashboard:

    best_rated_driver = "(//li[contains(@class,'react-multi-carousel-item react-multi-carousel-item--active')])[1]"
    video = "//tbody/tr[1]/td[6]"
    select_video = "//div[contains(@class,'flex flex--align-center video-url-btn text text--medium-semi-bold active')]//img[contains(@alt,'thumbnail')]"
    play_video = "//div[contains(@class,'custom-player')]//div//video"
    click_on_dashboard = "/html/body/div/div[2]/div/div/div[1]"
    last_week = "/html[1]/body[1]/div[1]/div[2]/main[1]/article[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/canvas[1]"
    TotalViolation = "//div[contains(text(),'Total No. of Violations')]"
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

    def lastWeek(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.last_week).click()
        time.sleep(3)

    def Totalviolation(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.TotalViolation).click()
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