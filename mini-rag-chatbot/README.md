# Mini RAG Chatbot

This project implements a Retrieval-Augmented Generation (RAG) chatbot using the LLaMA model and LangChain. The chatbot is designed to answer questions based on a small text database related to macroeconomics.

## Project Structure

![alt text](<../rag system.avif.jpg>)

```
mini-rag-chatbot
├── src
│   ├── app.py               # Main entry point of the chatbot application
│   ├── rag
│   │   ├── retriever.py     # Contains the Retriever class for data retrieval
│   │   ├── generator.py      # Contains the Generator class for response generation
│   │   └── pipeline.py       # Orchestrates the retrieval and generation process
│   ├── data
│   │   └── knowledge_base.txt # Text data for the chatbot's knowledge base
│   └── utils
│       └── helpers.py       # Utility functions for various tasks
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mini-rag-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have access to the LLaMA model and any necessary API keys if required.

## Usage

To run the chatbot, execute the following command:
```
python src/app.py
```

You will be prompted to enter your questions related to macroeconomics, and the chatbot will provide responses based on the knowledge base.

## RAG Technique

Retrieval-Augmented Generation (RAG) combines the strengths of retrieval-based and generation-based approaches. The system retrieves relevant information from a knowledge base and uses it to generate coherent and contextually relevant responses. This allows the chatbot to provide accurate answers while maintaining a conversational flow.

## Theme

This chatbot focuses on macroeconomics, providing insights and answers to questions related to economic principles, indicators, and trends. The knowledge base contains curated information to support the chatbot's responses.

## Project Pipeline

1. **Local LLM Model Installation:**  
   The project can be integrated with models such as LLaMA or Mistral, using `llama.cpp` or Hugging Face Transformers to run the model locally.

2. **Data Collection:**  
   Gather `.txt`, `.md`, and/or `.pdf` files with relevant content about trading and macroeconomics.

3. **Text Chunking:**  
   The texts are split into small chunks to facilitate retrieval and processing.

4. **Embeddings Generation:**  
   Each chunk is converted into a numerical vector using `HuggingFaceEmbeddings`.

5. **Vector Store Creation:**  
   The embeddings are stored in an efficient vector store, such as FAISS or Chroma, for fast retrieval.

6. **Pipeline Assembly with LangChain:**  
   LangChain orchestrates the retrieval of relevant chunks and the generation of the final answer by the LLM.

7. **Simple Interface:**  
   Users can interact with the chatbot via terminal or API (FastAPI), sending questions and receiving answers based on the knowledge base.