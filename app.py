from flask import Flask, render_template, jsonify, request
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from data_loader import embeddings_model
from model import llm_model, qa_retrieval
from prompt import custom_prompt
import os

app = Flask(__name__)

embeddings = embeddings_model()

vector_data_flask = FAISS.load_local("/Users/varun/Documents/Data Science/GenAI/Medical_Chatbot/vectorstore/data", embeddings, allow_dangerous_deserialization=True)

prompt_flask = custom_prompt()
chain_type_kwargs = {"prompt": prompt_flask}

llm_flask = llm_model()

qa_flask = qa_retrieval(llm_flask, prompt_flask, vector_data_flask)

@app.route("/")
def index():
    return render_template('chatbot_llm.html')

@app.route("/get_response", methods=["POST"])
def get_response():
    message = request.json.get("query")
    app.logger.debug(f"Received query: {message}")
    result = qa_flask({"query": message})
    app.logger.debug(f"Response: {result['result']}")
    return jsonify({"result": result['result']})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
