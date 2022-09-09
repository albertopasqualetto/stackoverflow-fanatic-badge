import os

from dotenv import load_dotenv
load_dotenv()

import logging
import logging.config

import telegram


logging.config.fileConfig('logging.conf')

test_msg='test'


def send(msg, chat_id=os.environ.get('TG_USER_ID'), token=os.environ.get('TG_BOT_TOKEN')):
	"""
	Send a mensage to a telegram user specified on chatId
	chat_id must be a number!
	"""
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)


if __name__ == '__main__':
	send(test_msg)