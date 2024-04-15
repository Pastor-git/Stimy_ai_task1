import openai

# Best practice: Load the API key from an environment variable or secure vault.
# For demonstration purposes, you'll set it directly here,
# but replace 'your_api_key' with the variable loading the key securely.
openai.api_key = 'a'

def query_openai_api(input_message):
    try:
        response = openai.Completion.create(
            model="gpt-4",
            prompt=input_message,
            max_tokens=50
        )

        print("Response:")
        print(response.choices[0].text.strip())
    except Exception as e:
        print(f"An error occurred: {e}")

query_openai_api("how are you?")