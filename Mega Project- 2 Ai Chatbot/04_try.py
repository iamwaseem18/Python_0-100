#Alternative Method

import pyautogui
import pytesseract
from PIL import Image
import time
import pyperclip
from openai import OpenAI

# If you're on Windows, set the path:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update path if needed

client = OpenAI(
    api_key="Enter Your API Key",
)

def is_last_message_from_sender(chat_text, sender_name="Rohan Das"):
    # Analyze the OCR-ed text
    lines = chat_text.strip().splitlines()
    if lines:
        last_line = lines[-1]
        if sender_name in last_line:
            return True
    return False

def capture_chat_text():
    # Screenshot a specific region where chat appears
    x, y, width, height = 950, 200, 950, 700  # Example values; adjust for your screen!
    screenshot = pyautogui.screenshot(region=(722,253,821,614))
    text = pytesseract.image_to_string(screenshot)
    return text

time.sleep(3)  # time to get ready

while True:
    time.sleep(5)  # wait between checks
    chat_history = capture_chat_text()

    print("\n--- Chat History ---")
    print(chat_history)
    print("--- End of Chat ---")

    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Naruto, roast people in Hindi-English mixed funny way. Keep responses short and witty."},
                {"role": "system", "content": "Don't repeat timestamps like [21:02, 26/04/2024] Rohan Das:"},
                {"role": "user", "content": chat_history}
            ]
        )
        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Paste response into WhatsApp
        pyautogui.click(1808, 1328)  # Click on message box
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
