import pyautogui

steam_path = "Windows.png"

steam = pyautogui.locateCenterOnScreen(steam_path, confidence = 0.69)
print(steam)