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
# logIn = allTabs[1]
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
enterEmail[0].send_keys("ahmedsaad_2009@live.com")
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
password.send_keys("123456789")
### Login Button ###########
driver.implicitly_wait(3)
loginButton = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Log In']")
loginButton.click()
# driver.implicitly_wait(20)
WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH,"//android.widget.Button[@content-desc='Log out']")))





########Change profile name ################
# driver.implicitly_wait(13)
WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, "//android.view.View/android.view.View/android.view.View/android.view.View/child::android.widget.Button[1]")))


editProfile = driver.find_element(AppiumBy.XPATH,"//android.view.View/android.view.View/android.view.View/android.view.View/child::android.widget.Button[1]")


###   Edit name #########
# editProfile.click()
# nameProfile = driver.find_element(By.XPATH,"//android.view.View[@content-desc='Name']/android.widget.Button")
# nameProfile.click()
# # driver.push_file()
# # Edit text
# driver.implicitly_wait(2)
# editTexts = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.EditText")
# first = editTexts[0]
# last = editTexts[1]

# first.click()
# driver.implicitly_wait(1)
# first.clear()
# first.send_keys("koko")

# driver.hide_keyboard()
# last.click()
# last.clear()
# last.send_keys(" youssef")

# driver.implicitly_wait(1)
# saveChanges = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Save Changes']")
# saveChanges.click()
#####################################################################


######### Change profile picture ############
# driver.implicitly_wait(13)
# editProfile.click()
# uploadPicture = driver.find_element(AppiumBy.XPATH,"//*[@content-desc='Update Picture']")
# # driver.push_file(uploadPicture,None,"/Internal storage/DCIM/Screenshots/Omar.jpg")
# # uploadPicture.send_keys("/Internal storage/DCIM/Screenshots/Omar.jpg")

# uploadPicture.click()
# photoOptions = driver.find_elements(By.ID,"com.google.android.documentsui:id/icon_thumb")

# photoOptions[0].click()


#####################   Manage Events  ####################

manageEvents = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Manage Events")
manageEvents.click()
## plus button ##
# /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button
WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button")))

plusButton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button")
plusButton.click()
WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText")))

eventTitle = driver.find_element(By.XPATH,"//android.widget.EditText")
eventTitle.send_keys("balady vs sorra")

nextButton = driver.find_element(By.XPATH,"//android.widget.Button")
nextButton.click()


summary = driver.find_element(By.XPATH,"//android.widget.EditText")
summary.send_keys("This is a brief summary")
nextButton = driver.find_element(By.XPATH,"//android.widget.Button")
nextButton.click()

dayButton = driver.find_element(By.XPATH,"(//android.view.View[@content-desc='Day'])[1]")
dayButton.click()
##  parse date and remove the first two commas ######
driver.implicitly_wait(5)
days = driver.find_elements(By.XPATH,"//android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/child::android.view.View")


matchedDay = "27"
matchedDay_2 = "30"

for day in days:
  # attr = day.get_property("text")
  # print(attr)
  attr = day.get_attribute("contentDescription")
  # print(attr)
  if attr == None: continue
  for i in attr:
     if (i == '2'):
        tempStr = ""
        for j in attr:
           if j != ',': tempStr += j
           else: break
        print(tempStr)
        if (tempStr == matchedDay): day.click();break 
        # print(attr)
        break

okButton = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='OK']")
okButton.click()
hoursMinutes = driver.find_element(By.XPATH,"(//android.view.View[@content-desc='Day'])[1]")
hoursMinutes.click()
driver.implicitly_wait(3)
keyboard = driver.find_element(By.XPATH,"//android.view.View[@content-desc='SELECT TIME']/android.widget.Button[1]")
keyboard.click()
driver.implicitly_wait(5)
hour = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")

hour.click()
hour.clear()
hour.send_keys("3")

minute = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")

minute.click()
minute.clear()
minute.send_keys("3")

okButton = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='OK']")
okButton.click()

##############   Repeat again ##########################
########################################################
########################################################
dayButton = driver.find_element(By.XPATH,"(//android.view.View[@content-desc='Day'])[1]")
dayButton.click()
##  parse date and remove the first two commas ######
driver.implicitly_wait(5)
days = driver.find_elements(By.XPATH,"//android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/child::android.view.View")

for day in days:
  # attr = day.get_property("text")
  # print(attr)
  attr = day.get_attribute("contentDescription")
  # print(attr)
  if attr == None: continue
  for i in attr:
     if (i == '2'):
        tempStr = ""
        for j in attr:
           if j != ',': tempStr += j
           else: break
        print(tempStr)
        if (tempStr == matchedDay_2): day.click();break 
        # print(attr)
        break





# for hour in hours:
#     attr = day.get_attribute("contentDescription")
#     print(attr)
#     if attr == None: continue
#     for i in attr:
#       if (i == '2'):
#           tempStr = ""
#           for j in attr:
#             if j != ',': tempStr += j
#             else: break
#           if (tempStr == matchedDay): day.click();break 
#           print(attr)
#           break

# dayButton.send_keys("23")

# logOut = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Log out']")
# logOut.click()



input()
driver.quit()