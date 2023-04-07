import requests
import json

def test_train_api(payload):
    url = "http://127.0.0.1:5000/upload_prompt"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response.text

payload_url = json.dumps({
    "file_list": ["https://cdn.vitae3.me/public-static/213113032213132120.1680148867987.txt"],
})

test_train_api(payload_url)
