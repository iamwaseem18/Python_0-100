from openai import OpenAI

#Pip install Openai
#if you saved the key under a different environment variable name, you can do something like:

client = OpenAI(api_key='Enter Your API Key')


command =''' [3:14 PM, 4/26/2025] Waseem: Konsey?
[3:14 PM, 4/26/2025] Waseem: Photos?
[3:14 PM, 4/26/2025] Qudsia: Aur banake peerey so bhi
[3:14 PM, 4/26/2025] Waseem: 😂😂😂😂
[3:14 PM, 4/26/2025] Qudsia: Fruits
[3:15 PM, 4/26/2025] Waseem: Ab kya bolun mai😂
[3:15 PM, 4/26/2025] Waseem: Daaltun
[3:15 PM, 4/26/2025] Qudsia: Okay
[3:15 PM, 4/26/2025] Qudsia: Allah hafiz
[3:15 PM, 4/26/2025] Waseem: Alhfzz
[9:20 PM, 4/26/2025] Waseem: Asalamulaikum'''

completion = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud"},
        {"role":"user","content": command }
    ]
)

print(completion.choices[0].message.content)

from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="Enter Your API Key",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named harry who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Harry"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)