# Custom Data GPT

[![label](https://img.shields.io/badge/%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3-ZH-brightgreen)](https://github.com/aboutmydreams/custom_data_gpt/blob/main/README_ZH.md)
[![label](https://img.shields.io/badge/English-EN-brightgreen)](https://github.com/aboutmydreams/custom_data_gpt/blob/main/README.md)
[![label](https://img.shields.io/badge/aiis.life-AI%20is%20life-orange)](https://www.aiis.life)
[![label](https://img.shields.io/badge/NonceGeek-cool--oriented%20programming-orange)](https://noncegeek.com)



This project is a chatbot based on OpenAI, suitable for enterprise privatized data fine-tuning. It can answer various questions related to enterprise products raised by users. It uses OpenAI's API for language model training and generation, and uses Faiss for text search and similarity matching. It supports getting training data from local files or URLs. This project is an enhanced version of [Custom-Company-Chatbot](https://replit.com/@DavidAtReplit/Custom-Company-Chatbot), inspired by the original project, extending the private data acquired from the network and locally (in principle, this is not true training, but finding relevant contexts and then telling GPT). Thanks to [@leeduckgo](https://github.com/leeduckgo) for the inspiring support.

## Steps to use

1. Add `API_SECRET=MySecret` and `OPENAI_API_KEY=<your-key>` to the .env file, where `<your-key>` is your [OpenAI API Key](https://beta.openai.com/account/api-keys).
2. Install the required dependencies for the project using poetry,
   - `pip install poetry`
   - `poetry install`
   - `poetry shell`
3. Activate the virtual environment and run `python3 main_api.py`.
4. Use an HTTP POST request to send a training request to [http://localhost:5000/train](http://localhost:5000/train), passing in the file list of training data and the model name.
5. Use an HTTP POST request to send a chat request to [http://localhost:5000/chat](http://localhost:5000/chat), passing in the model name, question, and history.

## API Documentation

### /train

This interface is used for language model training.

#### Request

- Method: POST
- Request body: JSON format
- Request body parameters:
  - file_list: A list of files to be trained
  - space_name: The vector space name
  - file_tag: `url` (network txt data) or `path` (local data) for the data

```json
{
    "file_list": ["https://cdn.vitae3.me/public-static/213113032213132120.1680148867987.txt"],
    "space_name": "train_space_name",
    "file_tag": "url",
}
```

#### Response

- Status code: 200
- Response body: JSON format
- Response body parameters:
  - code: status message 0 normal, 1 abnormal
  - data: data
  - msg: success

```json
{
  "code": 0,
  "data": {
    "index_space_size": 6.0439,
    "space_name": "train_space_name",
    "pkl_space_size": 2.4023,
    "size_type": "kb"
  },
  "msg": "success"
}
```

### /chat

This API is used for chatbot conversations.

#### chat request

- Method: POST
- Request Body: JSON format
- Request Body Parameters:
  - space_name: the name of the vector space stored locally
  - question: the question being asked
  - history: the conversation history
  - model_name: the model name, eg: text-davinci-003, gpt-3.5-turbo, gpt-3.5-turbo-0301, you can try more language generation models in the [Model List](https://platform.openai.com/docs/models) and check the pricing of different models in the [Pricing List](https://openai.com/pricing).

```json
{
  "history": ["human: how are u", "Bot: fine"],
  "question": "How to build a GPT3 Chatbot for your Company",
  "space_name": "train_space_name",
  "model_name": "text-davinci-003",
}
```

#### chat response

- Status Code: 200
- Response Body: JSON format
- Response Body Parameters:
  - code: status information 0 normal, 1 exception
  - data: data
  - msg: success

```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "answer": " Building a GPT3 chatbot for your company requires a few steps. First, you need to get your OpenAI API key and add it to Secrets as OPENAI_API_KEY. Next, you need to create an API_KEY for the JSON API. After that, you need to fill the training/facts folder with as many text documents as you can containing information about the company you're training it on. Finally, you need to edit the prompt/master.txt file to represent how you want the bot to behave when interacting with the users.",
        "history": [
            "human: how are u",
            "Bot: fine",
            "Human: How to build a GPT3 Chatbot for your Company",
            "Bot:  Building a GPT3 chatbot for your company requires a few steps. First, you need to get your OpenAI API key and add it to Secrets as OPENAI_API_KEY. Next, you need to create an API_KEY for the JSON API. After that, you need to fill the training/facts folder with as many text documents as you can containing information about the company you're training it on. Finally, you need to edit the prompt/master.txt file to represent how you want the bot to behave when interacting with the users."
        ]
    }
}
```

## Notes

- This project is built with Python 3.10 and is for learning and research purposes only. Please do not use it for any purposes that could harm the social environment.
- If you have a large amount of text, it will take a long time to train and require a lot of computing resources.
- Please read the documentation and code carefully before using it, and make sure that the API key and training data are properly configured.

Welcome to join the early Custom AI Chinese community

<p>
  <img alt="QQ-Group" src="https://cdn.nlark.com/yuque/0/2023/png/164272/1680279312300-35636818-45ad-41ce-b0c7-d86aba020a2e.png?x-oss-process=image%2Fresize%2Cw_962%2Climit_0" width="300" style="border-radius: 10%;">
  <img alt="WX-Group" src="https://cdn.nlark.com/yuque/0/2023/png/164272/1680278249286-59ac3cbd-a27b-4c54-87a1-3dd6f9cd46e0.png" width="300" style="border-radius: 10%;">
</p>
