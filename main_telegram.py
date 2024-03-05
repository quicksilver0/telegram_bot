from aiogram import F
import asyncio
from aiogram.types import Message
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import json
import requests


url = 'url_to_webapp'
token = 'your_telegram_token'

bot = Bot(token)
dp = Dispatcher()

# handler on command /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Greetings, I'm HSBC Bank's virtual assistant, here to help with any questions you may have about our services.\nFeel free to reach out—I'm here to assist you.")

@dp.message(F.text)
async def receive_prompt(message: Message):
	prompt = message.text
	jsonData={'message': prompt}
	jsonResponse = requests.post(
	  	url+'/send_message',
  		json=json.dumps(jsonData)
	)
	response = jsonResponse.json()
	await message.answer(response['message'])


# start of polling for new messages
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())