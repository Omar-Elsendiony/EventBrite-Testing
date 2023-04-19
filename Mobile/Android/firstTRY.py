from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

#######################################################
command_exec = "http://localhost:4723/wd/hub"
desired_cap = {
"appium:deviceName": "RF8NB0G1KVT",
  "platformName": "Android"
}

desiredCap = {
  "appium:deviceName": "emulator-5554",
  "platformName": "Android",
  "appium:platformVersion": "12.0",
  "appium:udid": "emulator-5554",
  "appium:automationName": "Appium",
  "appium:newCommandTimeout": 240,
}
  # "app":"C:/Users/moga/Downloads/mWord.apk"

driver = webdriver.Remote(command_exec,desiredCap,None,None,True)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(521, 1349)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(622, 618)
actions.w3c_actions.pointer_action.release()
actions.perform()

settings = driver.find_element(AppiumBy.ID,"//android.widget.TextView[@content-desc='Settings']")
settings.click()


#driver.hide_keyboard()

# playStore = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@content-desc='Play Store']")
# playStore.click()
# input()
driver.quit()
# driver.AC_ON()