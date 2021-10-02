import keyboard
from ahk import AHK
import time

ahk = AHK()

ahk.mouse_position = (200, 0)
ahk.mouse_move(200, 1420, speed = 10)
ahk.click()
ahk.type("12345")
ahk.mouse_drag(80, 1420, speed = 10)

time.sleep(1)

keyboard.press_and_release("Ctrl+x")
time.sleep(1)
keyboard.press_and_release("Ctrl+v")