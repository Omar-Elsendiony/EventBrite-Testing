from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import funcs
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (TimeoutException,NoSuchElementException,ElementNotVisibleException)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
def waitUntil(expectedCondition,optionalExpectedCondition=None):
    error1 = False
    error2 = False
    try:
        WebDriverWait(driver, 5,poll_frequency=1 ,  ignored_exceptions=[TimeoutException]).until(expectedCondition)
        print(1)
    except:
        error1 = True
        print(2)
    if (optionalExpectedCondition != None):
        try:          
            WebDriverWait(driver, 3,poll_frequency=1 ,  ignored_exceptions=[TimeoutException]).until(optionalExpectedCondition)
            print(1)
        except Exception as E:
            error2 = True
            print(2)
    return (error1)
          

driver.get("https://www.eventbrite.com/signin")
action = ActionChains(driver)
time.sleep(1)
login= funcs.ClickFnHttp("//div[@data-testid='consumer-header-links-test']//span[contains(text(),'Log In')]",1)
driver.maximize_window()
EmailField = funcs.SendKeysFnHttp(driver, "//input[@id='email']", "mt.hotmail@g.com", 1)  # Writes the email in the email field
PasswordField = funcs.SendKeysFnHttp(driver, "//input[@id='password']","mortmortvol", 1)  # Writes the password in the password field
time.sleep(1)
LoginButton = funcs.ClickFnHttp(driver, "//button[@type='submit']", 1)
time.sleep(1)
noNotification = waitUntil(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/div/div/div/div/div/div[2]/span/button")))
if(not noNotification):
    print("Note")
    element = driver.find_element(By.XPATH,"//*[contains(text(),'Skip')]")
    driver.implicitly_wait(1)
    action.move_to_element(element).click().perform()

free=funcs.ClickFnHttp(driver, "//span[normalize-space()='Free']", 1)

online=funcs.ClickFnHttp(driver, "//input[@id='locationPicker']", 1)
try:
    # time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Browse online events')]")))
    driver.execute_script("window.scrollBy(0,1000)","")
    online2=funcs.ClickFnHttp(driver, "//div[contains(text(),'Browse online events')]", 1)
    # event=funcs.ClickFnHttp(driver, "//div[@role='presentation'][contains(text(),'We The Medicine -')]", 1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div/div[contains(text(),'We The Medicine -')]")))
    event = driver.find_element(By.XPATH,"//div[@role='presentation' and contains(text(),'Guided Medi')]")
    eventClick = driver.find_element(By.XPATH,"//div/div[contains(text(),'We The Medicine -')]")
    driver.execute_script("arguments[0].scrollIntoView();",event)
    original_window = driver.current_window_handle
    # driver.execute_script("window.scrollBy(0,500)","")
    driver.implicitly_wait(2)
    action.move_to_element(event).click().perform()
    # event.click()
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    driver.execute_script("window.scrollBy(0,1000)","")
    followElement = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div[2]/div[2]/div[1]/section/div[2]/button")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'gister')]")))
    # cl=funcs.ClickFnHttp(driver, "//*[@id='eventbrite-widget-modal-trigger-385150915757']", 1)
    register = driver.find_element(By.XPATH,"//button[contains(text(),'gister')]")
    register.click()

    time.sleep(100)
except Exception as E:
    print(E)
    print(E.__class__.__name__)

input()
