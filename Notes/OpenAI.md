# OpenAI Notes

Notes on theory and projects from 5:12:14 to 7:12:54.

## Introduction to OpenAI 
- Access via Open AI website > API Platform. Currently paid $5.
- No need to download models, model are ran on servers and accessed via API Keys.
- Documentation on the website has everything with code samples.
- tldr: Gave an overview of the Open AI API Platform.

## Generating Open AI Key
- Dashboard > API Keys
- Params
    - temperature: how much random the model can be with their output (0: null/strict, 1: full freedom/creative)
    - Top P: p is the number of responses
    - can hover to see more info about params
    - imp: temp, top p, max tokens

## Hands on OpenAI - ChatCompletion API and Completion API
- setting up connection to OpenAI: https://platform.openai.com/docs/quickstart
- set up requirements.txt
    ```
    openai == 0.28
    pandas
    python-dotenv
    ```
- dotenv to put the API key in it, make a .env file (need to remove it when pushing changes to github as it is a secret)
    ```
    OPENAI_API_KEY = "<key>"
    ```
- anaconda is already there in codespaces, but incase of update use `$ conda update conda`
- before installing the packages need to create a virtual enviroment with terminal command `$ conda create -n openaidemo python=3.10 -y`
- `$ conda init`
- activate env with `$ conda activate openaidemo`
- install packages with `$ pip install -r requirements.txt` // NOT WORKING have to pip install, check why
- demo continued in openAIDemo1.ipynb
- Chat Completion API vs Completion API
    - Completion API: 1 prompt; models supporting have been depricated hence no code
    - Chat Completion API: Multiple prompts so u can have a convo
- Tokeniser: https://platform.openai.com/tokenizer
- charged according to #tokens and they use tokeniser to use this

## Function Calling in OpenAI
https://platform.openai.com/docs/guides/function-calling
- make an account on rapidAPI (unable to do so)
- basically a way to make ur LLM talk with a 3rd party API
- code isnt working so working here
    - define a function that calls this 3rd party API, take a note of these params
    - make a functions thing, make sure required has the params that is being called by ur 3rd party API function
    - pass it as an argument in completion code



