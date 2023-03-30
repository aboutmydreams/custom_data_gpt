# Custom Data GPT

本项目是一个基于 OpenAI，适用于企业私有化数据微调的聊天机器人，能够回答用户提出的各种和企业产品相关的问题。使用 OpenAI 的 API 进行语言模型的训练和生成，使用 Faiss 进行文本搜索和相似度匹配，支持从本地文件或 URL 获取训练数据。本项目为 [Custom-Company-Chatbot](https://replit.com/@DavidAtReplit/Custom-Company-Chatbot) 的增强版，受原项目启发，扩展了从网络以及本地获取 train 的私有数据。感谢 [@leeduckgo](https://github.com/leeduckgo) 的激励支持。

## 使用步骤

1. 在 .env 文件中添加 API_SECRET=MySecret 和 OPENAI_API_KEY=<your-key>，其中 <your-key> 为你的 OpenAI API key。
2. 使用 poetry 安装项目所需的依赖，
    - `pip install poetry`
    - `poetry install`
    - `poetry shell`
3. 启动虚拟环境，运行 python3 main_api.py。
4. 使用 HTTP POST 请求向 <http://localhost:5000/train> 发送训练请求，传入训练数据的文件列表和模型名称。
5. 使用 HTTP POST 请求向 <http://localhost:5000/chat> 发送聊天请求，传入模型名称、问题和历史记录。

## API 接口文档

### /train

该接口用于训练语言模型。

#### 请求

- 方法：POST
- 请求体：JSON 格式
- 请求体参数：
  - file_list：要训练的文件列表
  - model_name：模型名称

#### 响应

- 状态码：200
- 响应体：JSON 格式
- 响应体参数：
  - code：状态信息 0 正常，1 异常
  - data: 数据
  - msg: success

```json
{
  "code": 0,
  "data": {
    "index_model_size": 6.0439,
    "model_name": "train_model_name",
    "pkl_model_size": 2.4023,
    "size_type": "kb"
  },
  "msg": "success"
}
```

### /chat

该接口用于进行聊天。

#### chat 请求

- 方法：POST
- 请求体：JSON 格式
- 请求体参数：
  - model_name：模型名称
  - question：问题
  - history：历史记录

#### chat 响应

- 状态码：200
- 响应体：JSON 格式
- 响应体参数：
  - code：状态信息 0 正常，1 异常
  - data: 数据
  - msg: success

```json
{
    "code": 0,
    ""
    "data": {
        "answer": " Building a GPT3 chatbot for your company requires a few steps. First, you need to get your OpenAI API key and add it to Secrets as OPENAI_API_KEY. Next, you need to create an API_KEY for the JSON API. After that, you need to fill the training/facts folder with as many text documents as you can containing information about the company you're training it on. Finally, you need to edit the master.txt file to represent how you want the bot to behave when interacting with the users.",
        "history": [
            "human: how are u",
            "Bot: fine",
            "Human: How to build a GPT3 Chatbot for your Company",
            "Bot:  Building a GPT3 chatbot for your company requires a few steps. First, you need to get your OpenAI API key and add it to Secrets as OPENAI_API_KEY. Next, you need to create an API_KEY for the JSON API. After that, you need to fill the training/facts folder with as many text documents as you can containing information about the company you're training it on. Finally, you need to edit the master.txt file to represent how you want the bot to behave when interacting with the users."
        ]
    }
}
```

## 注意事项

- 本项目由 python3.10 构建，仅供学习和研究使用，请勿用于破坏社会环境的用途。
- 若文本数量较大，需要较长时间的训练时间和大量的计算资源。
- 使用前请仔细阅读文档和代码，并确保已经正确配置 API key 和训练数据。
