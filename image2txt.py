import pyautogui
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import numpy as np

# Capture the screenshot
screenshot = pyautogui.screenshot()

# Convert the screenshot to a numpy array and pass it to Tesseract
text = pytesseract.image_to_string(np.array(screenshot), lang='eng')
import pyperclip
pyperclip.copy(text)  # send text to clipboard
print(text)

# Write the text to a file
# with open('D:\kevin\output.txt', 'w') as f:
#    f.write(text)
