import pyautogui as py
import time
message = "YOU R cute  like a cat :)  "
time.sleep(2)
for i in range(100):
    py.typewrite(message+" " )
    py.press('Enter')
   