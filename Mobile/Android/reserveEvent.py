from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By 
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import Select
import time
#######################################################
home = 3
search = 4
profile = 0
tickets = 1
likedList = 2

def waitUntilClickable(driver, by, timeout):
    return WebDriverWait(driver,timeout).until(by)
#####################################################

command_exec = "http://localhost:4723/wd/hub"
desired_cap = {
"appium:deviceName": "RF8NB0G1KVT",
  "platformName": "Android",
    "app":"O:/DriveFiles/Testing/app-release.apk"
}


desiredCap = {
  "appium:deviceName": "emulator-5554",
  "platformName": "Android",
  "appium:platformVersion": "12.0",
  "appium:udid": "emulator-5554",
  "appium:automationName": "Appium",
  "appium:newCommandTimeout": 240,
  "app":"C:/Users/moga/Downloads/Phase3_final_version.apk"
}


driver = webdriver.Remote(command_exec,desired_cap,None,None,True)
# mainScreen = driver.find_element(By.XPATH,"//android.view.View")
WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, "//android.view.View/android.widget.Button")))

driver.implicitly_wait(3)


profileTab = driver.find_element(By.XPATH,"//android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/child::android.view.View[3]/child::android.view.View[5]")

homeTab = driver.find_element(By.XPATH,"//android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/child::android.view.View[3]/child::android.view.View[1]")

searchTab = driver.find_element(By.XPATH,"//android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/child::android.view.View[3]/child::android.view.View[2]")

likedTab = driver.find_element(By.XPATH,"//android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/child::android.view.View[3]/child::android.view.View[3]")

ticketsTab = driver.find_element(By.XPATH,"//android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/child::android.view.View[3]/child::android.view.View[1]")

chooseEvent = driver.find_elements(By.XPATH,"//android.view.View[@content-desc='Learn']/child::android.widget.ImageView")


driver.implicitly_wait(3)

profileTab.click()

loginButton = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Log In')
loginButton.click()

###  Choosing to sign in with already signed up account not facebook nor google #######
continueWith = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Continue with email address']")
continueWith.click()
driver.implicitly_wait(3)
enterEmail = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.EditText")
enterEmail[0].click()
driver.implicitly_wait(2)

# ahmedsaad_2009@live.com
# 1 - 9
myEmail = "omar.sendiony@gmail.com"
myPassword = "gigrgrwgg52lany"


enterEmail[0].send_keys(myEmail)
###  next button ##########
driver.implicitly_wait(2)
# input()
enterEmail = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@content-desc='Next']")
enterEmail.click()


################  SignIn   #########################
WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText")))

password = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText")
password.click()
driver.implicitly_wait(2)
password.send_keys(myPassword)
### Login Button ###########
driver.implicitly_wait(3)
loginButton = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Log In']")
loginButton.click()
# driver.implicitly_wait(20)
WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='Log out']")))


homeTab.click()



input()
driver.quit()