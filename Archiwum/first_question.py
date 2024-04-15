import requests
import json
from openai import OpenAI

def query_openai_api(input_message):
    # variables
    input = input_message

    api_key = 'a'
    headers = {
        'Authorization': f'Bearer {api_key}',
    }

    # GET request models endpoint
    response = requests.get('https://api.openai.com/v1/models', headers=headers)

    if response.status_code == 200:
        print("API Request Successful. Available models:")
        print(response.json())
    else:
        print(f"API Request Failed with status code: {response.status_code}")

    print(f"RESPONSE Status: {response.status_code}")
    # ////////////////////////////////////////
    client = OpenAI()

    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{f"role": "user", "content": {input}}],
        stream=True,
    )
    # output

    print(input)

query_openai_api("hello")