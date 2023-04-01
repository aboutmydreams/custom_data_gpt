from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
import faiss
import os,sys
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle
from langchain import OpenAI, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import Prompt
from dotenv import load_dotenv

load_dotenv()


def train():
    trainingData = list(Path("training/facts/").glob("**/*.*"))

    # check there is data in the trainingData folder

    if len(trainingData) < 1:
        print(
            "The folder training/facts should be populated with at least one .txt or .md file.",
            file=sys.stderr,
        )
        return

    data = []
    for training in trainingData:
        with open(training) as f:
            print(f"Add {f.name} to dataset")
            data.append(f.read())

    textSplitter = CharacterTextSplitter(chunk_size=2000, separator="\n")

    docs = []
    for sets in data:
        docs.extend(textSplitter.split_text(sets))

    store = FAISS.from_texts(docs, OpenAIEmbeddings())
    faiss.write_index(store.index, "training.index")
    store.index = None

    with open("faiss.pkl", "wb") as f:
        pickle.dump(store, f)


def runPrompt():
    index = faiss.read_index("training.index")

    with open("faiss.pkl", "rb") as f:
        store = pickle.load(f)

    store.index = index

    with open("training/prompt/master.txt", "r") as f:
        promptTemplate = f.read()

    prompt = Prompt(
        template=promptTemplate, input_variables=["history", "context", "question"]
    )

    # llmChain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0.25))
    llmChain = LLMChain(
        prompt=prompt,
        llm=OpenAI(
            temperature=0.25,
            model_name="gpt-3.5-turbo-0301",
            openai_api_key=os.environ["OPENAI_API_KEY"],
        ),
    )

    def onMessage(question, history):
        docs = store.similarity_search(question)
        contexts = []
        for i, doc in enumerate(docs):
            contexts.append(f"Context {i}:\n{doc.page_content}")
            answer = llmChain.predict(
                question=question, context="\n\n".join(contexts), history=history
            )
        return answer

    history = []
    while True:
        question = input("Ask a question > ")
        answer = onMessage(question, history)
        print(f"Bot: {answer}")
        history.append(f"Human: {question}")
        history.append(f"Bot: {answer}")
