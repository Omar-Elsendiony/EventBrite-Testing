from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (TimeoutException,NoSuchElementException,ElementNotVisibleException)
import logging
opts = webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")
websiteURL = "https://www.eventbrite.co.uk/signin/signup"
serv_obj = Service("O:\DriveFiles\Drivers\chromedriver_win32 (1)\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=opts)
driver.get(websiteURL)
driver.maximize_window()
logging.basicConfig(filename="test.log",format="%(message)s",level=logging.DEBUG)

def waitUntil(expectedCondition):
    error = False
    try:
        WebDriverWait(driver, 10,poll_frequency=1 ,  ignored_exceptions=[TimeoutException]).until(expectedCondition)
        error = True
    except:
        pass
    return error

def Assert(parameter,value,message):
    logging.error(message)
    try:
        assert parameter == value
    except AssertionError:
        print(message)

try:
    previousURL = driver.current_url
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//body")))
    emailTextBox = driver.find_element(By.NAME,"email")
    # invalid account format test
    emailTextBox.send_keys("gsgs.hhs")
    continueButton = driver.find_element(By.XPATH,"//button[contains(text(),'Continue')]")
    continueButton.click()
    emailTextBoxTitle = emailTextBox.get_attribute("title")
    print(emailTextBoxTitle)
    isLoggedIn = waitUntil(EC.staleness_of(continueButton))
    errorMessage = "Trying signing up with an invalid account format"
    Assert(isLoggedIn,False,errorMessage)
    # check entering account is already signed up
    emailTextBox.clear()
    emailTextBox.send_keys("omar.elsendiony@hotmail.com")
    continueButton.click()
    isSignedUp = driver.find_element(By.XPATH,"//div/strong[contains(text(),'There is an account associated with the email')]")
    errorMessage = "Trying Signing up with an already signed up account"
    Assert(isSignedUp,True,errorMessage)
    # sign in Email address doesn't match. Please try again
    emailTextBox.clear()
    emailTextBox.send_keys("mama.mama@hotmail.com")
    confirmEmailTextBox = driver.find_element(By.NAME,'emailConfirmation')
    confirmEmailTextBox.send_keys("mama.mona@hotmail.com")
    #EC.presence_of_element_located((By.XPATH,'//*[@id="twotabsearchtextbox"]'))
    confirmEmailError = driver.find_element(By.XPATH,"//div/aside[contains(text(),'Email address doesn't match. Please try again')]")
    firstName = driver.find_element(By.NAME,"firstName")
    lastName = driver.find_element(By.NAME,"lastName")
    password = driver.find_element(By.NAME,"password")
    firstName.send_keys("mama")
    lastName.send_keys("mona")
    password.send_keys("gwgrgrewgw")
    createAccount = driver.find_element(By.XPATH,"//button[contains(text(),'Create account')]")
    createAccount.click()
    isError  = waitUntil(EC.presence_of_element_located((By.XPATH,"//div/aside[contains(text(),'Email address doesn't match. Please try again')]")))
    errorMessage = "Email address does not match but Created Account"

    Assert(isError,False,)
except Exception as E:
    print(E)
    print(E.__class__.__name__)
finally:
    input()