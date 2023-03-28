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
websiteURL = "https://www.eventbrite.co.uk/manage/events/601564283967/details"
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
    events = driver.find_element(By.CLASS_NAME,"event-breadcrumb__label")
    events.click()
    isPresentError = waitUntil(EC.presence_of_element_located((By.XPATH,"//*[@id='orders-nav']/a/div")))
    print(isPresentError)
    # Drafts
    driver.implicitly_wait(3)
    toDraft = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[2]/div/div[2]/div/div/div/a/div")
    toDraft.click()
    toDraft2 = driver.find_element(By.XPATH,"//*[@id='draft']/div/button")
    toDraft2.click()
    ####################
    ellipsisVar = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[3]/div[2]/ul/li[1]/div/div/div[2]/div/div/span/button")
    ellipsisVar.click()
    driver.implicitly_wait(2)
    delete = driver.find_element(By.XPATH,"//*[@id='delete']/div/button")
    delete.click()

    driver.switch_to.alert.accept()

except Exception as E:
    print(E)
    print(E.__class__.__name__)
finally:
    input()