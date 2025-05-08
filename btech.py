import time
import pyautogui
import pandas as pd
import pyperclip


message = \
    "Subject: Invitation to Engagement Program B.Tech | MCA | M.Tech – Join Us Online!"\
    "\n"\
    "\n"\
    "Dear Student,"\
    "\n"\
    "\n"\
    "I hope this message finds you well!"\
    " We are pleased to invite you to our Engagement Program, scheduled for tomorrow at 4:00 PM."\
    " The session will be conducted via Microsoft Teams."\
    "\n"\
    "\n"\
    "We look forward to your enthusiastic participation in the program!"\
    "\n"\
    "\n"\
    "Details:"\
    "\n"\
    "Date & Time: 03:00PM TO 04:00OM (Every Wednesday Online Mode)"\
    "\n"\
    "Platform: Microsoft Teams"\
    "\n"\
    "Online Class Link: https://tinyurl.com/maw9tn5n"\
    "\n"\
    "Departmental Website: https://aucse.in/"\
    "\n"\
    "Online Class Schedule: https://www.aucse.in/more/engagement-session-2025"\
    "\n"\
    "\n"\
    "If you have any questions or need clarification, please feel free to contact Ms. Debasree Mitra (Assistant Professor), Department of CSE. Phone: +91-9051454255"\
    "\n"\
    "\n"\
    "Warm regards,"\
    "\n"\
    "Department of Computer Science and Engineering"\
    "\n"\
    "Adamas University"


data = pd.read_csv('bca.csv')
phone_numbers = data['phone_no'].tolist()

print("Starting in 10 seconds...")
time.sleep(10)

for phone in phone_numbers:
    pyautogui.click(404, 150)
    time.sleep(0.5)

    pyautogui.hotkey('command', 'a')
    pyautogui.hotkey('command', 'x')
    time.sleep(0.2)

    pyperclip.copy(str(phone))
    time.sleep(0.2)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.5)

    pyautogui.click(225, 343)
    time.sleep(0.5)

    pyautogui.hotkey('command', 'a')
    pyautogui.hotkey('command', 'x')
    time.sleep(0.2)

    pyperclip.copy(message)
    time.sleep(0.2)
    pyautogui.hotkey('command', 'v')
    time.sleep(0.5)

    pyautogui.click(1393, 863)
    time.sleep(1)

print("Done sending messages.")