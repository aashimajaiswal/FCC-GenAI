# Telegram Chat Bot
A bot that allows you to access ChatGPT via Telegram.
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