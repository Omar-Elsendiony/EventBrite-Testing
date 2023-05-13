import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (TimeoutException,NoSuchElementException,ElementNotVisibleException)
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.se
# import logging
######################################################################
opts = webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")

websiteURL = "https://www.eventbrite.co.uk/signin"
serv_obj = Service("O:\DriveFiles\Drivers\chromedriver_win32 (1)\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj,options=opts)
driver.get(websiteURL)
driver.maximize_window()
# logging.basicConfig(filename="test.log",format="%(message)s",level=logging.DEBUG)
action = ActionChains(driver)

def waitUntil(expectedCondition,optionalExpectedCondition=None):
    error1 = False
    error2 = False
    try:
        WebDriverWait(driver, 5,poll_frequency=1 ,  ignored_exceptions=[TimeoutException]).until(expectedCondition)
    except:
        error1 = True
    if (optionalExpectedCondition != None):
        try:
            WebDriverWait(driver, 3,poll_frequency=1 ,  ignored_exceptions=[TimeoutException]).until(optionalExpectedCondition)
        except Exception as E:
            error2 = True
    return (error1 or error2)

def Assert(parameter,value,message):

    try:
        assert parameter == value
    except AssertionError:
        print(message)
        # logging.error(message)
###########################################################
try:
    previousURL = driver.current_url
    ##########################################################
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))
    email = driver.find_element(By.NAME,"email")
    password = driver.find_element(By.NAME,"password")
    LogIn = driver.find_element(By.XPATH,"//div/button[@data-automation='signin-submit-button']")
    email.send_keys("mt.hotmail@g.com")
    password.send_keys("mortmortvol")
    driver.implicitly_wait(2)
    ActionChains(driver).double_click(LogIn).click().perform()
    action.move_to_element(LogIn).double_click(LogIn).click().perform()
    LogIn.click()
    # LogIn.click()
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))
    errorInChangingURL = waitUntil(EC.url_changes(previousURL))
    message = "Not Logged In"
    Assert(errorInChangingURL,False,message)
    ###### Notification appearing randomly
    main_page = driver.current_window_handle
    noNotification = waitUntil(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/div[2]/div/div/div/div/div[2]/span/button")))
    while (not noNotification):
        element = driver.find_element(By.XPATH,"//*[@id='edsModalContentChildren']/div/div[2]/button[2]")
        # ActionChains(driver).double_click(driver.find_element(driver.find_element(By.CLASS_NAME,"Button_primary__1p1bh"))).perform()
        driver.execute_script("arguments[0].click();", element)
        noNotification = waitUntil(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/div[2]/div/div/div/div/div[2]/span/button")))
        print(noNotification)
    
    createEvent = driver.find_element(By.XPATH,"//*[@id='global-header']/div/div[1]/div[2]/a/i")
    createEvent.click()
    # driver.switch_to.active_element()
    ###################################################################
    WebDriverWait(driver, 10).until(EC.url_changes("https://www.eventbrite.co.uk/manage/events/create"))
    driver.implicitly_wait(3)
    eventInfo = "Go to the jungle"
    organizer = "Abbas Bin Farnas"
    eventBasicInfo = driver.find_element(By.ID,"event-basicInfo-title")
    eventBasicInfo.send_keys(eventInfo)
    organizerName = driver.find_element(By.NAME,"organizerProfile")
    organizerName.send_keys(organizer)
    select = Select(driver.find_element(By.ID,"eventType"))
    select.select_by_visible_text('Attraction')
    #############################################
    eventCategory = driver.find_element(By.ID,"eventSubTopic")
    # select = Select(webelement=)
    # select.select_by_visible_text(text=)
    #############################################
    eventSubCategory = driver.find_element(By.ID,"subTopic")
    select = Select(driver.find_element(By.ID,"subTopic"))
    select.select_by_visible_text('Christmas')
    #####################################################
    addTag = driver.find_element(By.XPATH,"//button[contains(text(),'Add')]")
    tagsNeeded = ["music","rock","Science","drama","schoolholidays","scrum","drawing","poetry","popup","politics"]
    tags = driver.find_element(By.ID,"tagging-form-field")
    action.scroll_to_element(addTag).perform()
    driver.execute_script("arguments[0].scrollIntoView();",addTag)
    for tag in tagsNeeded:
        tags.send_keys(tag)
        addTag.click()

    onlineEvents = driver.find_element(By.NAME,"venueType")
    onlineEvents = driver.find_element(By.XPATH,"//label[contains(text(),'Online')]")

    driver.execute_script("arguments[0].scrollIntoView();",onlineEvents)
    onlineEvents.click()


    vtz = driver.find_element(By.NAME,"venueTimeZone") #venue time zone
    driver.execute_script("arguments[0].scrollIntoView();",vtz)
    #################################################################
    select = Select(driver.find_element(By.NAME,"venueTimeZone"))
    select.select_by_visible_text('(GMT+0200) Egypt Time')
    #################################################################
    select = Select(driver.find_element(By.NAME,"locale"))
    select.select_by_visible_text('English (Canada)')
    #################################################################
    month = "JULY"
    year = "2023"
    wDay = "13"
    startDate = driver.find_element(By.NAME,"event-startDate")
    endDate = driver.find_element(By.NAME,"event-endDate")
    # startDate.click()
    endDate.click()
    driver.implicitly_wait(1)
    # myMonth = driver.find_element(By.CSS_SELECTOR,'div.CalendarMonth_caption.CalendarMonth_caption_1 strong')
    monthYear = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[3]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/strong")
    #//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[3]/div[2]/div[3]/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/strong
    # monthYear = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[3]/div[2]/div[3]/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/strong")
    movForward = driver.find_element(By.XPATH,"//button[@aria-label='Move forward to switch to the next month.']")

    monthYearSplit = monthYear.text.split()
    currentMonth = str(monthYearSplit[0])
    currentYear = str(monthYearSplit[1])
    print(currentMonth)
    print(currentYear)
    while (currentYear != year):
        movForward.click()
        driver.implicitly_wait(2)
        monthYear = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[3]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/strong")
        print(monthYear.text)
        monthYearSplit = monthYear.text.split()
        print(monthYear.text)
        currentMonth = str(monthYearSplit[0])
        currentYear = str(monthYearSplit[1])
    while(currentMonth != month):
        movForward.click()
        driver.implicitly_wait(2)
        monthYear = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[3]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/strong")
        # print(monthYear.text)
        monthYearSplit = monthYear.text.split()
        # print(monthYear.text)
        currentMonth = str(monthYearSplit[0])
        currentYear = str(monthYearSplit[1])

    days = driver.find_elements(By.CSS_SELECTOR,".CalendarDay")
    print(days)
    for day in days:
        # print(day.text)
        if (day.text == wDay):
            day.click()
            break




    # eventType = driver.find_element(By.ID,"eventType")

    # //*[@id="root"]/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[3]
    # saveAndContinue = 
    # saveAndContinue.click()
    driver.implicitly_wait(4)
    # ActionChains(driver).double_click(driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div[2]/form/div[3]")).perform()
    # driver.execute_script("arguments[0].scrollIntoView();",onlineEvents)

    ActionChains(driver).double_click(driver.find_element(By.XPATH,"//button[contains(text(),'Save')]")).perform()
     # //*[@id="edsModalContentChildren"]/div/div[2]/button[2]


except Exception as E:
    print(E)
    print(E.__class__.__name__)
finally:
    input()

