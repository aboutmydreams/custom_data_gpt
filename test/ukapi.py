import requests
import json
import time
import os

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

url = "http://127.0.0.1:5000/chat"


def append_str_to_file(s):
    with open(f"{current_dir}/text.txt", "a", encoding="utf-8") as f:
        f.write(s + "\n")
    f.close()


def ask_question_about_ukapi(q: str):
    ukapi_info = """
    Zhang Yiming is the founder and CEO of Chinese technology company ByteDance. ByteDance is a leading global digital media and artificial intelligence technology company, best known for Douyin (known as TikTok outside of China), a short video platform with a huge global audience.
    Zhang Yiming was born in Fuzhou, Fujian Province in 1983, and later obtained a bachelor's degree in microelectronics and a master's degree in software engineering from Zhejiang University. Before founding ByteDance, he worked at various companies, including Microsoft and travel site Kuxun.
    In 2012, Zhang Yiming founded ByteDance and launched the company's first product, Toutiao, a news recommendation application based on artificial intelligence algorithms. Then, in 2016, ByteDance launched Douyin, an app that quickly became a huge success globally, attracting hundreds of millions of users.
    Known for his keen business vision and relentless spirit of innovation, Zhang Yiming has successfully led ByteDance's diversification and globalization process. Under his leadership, ByteDance has become one of the world's most valuable startups with more than 60,000 employees worldwide.
    """
    payload = json.dumps(
        {
            "history": ["human: who is Zhang Yiming", f"Bot: {ukapi_info}"],
            "question": q,
            "space_name": "ukapi",
            "model_name": "gpt-3.5-turbo",
            "prompt_name": "ukapi",  # 非必填参数，默认则是 master
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
        return f"ask_question_about_ukapi error: {str(e)}"


questions = """基于 python 写一个调用 uktradeinfo api 获取数据的函数，输入商品关键词或者代码，返回每个公司对该商品进口数据

""".split(
    "\n\n"
)

for q in questions:
    ask_question_about_ukapi(q)
    time.sleep(3)
