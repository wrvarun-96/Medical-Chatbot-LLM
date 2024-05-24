from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

def extract_data(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()

    return docs

extracted = extract_data("/Users/varun/Documents/Data Science/GenAI/Medical_Chatbot/data/")

#Create chunks of data
def doc_spliter(extracted):
    chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=30)
    text_chunks = chunks.split_documents(extracted)

    return text_chunks

documents_split = doc_spliter(extracted)

#Embedding model
def embeddings_model():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    return embeddings

#Creating and soring vectors
# vector_store = FAISS.from_documents(documents_split, embeddings_model())
# vector_store.save_local("/Users/varun/Documents/Data Science/GenAI/Medical_Chatbot")
