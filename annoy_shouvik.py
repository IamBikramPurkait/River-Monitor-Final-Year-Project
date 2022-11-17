import pyautogui
import time

time.sleep(5)

text = 'kire bhai code patha'

for i in range(100):
    pyautogui.typewrite(text)

    time.sleep(2)
    pyautogui.press('enter')
