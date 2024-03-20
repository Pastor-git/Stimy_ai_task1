import requests

def query_openai_api():

    api_key = 'key'
    headers = {
        'Authorization': f'Bearer {api_key}',
    }

    # GET request models endpoint.
    response = requests.get('https://api.openai.com/v1/models', headers=headers)

    if response.status_code == 200:
        print("API Request Successful. Available models:")
        print(response.json())
    else:
        print(f"API Request Failed with status code: {response.status_code}")


query_openai_api()
