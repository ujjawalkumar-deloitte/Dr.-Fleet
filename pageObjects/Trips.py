import time

from selenium.webdriver.common.by import By



class Trips:
    button_click_trips_xpath = "//div[contains(text(),'Trips')]"
    button_click_scheduledtrips_xpath = "//button[normalize-space()='Scheduled Trips']"
    button_click_delete_icon_xpath = "//tbody/tr[2]/td[5]/div[1]/button[2]//*[name()='svg']"
    button_click_yes_delete_icon_xpath = "//button[normalize-space()='Yes, delete it!']"
    button_click_cancel_icon_xpath = "//button[normalize-space()='Cancel']"
    button_click_update_icon_xpath = "//tbody/tr[1]/td[5]/div[1]/button[1]//*[name()='svg']"
    button_click_startdateicon_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[1]"
    button_select_startdate_xpath = "//button[normalize-space()='17']"
    button_click_enddateicon_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv'])[2]"
    button_click_nextmonth_xpath = "//button[@title='Next month']//*[name()='svg']"
    button_select_enddate_xpath = "//button[normalize-space()='1']"
    textbox_source_xpath = "/html/body/div/div[2]/main/article/div[2]/section/section[3]/div[1]/div[2]/div[1]/div/div/input"
    textbox_destination_xpath = "/html/body/div/div[2]/main/article/div[2]/section/section[3]/div[2]/div[2]/div/div[1]/div/div/input"
    dropdown_source_click_state = "//div[normalize-space()='Indiana']//div[@id='demo-simple-select']"
    dropdown_source_select_state = "//li[normalize-space()='Texas']"
    dropdown_source_click_city = "/html/body/div/div[2]/main/article/div[2]/section/section[3]/div[1]/div[2]/div[3]/div/div/div"
    dropdown_source_select_city = "//li[normalize-space()='Waco']"
    dropdown_dest_click_state = "//div[normalize-space()='Michigan']//div[@id='demo-simple-select']"
    dropdown_dest_select_state = "//li[normalize-space()='New York']"
    dropdown_dest_click_city = "/html/body/div/div[2]/main/article/div[2]/section/section[3]/div[2]/div[2]/div/div[3]/div/div/div"
    dropdown_dest_select_city = "//li[normalize-space()='Buffalo']"
    dropdown_click_assignDriver_xpath = "//div[@class='text-feild flex flex--justify-start']//button[@title='Open']//*[name()='svg']"
    dropdown_select_assignDriver_xpath = "//li[@id='driver-names-option-18']"
    dropdown_click_assignVehicle_xpath = "//div[@class='text-feild']//button[@title='Open']//*[name()='svg']"
    dropdown_select_assignVehicle_xpath = "//li[@id='vehicle-names-option-3']"
    button_click_save_xpath = "//button[normalize-space()='Save']"
    button_click_cancel_xpath = "//button[normalize-space()='Cancel']"
    button_click_Yescancel_xpath = "//button[normalize-space()='Yes']"
    button_click_Nocancel_xpath = "//button[normalize-space()='No']"




    def __init__(self, driver):
        self.driver = driver

    def trips(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_trips_xpath).click()
        time.sleep(3)


    def scheduledtrips(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_scheduledtrips_xpath).click()
        time.sleep(3)

    def delete(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_delete_icon_xpath).click()
        time.sleep(3)

    def yesdelete(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_yes_delete_icon_xpath).click()
        time.sleep(3)

    def cancel(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_cancel_icon_xpath).click()
        time.sleep(3)

    def update(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_update_icon_xpath).click()
        time.sleep(4)

    def clickstartdateicon(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_startdateicon_xpath).click()
        time.sleep(3)

    def selectstartdate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_select_startdate_xpath).click()
        time.sleep(3)

    def clickenddateicon(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_enddateicon_xpath).click()
        time.sleep(3)

    def selectenddate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_select_enddate_xpath).click()
        time.sleep(3)

    def nextmonth(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_nextmonth_xpath).click()
        time.sleep(3)

    def source(self,source):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_source_xpath).clear()

        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_source_xpath).send_keys(source)
        time.sleep(3)

    def destination(self,destination):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_destination_xpath).clear()

        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_destination_xpath).send_keys(destination)
        time.sleep(3)

    def clicksourcestate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_source_click_state).click()
        time.sleep(3)

    def selectsourcestate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_source_select_state).click()
        time.sleep(3)

    def clicksourcecity(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_source_click_city).click()
        time.sleep(3)

    def selectsourcecity(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_source_select_city).click()
        time.sleep(3)

    def clickdeststate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_dest_click_state).click()
        time.sleep(3)

    def selectdeststate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_dest_select_state).click()
        time.sleep(3)

    def clickdestcity(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_dest_click_city).click()
        time.sleep(3)

    def selectdestcity(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_dest_select_city).click()
        time.sleep(3)

    def clickassignDriver(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_click_assignDriver_xpath).click()
        time.sleep(3)

    def selectDriver(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_select_assignDriver_xpath).click()
        time.sleep(3)

    def clickassignVehicle(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_click_assignVehicle_xpath).click()
        time.sleep(3)

    def selectVehicle(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.dropdown_select_assignVehicle_xpath).click()
        time.sleep(3)

    def save(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_click_save_xpath).click()
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





