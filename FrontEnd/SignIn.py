from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

import funcs



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.eventbrite.com/signin")
time.sleep(1)

F = open('E:/Selenuim/TestCases/EmailTestCases.txt', 'r')
Emails = [Email.rstrip('\n') for Email in F.readlines()] # Makes a list containing all email test cases
F.close()
F = open('E:/Selenuim/TestCases/PasswordTestCases.txt', 'r')
Passwords = [Password.rstrip('\n') for Password in F.readlines()]  # Makes a list containing all Password test cases
F.close()
counter = 0  # counts number of cases tested

for Email in Emails:
    for Password in Passwords:
        # Locates the email field, password field, and the login button
        for i in range(2):  # uses same email and password twice, but shows password in one of them
            counter += 1
            print("Test number: ", counter)
            print("Email: ", Email)
            print("Password: ", Password)
            print("")


            
            time.sleep(1)
            EmailField = funcs.SendKeysFnHttp(driver, "//input[@id='email']", Email, 1)  # Writes the email in the email field
            # time.sleep(1)
            PasswordField = funcs.SendKeysFnHttp(driver, "//input[@id='password']", Password, 1)  # Writes the password in the password field
            
            if (i%2 == 0):
                time.sleep(1) 
                ShowPassword = funcs.ClickFnHttp(driver, "//i[@class='eds-vector-image eds-icon--small eds-vector-image--block']//*[name()='svg']", 1)
                
            time.sleep(1)
            LoginButton = funcs.ClickFnHttp(driver, "//button[@type='submit']", 1)


            time.sleep(2)


            # Checks if the login was successful
            try:
                #check if it is sigin page
                driver.find_element_by_xpath("//input[@id='email']")
                print("Login failed")
                print("")
                time.sleep(1)
                driver.refresh()
                time.sleep(1)

            except:
                print("Login Successful")
                print("")
                time.sleep(1)
                MenuLabel = funcs.ClickFnHttp(driver, "//span[@class='consumer-header__menu-label']", 1)
                Logout = funcs.ClickFnHttp(driver, "//div[contains(text(),'Log out')]", 1)
                time.sleep(1)
                #driver.refresh()
                MenuLabel = funcs.ClickFnHttp(driver, "//span[@class='consumer-header__menu-label']", 1)
                Logout = funcs.ClickFnHttp(driver, "//div[contains(text(),'Log out')]", 1)
                
                time.sleep(1)
            time.sleep(1)

driver.quit()  # Closes the browser

