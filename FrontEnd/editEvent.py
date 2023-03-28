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
    # eventOrganization = driver.find_element(By.PARTIAL_LINK_TEXT,"/organizations/events")
    # ordersNav = driver.find_element(By.XPATH,"//*[@id='orders-nav']/a/div")
    # ordersNav.click()
    # driver.implicitly_wait(4)
    #
    # eventsNav = driver.find_element(By.XPATH,"//*[@id='events-nav']/a/div")
    # eventsNav.click()
    # #//*[@id="creator-nav-root"]/aside/div[2]/div[1]/a/div
    # creatorNav = driver.find_element(By.XPATH,"//*[@id='events-nav']/a/div")
    # creatorNav.click()
    # events = waitUntil(EC.url_matches("https://www.eventbrite.co.uk/organizations/events/draft"))
    # print(events)
    # driver.implicitly_wait(3)
    # creator navigation button
    toDraft = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/section/div/div[2]/div[2]/div/div[2]/div/div/div/a/div")
    toDraft.click()
    toDraft2 = driver.find_element(By.XPATH,"//*[@id='draft']/div/button")
    toDraft2.click()
    driver.execute_script("window.scrollBy(0,1000)","")
    events = waitUntil(EC.presence_of_element_located(driver.find_elements(By.CLASS_NAME,"eds-text-bm eds-text-color--ui-900")))
    # print(events)
    events = driver.find_elements(By.CSS_SELECTOR,".eds-text-bm.eds-text-color--ui-900")
    # print(events)
    for event in events:
        print(event.text)
        if (event.text == "Go to the jungle"):
            print("weeeeeeeeeeeeeeee")
            event.click()
            break
    #############################################################
    ###############Tickets before publishing #####################
    #############################################################
    tickets = driver.find_element(By.XPATH,"//*[@id='root-event-sidenav-standalone']/div/div/div/div/ul/li[4]/a")
    action.move_to_element(tickets).click(tickets).perform()
    waitUntil(EC.presence_of_element_located(driver.find_element(By.ID,"ticket-quantity")))
    waitUntil(EC.presence_of_element_located(driver.find_element(By.NAME,"cost")))
    driver.implicitly_wait(3)
    cost = driver.find_element(By.NAME,"cost")
    quantity = driver.find_element(By.ID,"ticket-quantity")
    quantity.send_keys("1")
    cost.send_keys("10000")
    element = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/section/div[2]/div/div/div[2]/div/div[2]/button")
    ActionChains(driver).move_to_element(element).double_click(element).perform()
    # //*[@id="root"]/div/div[1]/div/div/div/div/div/div/div/main/div[2]/div[2]/div/nav/div/button
    driver.implicitly_wait(2)
    element = driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div/div/div/div/div/div/div/main/div[2]/div[2]/div/nav/div/button")
    ActionChains(driver).move_to_element(element).double_click(element).perform()

    details = driver.find_element(By.XPATH,"//*[@id='root-event-sidenav-standalone']/div/div/div/div/ul/li[2]/a")
    ActionChains(driver).move_to_element(details).double_click(details).perform()
    # EC.element_to_be_clickable()
    # //*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div/form/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/button
    #//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div/form/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/button
    # driver
    imagePort = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div/div/div[1]/div/main/section/div/div/div/form/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/button")
    driver.implicitly_wait(5)
    imagePort.send_keys("C:/Users/moga/Downloads/OIP.jpg")
    # imagePort.send_keys("C:\Users\moga\Downloads\OIP.jpg")
    driver.execute_script("window.scrollBy(0,500)","")

    # uploader-dropzone-1
    imagePort = driver.find_element(By.ID,"uploader-dropzone-1")
    imagePort.send_keys("C:/Users/moga/Downloads/bear.jpg")
    save = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[3]/div/div/div/div[1]/div/div/main/div/div[2]/div/nav/div/button")
    save.click()

    summary = driver.find_element(By.NAME,"summary")
    summary.send_keys("bla bla bla bla bla bla")
    save = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/button[2]")
    save.click()
except Exception as E:
    print(E)
    print(E.__class__.__name__)
finally:
    input()

