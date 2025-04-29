from openai import OpenAI
client = OpenAI(
    api_key= "Enter Your API Key"
    )

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a fun fact about space!"}
    ]
)

print(completion.choices[0].message)