# Retrieval-Augmented Generation Application
### Using LangChain and OpenAI

## Introduction
With this Retrieval-Augmented Generation (RAG) application, you can create chatbots for your documents, books, or files. You can also use it to build rich, interactive AI applications that use your data as a source. 
Examples:
1. Ask questions about a large set of documents
2. Create a customer support chatbot that helps customers by following a set of instructions.
### Creating the RAG application
The process for creating the app is as follows:
1. Split your data into chunks of text (500 to 1000 words) to store your data more efficiently. This allows the retrieval process to capture pieces of information that are more relevant to the query, and the generation by the LLM (OpenAI model) to be more precise. It is also less costly, as only parts of a document will be included in the prompt, instead of the entire document collection.
2. Create vector embeddings from the chunks and store them in a [Chroma database](https://www.trychroma.com/). Vector embeddings are numerical representations of terms, which can be words, sentences, or documents. These embeddings capture the relationships and similarities between the terms. In language models, this allows the model to understand the meaning and context of words based on their similarity to other words.
3. Use the query input by the user to perform a similarity search and retrieve a set of relevant chunks from the database.
4. The LLM (OpenAI model) uses the relevant chunks as context and sends a response along with its sources.
### Example output:
<img src="https://github.com/mlsmall/RAG-Application-with-LangChain/blob/main/output.png" width="1000" />

## Instructions
### Download the repository
* Go to a terminal and paste `git clone https://github.com/mlsmall/RAG-Application-with-LangChain.git`

### OpenAI API Key
Before you begin, set up an OpenAI account and generate a new key. You will need to put your credentials in a `.env` file.
* Go to https://platform.openai.com/api-keys and create an OpenAI key.
* Create a `.env` file in your project directory and add `OPENAI_API_KEY="your_generated_secret_key"`.
* Create a `.gitignore` file in your project directory and add `.env`.

### Copy your documents (Optional)
* Go to the `data` directory and add your document files in `.md` format.
* Go to the `create_database.py` file and set the variable `DATA_PATH = "data"` or to the directory name where you will store data.
  
### Running the application
Inside a terminal, run the following:
* Install dependencies
`pip install -r requirements.txt`

* Create the Chroma Database
`python create_database.py`

* Query the Chroma Database
`python query_data.py "What operating systems does EC2 support"`
