
from time import sleep
import keyboard
import pyautogui
import pytesseract

# Using pytesseract to detect text
def getTextFromZone(zone):
    screenshot = pyautogui.screenshot(region=zone)
    text = pytesseract.image_to_string(screenshot)
    return text

while True:
    if (keyboard.is_pressed('x')):
        print('Coordinates: ' + str(pyautogui.position()))
        sleep(0.1)

    if keyboard.is_pressed('q'):
        break

    if keyboard.is_pressed('a'):
        print("Press CTRL on the top-left corner of the region to capture")
        while not keyboard.is_pressed('ctrl'):
            x1, y1 = pyautogui.position()
            sleep(0.1)

        print("Press alt on the bottom-right corner of the region to capture")
        while not keyboard.is_pressed('alt'):
            x2, y2 = pyautogui.position()
            sleep(0.1)

        textZone = (x1, y1, x2 - x1, y2 - y1)
        print(f"\033[92m{getTextFromZone(textZone)}\033[0m")
        sleep(0.1)