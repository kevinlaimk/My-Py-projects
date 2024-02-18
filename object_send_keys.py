import pygetwindow as gw
import pyautogui
import time

windows = gw.getAllWindows()
for window in windows:
      print(window.title)

window=gw.getWindowsWithTitle('Excel')[0]
window.activate()

time.sleep(1)

pyautogui.typewrite('Hello world')
#window.moveTo(100,100)
#window.close()
