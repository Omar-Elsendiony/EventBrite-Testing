from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


opts = webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")
websiteURL = "https://google.com"
serv_obj = Service("O:\DriveFiles\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=opts)
driver.get(websiteURL)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@role='button']")))
inputTextBoxInGoogle = driver.find_element(By.XPATH,"//input[contains(@class,'gLFy')]")
inputTextBoxInGoogle.send_keys("Hello World")
driver.title
