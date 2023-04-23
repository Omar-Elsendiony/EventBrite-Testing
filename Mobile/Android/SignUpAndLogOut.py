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
#######################################################
command_exec = "http://localhost:4723/wd/hub"
desired_cap = {
"appium:deviceName": "RF8NB0G1KVT",
  "platformName": "Android",
    "app":"C:/Users/moga/Downloads/Phase3_final_version.apk"
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
def waitUntilClickable( by, timeout):
    return WebDriverWait.until(EC.element_to_be_clickable(by), timeout)

driver = webdriver.Remote(command_exec,desired_cap,None,None,True)



driver.implicitly_wait(5)

#   Clicking on the loginTab
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(959, 2194)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
################

driver.implicitly_wait(2)

loginButton = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Log In')
loginButton.click()

continueWith = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Continue with email address']")
continueWith.click()

myEmail = "remondaT@live.com"


action = TouchAction(driver=driver)
driver.implicitly_wait(3)
enterEmail = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.EditText")
enterEmail[0].click()
driver.implicitly_wait(2)
enterEmail[0].send_keys(myEmail)
###  next button ##########
driver.implicitly_wait(2)
enterEmail = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.Button")
enterEmail[1].click()


# ####  just like defines  #########
confirmEmail = 0
firstName = 1
surName = 2
password = 3
##################################
driver.implicitly_wait(2)
editTexts = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.EditText")
confirmEmail = editTexts[confirmEmail]
firstName = editTexts[firstName]
surName = editTexts[surName]
password = editTexts[password]

confirmEmail.click()
driver.implicitly_wait(1)
confirmEmail.send_keys("yogilany@hotmail.com")


driver.hide_keyboard()
firstName.click()
firstName.send_keys("youssef")

driver.hide_keyboard()
surName.click()
surName.send_keys("gilany")

driver.hide_keyboard()
password.click()
password.send_keys("gigrgrwgg52lany")


driver.implicitly_wait(5)
driver.hide_keyboard()
confirmEmail.click()
confirmEmail.clear()
driver.implicitly_wait(1)
confirmEmail.send_keys(myEmail)

driver.implicitly_wait(3)

signUp = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Sign Up']")
signUp.click()

driver.implicitly_wait(1)
agree = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Agree']")
agree.click()




###    Switching To home Tab #########
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(160, 2194)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

###############################################################
## add to liked list ######
# driver.implicitly_wait(2)
# likes = driver.find_elements(By.XPATH,"//android.view.View[@content-desc='Tech']/android.widget.Button[3]")
# like = likes[0]
# b = like.get_attribute('bounds')
# print(type(b))
# b =list(b)

# listOfCoordinates = list()
# i  =0
# while i < len(b)-1:
#     if (b[i] == '['): i+= 1 ;continue
#     tempBuff =""
#     while not (b[i] == ',' or b[i] == ']'):
#         tempBuff  += b[i]
#         i += 1
#     i += 1
#     listOfCoordinates.append(int(tempBuff))

# print(listOfCoordinates)
# xC = (listOfCoordinates[0] + listOfCoordinates[1]) /2
# yC = (listOfCoordinates[2] + listOfCoordinates[3]) /2

# print(xC)
# print(yC)

# driver.implicitly_wait(2)
# actions.w3c_actions._pointer_action.move_to_location(xC,yC)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()




# driver.implicitly_wait(5)
# ##   Clicking on the favorites
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(470, 2194)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
# ###############



# ###### change profile #########
# driver.implicitly_wait(2)
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(959, 2194)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
# ################

# #####  Click on edit ############
# editProfile = driver.find_elements(By.XPATH,"//android.widget.Button")
# editProfile[0].click()

# nameProfile = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Ahmed Saad']")
# nameProfile.click()

# # Edit text
# driver.implicitly_wait(2)
# editTexts = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.EditText")
# first = editTexts[0]
# last = editTexts[1]

# first.click()
# driver.implicitly_wait(1)
# first.send_keys("koko")

# driver.hide_keyboard()
# last.click()
# last.send_keys("  youssef")

# driver.implicitly_wait(1)
# saveChanges = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Save Changes']")
# saveChanges.click()

# driver.implicitly_wait(1)
# logOut = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Log out']")
# logOut.click()



input()
driver.quit()
# driver.AC_ON()