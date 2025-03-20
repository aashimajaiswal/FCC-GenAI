import os
from dotenv  import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from prompt import *

# set up the environment
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def file_processing(file_path):

    # Load the document
    loader = PyPDFLoader(file_path)
    data = loader.load()

    # Extract the documents
    question_gen = ""
    for page in data:
        question_gen += page.page_content
    
    # Chunking
    # for questions
    splitter_ques_gen = TokenTextSplitter(
        model_name='gpt-3.5-turbo',
        chunk_size = 1000,
        chunk_overlap = 200
    )
    chunk_ques_gen = splitter_ques_gen.split_text(question_gen)
    document_ques_gen = [Document(page_content=chunk) for chunk in chunk_ques_gen]
    # for answers
    splitter_ans_gen = TokenTextSplitter(
        model_name='gpt-3.5-turbo',
        chunk_size = 1000,
        chunk_overlap = 100
    )
    document_ans_gen = splitter_ans_gen.split_documents(document_ques_gen)

    return document_ques_gen, document_ans_gen

def llm_pipeline(file_path, topic):

    document_ques_gen, document_ans_gen = file_processing(file_path)

    # question generation chain
    llm_ques_gen_pipeline = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    PROMPT_QUESTIONS = PromptTemplate(template=prompt_template, input_fields=["topic", "source_material"])
    question_gen_chain = LLMChain(
        llm=llm_ques_gen_pipeline,
        prompt=PROMPT_QUESTIONS
    )
    generated_questions = question_gen_chain.run(topic=topic, source_material=document_ques_gen)

    # formating qs to get answers
    ques_list = generated_questions.split("\n")
    ques_list = [q for q in ques_list if q.strip() != '']

    # answer generation chain
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(document_ans_gen,embeddings)
    llm_ans_gen_pipeline = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    ans_chain = RetrievalQA.from_chain_type(llm = llm_ans_gen_pipeline, chain_type = "stuff",
                                         retriever = vector_store.as_retriever())
    
    return ans_chain, ques_list