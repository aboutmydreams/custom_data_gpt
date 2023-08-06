import requests
import json
import time
import os

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

# url = "http://127.0.0.1:5000/chat"
url = "https://cleverspanishautoresponder--abouthomeloving.repl.co/auto_chat"


def append_str_to_file(s):
    with open(f"{current_dir}/text.txt", "a", encoding="utf-8") as f:
        f.write(s + "\n")
    f.close()


def ask_question_about_debox(q: str):
    debox_info = """DeBox is the first and best community-driven Web3 social platform. DeBox focuses on solving the problem of social information authenticity and reducing fraud. DeBox will provide decentralized social features and services for Web 3.0 communities, such as holding tokens to chat, open platforms for DAO tools, multi-dimensional social graphs, etc."""
    payload = json.dumps(
        {
            "history": ["human: what is debox", f"Bot: {debox_info}"],
            "question": q,
            "space_name": "debox",
            "model_name": "gpt-3.5-turbo",
            "prompt_name": "debox",  # 非必填参数，默认则是 master
        }
    )
    headers = {"Content-Type": "application/json"}

    try:
        ask_info = f"user question: {q}. waiting..."
        append_str_to_file(ask_info)
        print(ask_info)
        response = requests.request("POST", url, headers=headers, data=payload)
        answer_info = f'gpt: {response.json()["data"]["answer"]}'
        append_str_to_file(answer_info)
        print(answer_info)

        return response.text
    except Exception as e:
        return f"ask_question_about_debox error: {str(e)}"


questions = """how to download debox

can you give me some debox links""".split(
    "\n\n"
)

for q in questions:
    ask_question_about_debox(q)
    time.sleep(3)
