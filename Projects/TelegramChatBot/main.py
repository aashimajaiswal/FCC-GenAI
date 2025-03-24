from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
import openai
import sys
import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.filters import Command
import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAPI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class Reference:
    '''
    A class to store previously response from the openai API
    '''
    def __init__(self) -> None:
        self.response = ""

# init reference
reference = Reference()
model_name = "gpt-4"

# Bot token can be obtained via https://t.me/BotFather
# see why getenv was not working
# TOKEN = ""
# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

def clear_past():
    """A function to clear the previous conversation and context.
    """
    reference.response = ""

@dp.message(Command('clear'))
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hi {html.bold(message.from_user.full_name)}!")

@dp.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command
    """
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm Telegram bot created by Aashima! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps :)
    """
    await message.answer(help_command)

@dp.message()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using OpenAI API.
    """
    print(f">>> USER: \n\t{message.text}")

    try:
        response = openai.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "assistant", "content": reference.response},
                {"role": "user", "content": message.text},
            ]
        )
        reference.response = response.choices[0].message.content

        print(f">>> chatGPT: \n\t{reference.response}")
        await message.answer(reference.response)

    except openai.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        await message.answer("An error occurred while processing your request. Please try again later.")



async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())