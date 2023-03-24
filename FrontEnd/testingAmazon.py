from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service("O:\DriveFiles\Drivers\chromedriver_win32\chromedriver.exe"))
driver.get("https://amazon.com")
action = ActionChains(driver)
# driver.back()
driver.maximize_window()
# driver.implicitly_wait(10)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="twotabsearchtextbox"]')))

videoGames = driver.find_elements(By.CLASS_NAME,'navFooterBackToTopText')
# allCategories = driver.find_element(By.CSS_SELECTOR,'a[data-csa-c-interaction-events="click"]')
# allCategories.click()
# ElectronicsButton = driver.find_element(By.XPATH,"//a[@data-menu-id='5']").click()
dismiss = driver.find_element(By.CLASS_NAME,"a-button-text")
print(dismiss.text)
action.move_to_element(dismiss).click().perform()
computersAndAccessories = driver.find_element(By.LINK_TEXT,"Gift Cards")
driver.implicitly_wait(1)

action.move_to_element(computersAndAccessories).click().perform()

print(videoGames)
# print(elements)

input()



