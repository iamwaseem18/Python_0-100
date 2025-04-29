import pyautogui
import time
import pyperclip
from openai import OpenAI
from pyautogui import FailSafeException


client = OpenAI(
  api_key="Enter Your API Key",
)

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
# Optional: add a short delay before starting so you can get ready
time.sleep(3)

# Step 1: Click the icon at (1325, 1056)
pyautogui.click(1325, 1056)
time.sleep(1)

while True:
    try:
        time.sleep(5)
        pyautogui.moveTo(972,202)
        pyautogui.dragTo(1537,871, duration=2.0, button='left')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        pyautogui.click(1452,866)

        chat_history = pyperclip.paste()
        print(chat_history)
        print(is_last_message_from_sender(chat_history))

        if is_last_message_from_sender(chat_history):
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a person named Naruto who speaks Hindi and English, a coder from India who roasts people in a funny way."},
                    {"role": "system", "content": "Do not start with the timestamp like [21:02, 12/6/2024] Rohan Das:"},
                    {"role": "user", "content": chat_history}
                ]
            )
            response = completion.choices[0].message.content
            pyperclip.copy(response)

            pyautogui.click(1808, 1328)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')

    except FailSafeException:
        print("Fail-safe triggered! Mouse moved to corner. Exiting script...")
        break