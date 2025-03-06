# OpenAI and Prompt Engineering Notes

Notes on theory and projects from 5:12:14 to 7:42:49.

## Introduction to OpenAI 
- Access via Open AI website > API Platform. Currently paid $5.
- No need to download models, model are ran on servers and accessed via API Keys.
- Documentation on the website has everything with code samples.
- tldr: Gave an overview of the Open AI API Platform.

## Generating OpenAI Key
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

## Telegram Bot using OpenAI
A bot that allows you to access ChatGPT via Telegram
- Flow diagram/ Architecture
    - User: Sends in a query to
    - Frontend (Telegram): passes it to
    - Backend (OpenAI): passes it to
    - LLM(some GPT model): Sends back a response to Backend -> Frontend -> User
- Steps
    1. Create environment in appropriate folder 
        - `$ conda create -n telebot python -y`, n flag: name, y flag: automatically says yes to installation
        - `$ conda  acitvate telebot`, use `conda init` if error using activate
    2. requirements.txt: aiogram is the telegram ai bot, use `$ pip install -r requirements.txt` to install packages, -r indicates requirements file that pip needs to install
        ```
        aiogram
        openai
        python-dotenv
        ```
    3. (optional) check if your connection to Frontend/ bot works
        - make a folder, here its connectToBot
        - .env file with OpenAI key and Telegram Bot key
            - telegram: go to BotFather on telegram -> /newbot in chat and do the steps } will give an API key
        - create an env for the bot
        - make sure u change ur env to bot when running the python file
        - install the requirements in this folder using pip
        - code in .py file, run using `$ python <relFilePath>`
        - note: executor has been moved to another version of aiogram so remove it in .py
        - Video has old code: refer Simple Usage from here https://docs.aiogram.dev/en/dev-3.x/
    4. `TelegramChatBot/main.py` is where the bot is } code has updated from the time video was made
    5. make sure to add .env for it to work
    6. Figure out how to make it work offline

## Finetuning of GPT-3 model for text classification
How to fine tune a model and make it personalised to yourself. Gave a high level overview. Look more in. In depth guide here: https://platform.openai.com/docs/guides/fine-tuning

## Whisper and DALLE Project
Done something similar in MSBA.

## Prompt Engineering
OpenAI do on prompt engineering: https://platform.openai.com/docs/guides/prompt-engineering
- Prompt is everything in LLM to get a useful answer
- Components of Prompt engineering
    - optimise prompts
    - perfect interactions between AI and humans
    - monitor prompts
    - maintain up to date prompts
- Best practices: be clear, create a persona, specify format, dont lead w answer, limit scope
- Types: Zero shot propmting (straight q, no examples to structure response), Few shot prompting (u give response examples)
- AI hallucination: when LLM gives false information.


    