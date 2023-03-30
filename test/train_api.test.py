import requests
import json

def test_train_api(payload):
    url = "http://127.0.0.1:5000/train"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response.text

payload_url = json.dumps({
    "file_list": ["https://cdn.vitae3.me/public-static/213113032213132120.1680148867987.txt"],
    "model_name": "train_model_name",
    "get_file_type": "url",
})

payload_path = json.dumps({
    "file_list": ["./training/master.txt"],
    "model_name": "train_model_name_path_test",
    "get_file_type": "path",
})

test_train_api(payload_url)
test_train_api(payload_path)