# LangChain
Notes on theory and projects from 9:35:25 to 11:46:21.

Doc: https://python.langchain.com/docs/introduction/
- Langchain is a framework to make GenAI applications using LLM models.
- why prompt template? Don't want user to type in long prompts again and again for different categories.
- Chain: combine different components like LLMs and prompts in a sequence/ chain to make a gen ai end product
- Sequence Chains: Combine multiple chains
- Simple Sequence Chain vs Sequence Chain: Simple one only shows the last output
- Agents usually have autonomy to perform multi-step tasks independently. They can plan, execute, reason, and interact with tools without constant human guidance.
- tool: a function to do something
- env setup
    ```python
    import os
    os.environ['OPENAI_API_KEY'] = "<key>"
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "<key>"
    ```
- can run langchain with source as a pandas df: https://python.langchain.com/docs/integrations/tools/pandas/
- hugging face langchain: https://python.langchain.com/docs/integrations/providers/huggingface/
- code is the same, you just pass different llm names in the `llm` parameter.

## Project: Interview Questions Creator Application
- What? User provides a document, application uses this document to create interview questions as well as the answers from it
- To use: Langchain, GPT 3.5, FAISS (vector db), Fast API (to make a UI)
    - Architecture: Pdf -> Extract Docs -> Chunks -> Embedding model -> Vector Embeddings -> Vector DB
    - LLM (with appropriate prompt) -> creates questions -> these questions are put again in the model
- Steps
    - create conda env // creates an isolated workspace to seperate from other projects that might be using diff versions of packages
    - create `requirements.txt`
    - make the `.env` with the required keys

## Project: Custom Website Chatbot 
- Basic RAG project: supply a website to the llm and ask on questions on that particular website
- to get the page structure of any website add `/sitemap.xml` to the route like `https://www.google.com.sg/sitemap.xml`
