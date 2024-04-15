import openai
import os
from openai import OpenAI


openai.api_key = os.getenv("OPENAI_API_KEY")
# test
# print(os.getenv("OPENAI_API_KEY"))

def test_hello(message):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        stream=True,
    )
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


test_hello("how are you?")

