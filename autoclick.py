

import keyboard
import pyautogui


def click():
    pyautogui.click()


while True:
    click()
    if keyboard.is_pressed('q'):
        break
print('Stopped')