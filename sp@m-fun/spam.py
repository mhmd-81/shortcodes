import pyautogui as py
import time
message = "fuck  you"
time.sleep(2)
for i in range(20):
    py.typewrite(message+" " )
    py.press('Enter')
   