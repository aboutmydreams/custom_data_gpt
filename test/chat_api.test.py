import requests
import json

url = "http://127.0.0.1:5000/chat"

payload = json.dumps({
  "history": ["human: how are u", "Bot: fine"],
  "question": "How to build a GPT3 Chatbot for your Company",
  "model_name": "train_model_name",
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)