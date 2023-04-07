from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

#verifica os modelos GET
#link = "https://api.openai.com/v1/models"
#request = requests.get(link, headers=headers)
#print(request)
#print(request.text)

link = "https://api.openai.com/v1/chat/completions"

id_model = "gpt-3.5-turbo"

body_message = {
    "model": id_model,
    "messages": [{"role": "user", "content": "Oi tudo bem?"}]
}

body_message = json.dumps(body_message)
#print(body_message)

#request POST
request = requests.post(link, headers=headers, data=body_message)
print(request)
print(request.text)
