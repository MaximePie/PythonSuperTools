import pyautogui
import pytesseract # OCR

def getText(region):
    screenshot = pyautogui.screenshot(region=region)
    text = pytesseract.image_to_string(screenshot)
    return text

def getCoordinates():
    input("Press enter to take the first point")
    x1, y1 = pyautogui.position()

    input("Press enter to take the second point")
    x2, y2 = pyautogui.position()
    coordinates = (x1, y1, x2 - x1, y2 - y1)
    return coordinates


while True:
    coordinates = getCoordinates()
    text = getText(coordinates)
    print(f"\033[92m{text}\033[0m")
    
    # Continue ? Y/n
    answer = input("Continue ? Y/N")
    if answer.lower() == "n":
        break