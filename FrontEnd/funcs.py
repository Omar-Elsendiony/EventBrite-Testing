from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

def elements(driver, xpath):
    try:
        return driver.find_elements_by_xpath(xpath)
    except:
        print("Not found")
        
def ClickFnHttp(Driver,http,DelayTime = 1): 
    try:
        button = Driver.find_element(by=By.XPATH,value=http)
        time.sleep(DelayTime)
        button.click()
        time.sleep(DelayTime)
    except:
        print("Not found")

def SendKeysFnHttp(Driver,http,value,DelayTime = 1):
    try:
        button = Driver.find_element(by=By.XPATH, value=http)
        time.sleep(DelayTime)
        button.send_keys(value)
        time.sleep(DelayTime)
    except:
        print("Not found")

