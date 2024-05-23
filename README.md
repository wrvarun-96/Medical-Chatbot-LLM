# Medical Chatbot
This project is a comprehensive Medical Chatbot designed to provide accurate and relevant medical information and respond to health-related queries. The core of the chatbot is built using the LLAMA2 Large Language Model (LLM), known for its advanced natural language processing capabilities. By utilizing Langchain, the chatbot effectively manages conversation flow and maintains context throughout interactions, ensuring coherent and contextually appropriate responses.

In addition to these components, the chatbot employs FAISS vectorDB for efficient and rapid information retrieval. This enables the system to quickly access and deliver relevant data from a vast pool of medical knowledge, enhancing the user experience by providing timely and precise answers. The integration of these technologies ensures that the chatbot not only understands and processes user queries accurately but also delivers information in a manner that is both informative and easy to comprehend.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Steps](#steps)
- [Usage](#usage)
- 
## Features
- **Conversational AI:
The chatbot utilizes the LLAMA2 Large Language Model (LLM) to understand and generate natural language responses. LLAMA2 is a state-of-the-art language model capable of processing complex medical terminology and providing accurate, context-aware answers to user queries. Its advanced natural language understanding capabilities ensure that the chatbot can handle a wide range of questions with high precision, making interactions feel seamless and human-like.

- **Efficient Querying:
The integration of FAISS vectorDB significantly enhances the chatbot's ability to retrieve information quickly and accurately. FAISS (Facebook AI Similarity Search) is a powerful library for efficient similarity search and clustering of dense vectors. By leveraging FAISS, the chatbot can swiftly search through large datasets of medical information to find the most relevant data points in response to user queries. This ensures that users receive timely and pertinent information, improving the overall user experience.

- **Scalable Architecture:
The chatbot is built using Langchain, a framework designed to manage the flow of conversations and maintain context over multiple interactions. Langchain's capabilities allow the chatbot to handle complex dialogue structures, ensuring that it can follow and contribute to extended conversations without losing track of context. This scalability is crucial for providing consistent and coherent responses, especially in dynamic and multi-turn conversations, which are common in medical consultations.
These features combine to create a robust, responsive, and user-friendly medical chatbot capable of delivering high-quality medical information and support.
  
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
