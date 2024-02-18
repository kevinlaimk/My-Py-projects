import pyautogui
import time
import win32gui
import win32con
# need to pip install pywin32

def send_keystrokes(window_title, keystrokes):
    window_handle = win32gui.Findwindow(None, window_title)

win32gui.SetForegroundWindow(window_handle)

#wait for the window to become the active window while win32gui.getforegroundwindow() !=window_handle:
time.sleep(0.1)
pyautogui.typewrite(keystrokes)

window_title="Excel"
keystrokes="Hello World!"

send_keystrokes(window_title,keystrokes)
