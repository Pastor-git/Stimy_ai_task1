import os
from wsgiref import headers
import openai
import prompt as prompt
import requests
from openai import OpenAI
import json



client = OpenAI(
    api_key = 'a'
)

def chat(message):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": "Hello, how are you?"
        }]
    )

    response = requests.get('https://api.openai.com/v1/models', headers=headers)
    print(response.json())
    # response = requests.get('https://api.openai.com/v1/models', headers=headers)
    # if chat_completion.choices:
    #     response_messages = chat_completion.choices[0].message
    #     return response_messages['content'] if 'content' in response_messages else "No content found."
    # else:
    #     return "No response."

prompt_message = "how are you?"
print(chat(prompt_message))