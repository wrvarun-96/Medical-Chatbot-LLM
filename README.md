# Medical Chatbot
This project is a Medical Chatbot built using the LLAMA2 Large Language Model (LLM) with Langchain and FAISS vectorDB. The chatbot is designed to provide medical information and answer health-related queries.

## Features
Conversational AI: Utilizes the LLAMA2 LLM for natural language understanding and response generation.
Efficient Querying: Integrates FAISS vectorDB for fast and accurate information retrieval.
Scalable Architecture: Built with Langchain to manage the conversation flow and maintain context.
Table of Contents
1) Installation
2) Usage
3) Architecture
## Installation
Prerequisites
Ensure you have the following installed:

1)Python 3.9 or higher
2)pip (Python package installer)
3) git
## Steps
Clone the repository:

bash
Copy code
git clone https://github.com/wrvarun-96/Medical_Chatbot.git
cd Medical_Chatbot
Install the required packages:

bash
Copy code
pip install -r requirements.txt
## Usage
Running the Chatbot
To start the chatbot, run the following command:

bash
Copy code
python main.py
Interacting with the Chatbot
Once the chatbot is running, you can interact with it via the terminal or a web interface (if implemented). Simply type your medical queries, and the chatbot will respond with relevant information.

## Architecture
The Medical Chatbot is built using the following components:

-> LLAMA2 : Provides the natural language understanding and generation capabilities.
-> Langchain: Manages the conversation flow and maintains context across interactions.
-> FAISS vectorDB: Facilitates fast and efficient information retrieval for answering queries.
## High-Level Overview
-> User Input: The user inputs a query.
-> Processing: Langchain processes the input and interacts with the LLAMA2 model.
-> Query Handling: If the query requires specific information, Langchain uses FAISS vectorDB to retrieve relevant data.
-> Response Generation: The LLAMA2 model generates a response based on the processed input and retrieved data.
-> User Output: The response is sent back to the user.
