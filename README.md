# Medical Chatbot
This project is a Medical Chatbot built using the LLAMA2 Large Language Model (LLM) with Langchain and FAISS vectorDB. The chatbot is designed to provide medical information and answer health-related queries.

## Features
- **Conversational AI:** Utilizes the LLAMA2 LLM for natural language understanding and response generation.
- **Efficient Querying:** Integrates FAISS vectorDB for fast and accurate information retrieval.
- **Scalable Architecture:** Built with Langchain to manage the conversation flow and maintain context.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
## Installation
### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- git
## Steps
1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/Medical_Chatbot.git
    cd Medical_Chatbot
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```
## Usage
Running the Chatbot
To start the chatbot, run the following command:

```bash
python main.py
```
Interacting with the Chatbot
Once the chatbot is running, you can interact with it via the terminal or a web interface (if implemented). Simply type your medical queries, and the chatbot will respond with relevant information.

## Architecture
The Medical Chatbot is built using the following components:

1) LLAMA2 : Provides the natural language understanding and generation capabilities.
2) Langchain: Manages the conversation flow and maintains context across interactions.
3) FAISS vectorDB: Facilitates fast and efficient information retrieval for answering queries.
## High-Level Overview
1) User Input: The user inputs a query.
2) Processing: Langchain processes the input and interacts with the LLAMA2 model.
3) Query Handling: If the query requires specific information, Langchain uses FAISS vectorDB to retrieve relevant data.
4) Response Generation: The LLAMA2 model generates a response based on the processed input and retrieved data.
5) User Output: The response is sent back to the user.
