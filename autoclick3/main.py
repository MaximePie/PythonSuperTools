# Autoclicker with upgrade detection feature
from time import sleep
import keyboard
import pyautogui
# import time
import numpy as np


cookieCoordinates = (125, 480)
upgradeZoneCoordinates = (522, 283, 729, 1007)

# Take a screenshot of the screen
# For each pixel, check if it is green
# If it is, return the coordinates
# Else, return None
def getGreenCoordinates():
    # start_time = time.time()
    screenshot = pyautogui.screenshot(region=upgradeZoneCoordinates)
    screenshot = np.array(screenshot)
    green = np.where((screenshot[:, :, 0] == 102) & (screenshot[:, :, 1] == 255) & (screenshot[:, :, 2] == 102))
    if green[0].size > 0:
        # end_time = time.time()
        # print(f"Execution time: {end_time - start_time} seconds")
        return (green[1][0] + upgradeZoneCoordinates[0], green[0][0] + upgradeZoneCoordinates[1])
    # end_time = time.time()
    # print(f"Execution time: {end_time - start_time} seconds")
    return None

# If an upgrade is available, click on it
# Else, click on the cookie
def click():
    greenCoordinates = getGreenCoordinates()
    if (greenCoordinates):
        pyautogui.click(greenCoordinates)
    else:
        pyautogui.click(cookieCoordinates)

canClick = False

while True:

    if (keyboard.is_pressed('x')):
        print('Coordinates: ' + str(pyautogui.position()))
        sleep(0.1)

    if keyboard.is_pressed('q'):
        break

    if keyboard.is_pressed('a'):
        canClick = not canClick
        print('Started, click is now ' + str(canClick))
        sleep(0.1)
    if (canClick):
        click()
print('Stopped')