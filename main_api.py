from flask import Flask, jsonify, request, send_file
from typing import List, Union
import requests
import faiss
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle, os
from langchain import OpenAI, LLMChain
from langchain.prompts import Prompt
from dotenv import load_dotenv

from utils.flask_input_fixed import Inputs, JsonSchema
from utils.get_file_size import get_file_size

load_dotenv()
app = Flask(__name__)

class TrainInputs(Inputs):
    """
    针对 '/train' 视图函数的输入参数规则
    """
    json = [JsonSchema({
        'model_name': Union[str, int],
        'file_list': List[str],
        'get_file_type': str, # "url" | "path"
    })]

@app.route("/train", methods=["POST"])
def train():
    inputs = TrainInputs(request)
    if not inputs.validate():
        errors = []
        for error in inputs.errors:
            errors.append({'message': error.message})
        return jsonify({'errors': errors}), 400

    try:
        file_list = request.json["file_list"]
        model_name = request.json["model_name"]
        get_file_type = request.json["get_file_type"]
        index_path = "./training/models/{}.index".format(model_name)
        pkl_path = "./training/models/{}.pkl".format(model_name)

        trainingData = []
        
        if get_file_type == "url":
            for url in file_list:
                r = requests.get(url)
                if r.status_code == 200:
                    trainingData.append(r.text)
        else:
            for file_path in file_list:
                with open(file_path, "r") as data_file:
                    use_text = data_file.read()
                trainingData.append(use_text)
                data_file.close()
        if len(trainingData) < 1:
            return jsonify({"error": "No training data found"}), 400
        textSplitter = CharacterTextSplitter(chunk_size=2000, separator="\n")
        docs = []
        for sets in trainingData:
            docs.extend(textSplitter.split_text(sets))
        store = FAISS.from_texts(docs, OpenAIEmbeddings())
        faiss.write_index(store.index, index_path)
        store.index = None
        with open(pkl_path, "wb") as f:
            pickle.dump(store, f)
        # 如果需要下载 model 文件
        # return send_file("./training/models/{}.pkl".format(model_name), as_attachment=True)
        return jsonify({
                    "code": 0,
                    "msg": "success",
                    "data": {"model_name": model_name,
                             "size_type": "kb",
                             "pkl_model_size": get_file_size(pkl_path),
                             "index_model_size": get_file_size(index_path)}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


class ChatInputs(Inputs):
    """
    针对 '/train' 视图函数的输入参数规则
    """
    json = [JsonSchema({
        'model_name': Union[str, int],
        'question': str,
        'history': List[Union[str, None]],
    })]

@app.route("/chat", methods=["POST"])
def chat():
    inputs = ChatInputs(request)
    if not inputs.validate():
        errors = []
        for error in inputs.errors:
            errors.append({'message': error.message})
        return jsonify({'errors': errors}), 400
    try:
        model_name = request.json["model_name"]
        question = request.json["question"]
        history = request.json["history"]

        index = faiss.read_index("./training/models/{}.index".format(model_name))
        with open("./training/models/{}.pkl".format(model_name), "rb") as f:
            store = pickle.load(f)
        store.index = index

        with open("training/master.txt", "r") as f:
            promptTemplate = f.read()

        prompt = Prompt(
            template=promptTemplate, input_variables=["history", "context", "question"]
        )
        
        llmChain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0.25,openai_api_key=os.environ["OPENAI_API_KEY"]))
        
        docs = store.similarity_search(question)
        contexts = []
        for i, doc in enumerate(docs):
            contexts.append(f"Context {i}:\n{doc.page_content}")
        answer = llmChain.predict(
            question=question, context="\n\n".join(contexts), history=history
        )
        response = {
            "answer": answer,
            "history": history + [f"Human: {question}", f"Bot: {answer}"],
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
