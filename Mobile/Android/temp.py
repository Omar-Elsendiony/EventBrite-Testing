homeTab.click()









## add to liked list ######
driver.implicitly_wait(2)
likes = driver.find_elements(By.XPATH,"//android.view.View[@content-desc='Tech']/android.widget.Button[3]")
like = likes[0]
b = like.get_attribute('bounds')
print(type(b))
b =list(b)

listOfCoordinates = list()
i  =0
while i < len(b)-1:
    if (b[i] == '['): i+= 1 ;continue
    tempBuff =""
    while not (b[i] == ',' or b[i] == ']'):
        tempBuff  += b[i]
        i += 1
    i += 1
    listOfCoordinates.append(int(tempBuff))

print(listOfCoordinates)
xC = (listOfCoordinates[0] + listOfCoordinates[1]) /2
yC = (listOfCoordinates[2] + listOfCoordinates[3]) /2

print(xC)
print(yC)


driver.implicitly_wait(5)
##   Clicking on the favorites
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(470, 2194)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
###############