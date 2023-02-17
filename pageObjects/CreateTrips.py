import time
from selenium.webdriver.common.by import By


class CreateTrips:
    button_click_trips_xpath = "//div[contains(text(),'Trips')]"
    button_createtrip_xpath = "//button[@class='add-trip-btn']//*[name()='svg']"
    button_startcalendar_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[1]"
    button_selectDate_xpath = "//button[normalize-space()='24']"
    button_endcalendar_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[2]"
    button_nextmonth_xpath = "//button[@title='Next month']//*[name()='svg']"
    button_endselectDate_xpath = "//button[normalize-space()='21']"
    textbox_source_xpath = "/html/body/div/div[2]/main/article/div[2]/section/section[3]/div[1]/div[2]/div[1]/div/div/input"
    textbox_destination_xpath = "/html/body/div/div[2]/main/article/div[2]/section/section[3]/div[2]/div[2]/div/div[1]/div/div/input"
    dropdown_source_clickState_xpath = "/html/body/div/div[2]/main/article/div[2]/section/section[3]/div[1]/div[2]/div[2]/div/div/div"
    dropdown_source_selectState_xpath = "//li[normalize-space()='Ohio']"
    dropdown_source_clickCity_xpath = "/html/body/div/div[2]/main/article/div[2]/section/section[3]/div[1]/div[2]/div[3]/div/div/div"
    dropdown_source_selectCity_xpath = "//li[normalize-space()='Parma']"
    dropdown_destination_clickState_xpath = "/html/body/div/div[2]/main/article/div[2]/section/section[3]/div[2]/div[2]/div/div[2]/div/div/div"
    dropdown_destination_selectState_xpath = "//li[normalize-space()='Texas']"
    dropdown_destination_clickCity_xpath = "/html/body/div/div[2]/main/article/div[2]/section/section[3]/div[2]/div[2]/div/div[3]/div/div/div"
    dropdown_destination_selectCity_xpath = "//li[normalize-space()='Tyler']"
    dropdown_click_assignVehicle_xpath = "//div[@class='text-feild']//button[@title='Open']//*[name()='svg']"
    dropdown_select_vehicle_xpath = "//li[@id='vehicle-names-option-0']"
    dropdown_click_assignDriver_xpath = "//input[@id='driver-names']"
    dropdown_select_driver_xpath = "//li[@id='driver-names-option-1']"
    button_click_create_xpath = "//button[normalize-space()='Create']"
    button_click_cancel_xpath = "//button[normalize-space()='Cancel']"
    button_click_Yescancel_xpath = "//button[normalize-space()='Yes']"
    button_click_Nocancel_xpath = "//button[normalize-space()='No']"
    button_click_scheduledtrips_xpath = "//button[normalize-space()='Scheduled Trips']"
    textbox_searcbox_xpath = "//input[@placeholder='Search…']"
    clicksearch = "(//*[name()='svg'][@type='submit'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def trip(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_trips_xpath).click()
        time.sleep(3)

    def createtrip(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_createtrip_xpath).click()
        time.sleep(3)

    def startcalendar(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_startcalendar_xpath).click()
        time.sleep(3)

    def selectdate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_selectDate_xpath).click()
        time.sleep(3)

    def endcalendar(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_endcalendar_xpath).click()
        time.sleep(3)

    def nextmonth(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_nextmonth_xpath).click()
        time.sleep(3)

    def endselectdate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_endselectDate_xpath).click()
        time.sleep(3)

    def source(self,source):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_source_xpath).send_keys(source)
        time.sleep(3)

    def destination(self,destination):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_destination_xpath).send_keys(destination)
        time.sleep(3)

    def sourceClickState(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_source_clickState_xpath).click()
        time.sleep(3)

    def sourceSelectState(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_source_selectState_xpath).click()
        time.sleep(3)


    def sourceClickCity(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_source_clickCity_xpath).click()
        time.sleep(3)

    def sourceSelectCity(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_source_selectCity_xpath).click()
        time.sleep(3)

    def destinationClickState(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_destination_clickState_xpath).click()
        time.sleep(3)

    def destinationSelectState(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_destination_selectState_xpath).click()
        time.sleep(3)

    def destinationClickCity(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_destination_clickCity_xpath).click()
        time.sleep(3)

    def destinationSelectCity(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_destination_selectCity_xpath).click()
        time.sleep(3)

    def assignDriver(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_click_assignDriver_xpath).click()
        time.sleep(3)

    def selectDriver(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_select_driver_xpath).click()
        time.sleep(3)

    def assignVehicle(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_click_assignVehicle_xpath).click()
        time.sleep(3)

    def selectvehicle(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_select_vehicle_xpath).click()
        time.sleep(3)

    def clickCreate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_create_xpath).click()
        time.sleep(3)

    def cancel(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_cancel_xpath).click()
        time.sleep(3)

    def Yescancel(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_Yescancel_xpath).click()
        time.sleep(3)

    def Nocancel(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_Nocancel_xpath).click()
        time.sleep(3)

    def search(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_searcbox_xpath).send_keys("UP36TX3854")
        time.sleep(3)

    def clicksearch(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.clicksearch).click()
        time.sleep(3)

    def scheduledtrips(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_scheduledtrips_xpath).click()
        time.sleep(3)