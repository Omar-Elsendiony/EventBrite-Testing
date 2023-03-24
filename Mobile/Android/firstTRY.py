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
driver = webdriver.Remote(command_exec,desired_cap,None,None,True)
playStore = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@content-desc='Play Store']")
playStore.click()
input()
driver.quit()
# driver.AC_ON()