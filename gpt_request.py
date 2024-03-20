#IMPORT
import requests
import openai
from openai import OpenAI

client = OpenAI(
  organization='YOUR_ORG_ID',
)
# await fetch("https://api.openai.com/v1/chat/completions",
#             {
#                 method: "POST",
#                 headers: {
#                     "Authorization": "Bearer " + API_KEY,
#                     "Content-Type": "application/json"
#                 },
#                 body: JSON.stringify(apiRequestBody)
#             }).then((data) = > {
# return data.json();
# }).then((data) = > {
# console.log(data);
# setMessages([...chatMessages, {
#     message: data.choices[0].message.content,
#     sender: "ChatGPT"
# }]);
# setIsTyping(false);
# });
# }




# variables
access_token = "aaaa"
URL = "https://api.openai.com/v1/models"
# def
def headers_with_token(access_token):
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    return headers


def query_openai_api(org_id):

    api_key = 'key'
    headers = {
        'Authorization': f'Bearer {api_key}',

    }


    response = requests.get('https://api.openai.com/v1/models', headers=headers)

    if response.status_code == 200:
        print("API Request Successful. Available models:")
        print(response.json())
    else:
        print(f"API Request Failed with status code: {response.status_code}")


query_openai_api('YOUR_ORG_ID')


# END
response ="""json_request"""
print(response)