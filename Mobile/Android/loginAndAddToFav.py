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





########Change profile name ################
# driver.implicitly_wait(13)
WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, "//android.view.View/android.view.View/android.view.View/android.view.View/child::android.widget.Button[1]")))


editProfile = driver.find_element(AppiumBy.XPATH,"//android.view.View/android.view.View/android.view.View/android.view.View/child::android.widget.Button[1]")

myFirstName = "Black"
mySecondName = "Cat"
###   Edit name #########
editProfile.click()
nameProfile = driver.find_element(By.XPATH,"//android.view.View[@content-desc='Name']/android.widget.Button")
nameProfile.click()
# driver.push_file()
# Edit text
driver.implicitly_wait(2)
editTexts = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.EditText")
first = editTexts[0]
last = editTexts[1]

first.click()
driver.implicitly_wait(1)
first.clear()
first.send_keys(myFirstName)

driver.hide_keyboard()
last.click()
last.clear()
last.send_keys(mySecondName)

driver.implicitly_wait(1)
saveChanges = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Save Changes']")
saveChanges.click()
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
time.sleep(3)
manageEvents = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Manage Events")
manageEvents.click()
## plus button ##

WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button")))

plusButton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button")
plusButton.click()
WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText")))

myEvent = "Anime lovers"
mySummary = "Do not watch anime!"
eventTitle = driver.find_element(By.XPATH,"//android.widget.EditText")
eventTitle.send_keys(myEvent)

nextButton = driver.find_element(By.XPATH,"//android.widget.Button")
nextButton.click()


summary = driver.find_element(By.XPATH,"//android.widget.EditText")
summary.send_keys(mySummary)
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
  attr = day.get_attribute("contentDescription")
  if attr == None: continue
  for i in attr:
     if (i == '2'):
        tempStr = ""
        for j in attr:
           if j != ',': tempStr += j
           else: break
        if (tempStr == matchedDay_2): day.click();break 
        # print(attr)
        break
okButton = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='OK']")
okButton.click()
########  NOW HOURS #################
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

nextButton = driver.find_element(By.XPATH,"//android.widget.Button")
nextButton.click()

location = driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText")
location.click()
location.send_keys("Cairo, Egypt")
# input()
driver.implicitly_wait(7)
listLocations = driver.find_elements(AppiumBy.XPATH,"//android.widget.Button/android.view.View")
for l in listLocations:
  attr = l.get_attribute("contentDescription")
  if attr == None: continue
  if attr == "Cairo, Egypt": l.click();break
  print(attr)


# select = Select(driver.find_element(By.XPATH,"//android.widget.EditText"))
# select.select_by_visible_text('Cairo, Egypt')
# driver.hide_keyboard()
driver.implicitly_wait(3)
# nextButton = driver.find_element(By.XPATH,"//android.widget.Button")
# nextButton.click()


#########  Event Image ################
# driver.implicitly_wait(3)
# uploadPicture = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")
# uploadPicture.click()
# photoOptions = driver.find_elements(By.ID,"com.google.android.documentsui:id/icon_thumb")
# # photoOptions[0].click()

# ##   Clicking on the photo
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to(photoOptions[2])
# actions.w3c_actions.pointer_action.click_and_hold()
# actions.w3c_actions.pointer_action.pause(0.5)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
# select = driver.find_element(AppiumBy.ID,"com.google.android.documentsui:id/action_menu_select")
# select.click()
# ############################################################

# driver.implicitly_wait(10)
time.sleep(3)


addTickets = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[10]")

addTickets.click()
driver.implicitly_wait(5)

add = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button")
add.click()

texts = driver.find_elements(By.XPATH,"//android.widget.EditText")
ticketName = texts[0]
ticketName.send_keys("For those who love sorra")

q = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]")
q.click()
q.send_keys("11")
driver.hide_keyboard()
price = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]")
price.click()
price.send_keys("10")
driver.hide_keyboard()

EOS = driver.find_element(AppiumBy.XPATH,"//android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/child::android.view.View[3]")

EOS.click()


#########################################################################################
driver.implicitly_wait(5)
days = driver.find_elements(By.XPATH,"//android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/child::android.view.View")

for day in days:
  attr = day.get_attribute("contentDescription")
  if attr == None: continue
  for i in attr:
     if (i == '2'):
        tempStr = ""
        for j in attr:
           if j != ',': tempStr += j
           else: break
        if (tempStr == matchedDay_2): day.click();break 
        # print(attr)
        break

okButton = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='OK']")
okButton.click()


BOS = driver.find_element(AppiumBy.XPATH,"//android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/child::android.view.View[1]")

BOS.click()


#########################################################################################
driver.implicitly_wait(5)
days = driver.find_elements(By.XPATH,"//android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/child::android.view.View")

for day in days:
  attr = day.get_attribute("contentDescription")
  if attr == None: continue
  for i in attr:
     if (i == '2'):
        tempStr = ""
        for j in attr:
           if j != ',': tempStr += j
           else: break
        if (tempStr == matchedDay): day.click();break 
        # print(attr)
        break

okButton = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='OK']")
okButton.click()

driver.implicitly_wait(3)

done = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]")

done.click()

successfullyAdded = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='OK']")
successfullyAdded.click()
driver.implicitly_wait(3)
backBtn = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button")
backBtn.click()

WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, "//android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/child::android.view.View[8]")))

eventCategory =driver.find_element(AppiumBy.XPATH,"//android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/child::android.view.View[8]")

eventCategory.click()
time.sleep(2)
categories = driver.find_elements(By.XPATH,"//android.view.View/android.widget.Button")
categories[4].click()

driver.implicitly_wait(3)



#########  Event Image ################
driver.implicitly_wait(3)
uploadPicture = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")
uploadPicture.click()
photoOptions = driver.find_elements(By.ID,"com.google.android.documentsui:id/icon_thumb")
# photoOptions[0].click()

##   Clicking on the photo
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to(photoOptions[0])
actions.w3c_actions.pointer_action.click_and_hold()
actions.w3c_actions.pointer_action.pause(0.5)
actions.w3c_actions.pointer_action.release()
actions.perform()
select = driver.find_element(AppiumBy.ID,"com.google.android.documentsui:id/action_menu_select")
select.click()
############################################################

driver.implicitly_wait(10)
time.sleep(3)


createEvent = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[3]")
createEvent.click()
time.sleep(1)
okBtn = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='OK']")
okBtn.click()
# logOut = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Log out']")
# logOut.click()
input()
driver.quit()