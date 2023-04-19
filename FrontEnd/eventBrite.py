from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (TimeoutException, NoSuchElementException, ElementNotVisibleException)

# import logging
######################################################################
opts = webdriver.ChromeOptions()
opts.add_argument("--disable-notifications")
proxy = "121.240.187.80:31"
desiredC = {
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy,
    "noProxy": None,
    "proxyType": "MANUAL",
    "class": "org.openqa.selenium.Proxy",
    "autodetect": False
}
websiteURL = "https://www.eventbrite.co.uk/signin/signup"
serv_obj = Service("O:\DriveFiles\Drivers\chromedriver_win32 (1)\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj, options=opts, desired_capabilities=desiredC)
driver.get(websiteURL)
driver.maximize_window()
# logging.basicConfig(filename="test.log",format="%(message)s",level=logging.DEBUG)
action = ActionChains(driver)


######################################################################
def waitUntil(expectedCondition, optionalExpectedCondition=None):
    error1 = False
    error2 = False
    try:
        WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=[TimeoutException]).until(expectedCondition)
    except:
        error1 = True
    if (optionalExpectedCondition != None):
        try:
            WebDriverWait(driver, 3, poll_frequency=1, ignored_exceptions=[TimeoutException]).until(
                optionalExpectedCondition)
            print(driver.current_url)
            print("URl1")
        except Exception as E:
            error2 = True
            print(E)
            print(E.__class__.__name__)
            print("Url2")
    print(error1, error2)
    return (error1 or error2)

def Assert(parameter, value, message):
    try:
        assert parameter == value
    except AssertionError:
        print(message)
        # logging.error(message)

try:
    previousURL = driver.current_url
    ##########################################################
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))
    emailTextBox = driver.find_element(By.NAME, "email")
    continueButton = driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
    #######################################################
    # invalid account format test
    #########################################################
    emailTextBox.send_keys("gsgs.hhs")
    emailTextBox.clear()

    continueButton.click()
    emailTextBoxTitle = emailTextBox.get_attribute("title")
    print(emailTextBoxTitle)
    isLoggedIn = waitUntil(EC.staleness_of(continueButton))
    errorMessage = "Trying signing up with an invalid account format"
    Assert(isLoggedIn,False,errorMessage)
    ####################################################
    # check entering account is already signed up
    ##################################################
    # editAddress = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/form/div[1]/div[1]/div/div/div/span/span/button")
    # emailTextBox.click()
    driver.implicitly_wait(4)
    ######## Clearing the text Box By another way as the conventional .clear() method does not work
    emailTextBox.send_keys(Keys.CONTROL, 'a')
    emailTextBox.send_keys(Keys.BACKSPACE)
    #######################################
    emailTextBox.clear()
    # emailTextBox.set
    # editAddress.click()
    emailTextBox.send_keys("omar.elsendiony@hotmail.com")
    continueButton.click()
    isSignedUp = driver.find_element(By.XPATH,"//div/strong[contains(text(),'There is an account associated with the email')]")
    errorMessage = "Trying Signing up with an already signed up account"
    Assert(isSignedUp,True,errorMessage)
    # ###############################################################
    # # sign in Email address doesn't match. Please try again
    # ##########################################################
    emailTextBox.send_keys(Keys.CONTROL, 'a')
    emailTextBox.send_keys(Keys.BACKSPACE)
    originalEmail = "remonda.tALAAT@hotmail.com"
    unmatchedEmail = "mama.mona@hotmail.com"
    emailTextBox.send_keys(originalEmail)
    continueButton.click()
    driver.implicitly_wait(2)
    confirmEmailTextBox = driver.find_element(By.NAME, 'emailConfirmation')
    confirmEmailTextBox.send_keys(unmatchedEmail)
    # EC.presence_of_element_located((By.XPATH,'//*[@id="twotabsearchtextbox"]'))
    # confirmEmailError = driver.find_element(By.XPATH,"//div/aside[contains(text(),'Email address doesn't match. Please try again')]")
    firstName = driver.find_element(By.NAME, "firstName")
    lastName = driver.find_element(By.NAME, "lastName")
    password = driver.find_element(By.NAME, "password")
    firstName.send_keys("mama")
    lastName.send_keys("mme")
    password.send_keys("gwgrgrewgw")
    createAccount = driver.find_element(By.XPATH, "//button[contains(text(),'Create account')]")
    createAccount.click()
    isError = waitUntil(EC.url_matches(previousURL))  # if it is still on the same webpage
    errorMessage = "Email address does not match but Created Account"
    Assert(isError, False, errorMessage)
    ##########################################
    ###### Sign Up Noooooooooow
    #########################################
    confirmEmailTextBox.send_keys(Keys.CONTROL, 'a')
    confirmEmailTextBox.send_keys(Keys.BACKSPACE)
    confirmEmailTextBox.send_keys(originalEmail)
    createAccount.click()
    agreeCondition = driver.find_element(By.XPATH,"//*[@id='edsModalContentChildren']/div/div/div/div[2]/button[2]")
    agreeCondition.click()
except Exception as E:
    print(E)
    print(E.__class__.__name__)
finally:
    input()
