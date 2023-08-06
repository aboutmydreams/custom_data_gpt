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


def ask_question_about_zym(q: str):
    zym_info = """
    Zhang Yiming is the founder and CEO of Chinese technology company ByteDance. ByteDance is a leading global digital media and artificial intelligence technology company, best known for Douyin (known as TikTok outside of China), a short video platform with a huge global audience.
    Zhang Yiming was born in Fuzhou, Fujian Province in 1983, and later obtained a bachelor's degree in microelectronics and a master's degree in software engineering from Zhejiang University. Before founding ByteDance, he worked at various companies, including Microsoft and travel site Kuxun.
    In 2012, Zhang Yiming founded ByteDance and launched the company's first product, Toutiao, a news recommendation application based on artificial intelligence algorithms. Then, in 2016, ByteDance launched Douyin, an app that quickly became a huge success globally, attracting hundreds of millions of users.
    Known for his keen business vision and relentless spirit of innovation, Zhang Yiming has successfully led ByteDance's diversification and globalization process. Under his leadership, ByteDance has become one of the world's most valuable startups with more than 60,000 employees worldwide.
    """
    payload = json.dumps(
        {
            "history": ["human: who is Zhang Yiming", f"Bot: {zym_info}"],
            "question": q,
            "space_name": "zym",
            "model_name": "gpt-3.5-turbo",
            "prompt_name": "zym",  # 非必填参数，默认则是 master
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
        return f"ask_question_about_zym error: {str(e)}"


questions = """作者的内容截止到2016年，请根据你的理解，推测在2023年，作者的公司可能在从事的业务，发展情况等

以下哪一条更可能是作者所创办公司的使命？请简述原因 1）激发创造 丰富生活 2） 用科技让复杂的世界更简单 3） 帮大家吃得更好，生活更好 4） 让全球多一点幸福

作者的内容截止到2016年，请根据你的理解，推测在2023年，作者的公司可 能在从事的业务，发展情况等

请尝试用MBTI人格分析法来分析作者的人格，并给出较详细的理由

2012-4-2412:54 来自微博 weibo.com 很香，感觉还没饱，但是我忍住了，立志不成为有啤酒肚的中年男 抱歉，此微博己被作者删除。查看帮助：。网页链接 这条内容表达作者什么思考

你觉得作者可能是中国哪一位著名互联网企业家很类似？简述理由？

推测以下信息并简单说明原因 1） 作者的大概年龄 2） 作者的公司可能的管理方式和企业文化 3） 作者比较推崇哪些公司，比较反感那些公司

如果作者的公司开展国际化业务，你认为最可能直接竞争的美国公司有哪些？ 为什么？

你觉得作者创办的公司在美国经营时，有哪些尤其要注意的地方？可能引起哪 些争议？

你觉得作者可能是中国哪一位著名互联网企业家？简述理由""".split(
    "\n\n"
)

for q in questions:
    ask_question_about_zym(q)
    time.sleep(3)
