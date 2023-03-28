# import os
# prefixed = [filename for filename in os.listdir("C:\Program Files") if filename.startswith("Wind")]
# print(prefixed)
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
options = Options()
driver = webdriver.Chrome(service=Service("O:\DriveFiles\Drivers\chromedriver_win32 (1)\chromedriver.exe"))
driver.maximize_window()
# driver.get("https:\\google.com")
# print(driver.title)
driver.get("https://opensource-demo.orangehrmlive.com")
# driver.get("https://google.com")
# driver.back()
# google = driver.find_element(By.NAME,"q")
driver.implicitly_wait(2)
txtUserName = driver.find_element(By.NAME,'username')
txtPass = driver.find_element(By.NAME,"password")
loginBtn = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')


# txtUsername.clear()
# txtUserName.send_keys("Admin")
# txtPass.send_keys("admin123")
# loginBtn.click()
#
# # print(txtUsername.is_displayed())
# # print(username.is_enabled())
#
# # time.sleep(2)
# print(driver.title)
# driver.forward()
input()
