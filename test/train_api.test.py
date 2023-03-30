import requests
import json

url = "http://127.0.0.1:5000/train"

payload = json.dumps({
  "urls": ["https://cdn.vitae3.me/public-static/213113032213132120.1680148867987.txt"],
  "model_name": "train_model_name",
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)