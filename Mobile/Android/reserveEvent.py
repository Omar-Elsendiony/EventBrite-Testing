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





driver.implicitly_wait(3)

profileTab.click()

loginButton = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Log In')
loginButton.click()

###  Choosing to sign in with already signed up account not facebook nor google #######
# input()


continueWith = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Continue With Google']")
continueWith.click()
time.sleep(3)
myGmail = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]")
myGmail.click()
## /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]

WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='Log out']")))

homeTab = driver.find_element(By.XPATH,"//android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/child::android.view.View/child::android.view.View[2]/child::android.view.View[1]")
homeTab.click()
WebDriverWait(driver, 32).until(EC.presence_of_element_located((By.XPATH,"//android.view.View[@content-desc='Learn']")))
time.sleep(3)

chooseEvent = driver.find_elements(AppiumBy.XPATH,"//android.view.View/android.widget.ImageView")
chooseEvent[3].click()

WebDriverWait(driver, 32).until(EC.presence_of_element_located((By.XPATH,"//android.widget.ImageView")))

WebDriverWait(driver, 32).until(EC.presence_of_element_located((By.XPATH,"//android.view.View[@content-desc='Organizer']")))

tickets = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Tickets']") 
tickets.click()

WebDriverWait(driver, 32).until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='Check out']")))

plusButtons = driver.find_element(AppiumBy.XPATH,"//android.view.View/child::android.widget.Button[2]")
plusButtons.click()
# plusButtons[1].click()

checkout = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Check out']")
checkout.click()

WebDriverWait(driver,32).until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='Place order']")))

# fName = driver.find_element(AppiumBy.XPATH,"//android.view.View/android.view.View/android.view.View/android.widget.ImageView/child::android.widget.EditText[3]")

# fName.send_keys("omar")

# secondName = driver.find_element(AppiumBy.XPATH,"//android.view.View/android.view.View/android.view.View/android.widget.ImageView/child::android.widget.EditText[4]")

# secondName.send_keys("Sendo")

# email = driver.find_element(AppiumBy.XPATH,"//android.view.View/android.view.View/android.view.View/android.widget.ImageView/child::android.widget.EditText[5]")

# email.send_keys("omar.sendo@gmail.com")

texts = driver.find_elements(By.XPATH,"//android.widget.EditText")
texts[0].click()
texts[0].send_keys("omar")
driver.hide_keyboard()
texts[1].click()
texts[1].send_keys("send")
driver.hide_keyboard()
texts[2].click()
texts[2].send_keys("mora")
driver.hide_keyboard()
texts[3].click()
texts[3].send_keys("mora")
driver.hide_keyboard()
texts[4].click()
texts[4].send_keys("omar.sendo@gmail.com")
driver.hide_keyboard()

driver.implicitly_wait(2)

placeOrder = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Place order']")
placeOrder.click()

# //android.view.View/child::android.widget.Button[2]
# //android.view.View[@content-desc="Organizer"]

input()
driver.quit()