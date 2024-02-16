import os

from dotenv import load_dotenv
load_dotenv()

import logging
import logging.config

import telegram
import asyncio


logging.config.fileConfig('logging.conf')

test_msg = '*test*'


async def send(msg, chat_id=os.environ.get('TG_USER_ID'), token=os.environ.get('TG_BOT_TOKEN'), notification=True):
	"""
	Send a message to a telegram user specified on chatId
	chat_id must be a number!
	"""
	logging.info("Sending message to " + chat_id)
	bot = telegram.Bot(token=token)
	async with bot:
		await bot.send_message(chat_id=chat_id, text=msg, disable_notification=(not notification), parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)


if __name__ == '__main__':
	asyncio.run(send(test_msg))
