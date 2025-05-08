# Automated Message Sender via GUI

This script automates the process of sending personalized messages (e.g., invitations or notifications) to a list of phone numbers using GUI automation. It utilizes `pyautogui` for mouse and keyboard interactions and `pyperclip` for clipboard handling.

## 📌 Features

- Reads phone numbers from a CSV file (`btech.csv`)
- Automatically pastes phone number and message into a GUI (e.g., WhatsApp Web or other platform)
- Sends a pre-defined engagement program invitation
- Adds a delay before and between message sends for stability

## 🛠️ Requirements

Python 3.6 or above

Install dependencies with:

```bash
pip install -r requirements.txt
```

**`requirements.txt` should contain:**
```
pandas
pyautogui
pyperclip
```

## 📄 Usage

1. Ensure your system resolution matches the coordinate clicks in the script (e.g., `pyautogui.click(404, 150)`). Adjust as needed.
2. Prepare a CSV file named `btech.csv` with a column named `phone_no` containing the phone numbers.
3. Open the GUI platform (e.g., WhatsApp Web) where the message will be sent.
4. Run the script:

```bash
python send_message.py
```

5. The script will start after a 10-second delay to give you time to switch to the intended GUI.

## 📝 Message Template

The message includes:
- Invitation details for an online engagement program
- Microsoft Teams link
- Department website and class schedule
- Contact information for the organizing faculty member

## ⚠️ Disclaimer

- This script relies on hard-coded screen coordinates and is OS- and resolution-dependent.
- Use responsibly. Avoid spamming or violating platform terms of service.
