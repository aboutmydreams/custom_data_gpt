import requests
import json

url = "http://127.0.0.1:5000/chat"

payload = json.dumps({
  "history": ["human: how are u", "Bot: fine"],
  "question": "How to build a GPT3 Chatbot for your Company",
  "space_name": "train_space_name",
  "model_name": "text-davinci-003",
  "prompt_name": "if-u-were-me", # 非必填参数，默认则是 master
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)