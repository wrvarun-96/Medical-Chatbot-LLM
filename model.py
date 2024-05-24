from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
import pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from data_loader import extracted, embeddings_model, documents_split
import os
from langchain_community.vectorstores import FAISS
from prompt import custom_prompt

#Loading vectors
vector_data = FAISS.load_local("/Users/varun/Documents/Data Science/GenAI/Medical_Chatbot/vectorstore/data", embeddings_model(), allow_dangerous_deserialization=True )

#LLM Model(Llama-2)
def llm_model():
  llm = CTransformers(model="/Users/varun/Documents/Data Science/GenAI/Medical_Chatbot/model/llama-2-7b-chat.ggmlv3.q8_0.bin",
                    model_type="llama",
                    config={"max_new_tokens":512,
                            "temperature":0.8})
  return llm

#QA retrieval
def qa_retrieval(llm, prompt, vector_db):

  QA = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_db.as_retriever(search_kwargs={"k":2}),
    return_source_documents=True,
    chain_type_kwargs={'prompt':prompt})

  return QA

def bot():
  embeddings = embeddings_model()
  llm = llm_model()
  prompt = custom_prompt()
  vector_data = FAISS.load_local("/Users/varun/Documents/Data Science/GenAI/Medical_Chatbot/vectorstore/data", embeddings, allow_dangerous_deserialization=True)
  retrieve = qa_retrieval(llm, prompt, vector_data)

  return retrieve

# def final_result(query):
#     qa_system = bot()
#     result = qa_system.invoke({"query": query})
#     print("Response: ", result["result"])
#
# # For final testing with a single query
# final_result(input("Input Prompt: "))