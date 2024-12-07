# This autoclick can click on a specific location on the screen
# Make sure you can quit your script before running it
from time import sleep
import keyboard
import pyautogui

# TODO - Toggle 

def click():
    pyautogui.click()

canClick = False

while True:

    if keyboard.is_pressed('q'):
        break

    # If I press 'a', start clicking
    if keyboard.is_pressed('a'):
        canClick = not canClick
        print('Started, click is now ' + str(canClick))
        sleep(0.1)

    # if a condition is met, click
    if (canClick):
        click()
print('Stopped')