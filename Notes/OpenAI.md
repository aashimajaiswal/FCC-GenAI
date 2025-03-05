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
- install packages with `$ pip install -r requirements.txt`


