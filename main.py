from dotenv import load_dotenv

import logging
import logging.config

from datetime import datetime, timedelta

load_dotenv()

logging.config.fileConfig('logging.conf')

from stack_overflow_page import login
from stack_exchange_api import fetch_me_last_access
from tg_send import send

import time


def main(tries=0):
	log_return = login()

	last_access = fetch_me_last_access()
	if datetime.now() - timedelta(days=1) > datetime.fromtimestamp(last_access):
		logging.error("Last access was more than 24 hours ago, retrying... Tries: " + str(tries))
		if tries < 10:
			time.sleep(100)
			main(tries + 1)
		else:
			logging.error("Tried to login 10 times and failed!")
			send("*Tried to login 10 times and failed!*\nYou have *NOT* accessed Stack Overflow in the last 24 hours!\nLast login: " + str(datetime.fromtimestamp(last_access)) + "\nSuccess: " + str(log_return[0]))
	elif not log_return[0]:
		logging.error("Failed to login, retrying... Tries: " + str(tries))
		if tries < 10:
			time.sleep(100)
			main(tries + 1)
		else:
			logging.error("Tried to login 10 times and failed but last access was less than 24 hours ago!")
			send("*Tried to login 10 times and failed!*\nYou have *NOT* accessed Stack Overflow *now*!" + "\nSuccess: " + str(log_return[0]) + "\nLast login: " + str(datetime.fromtimestamp(last_access)) + "\nTries: " + str(tries))
	elif log_return[1] < 100 or log_return[1] % 30 == 0:
		send("You have accessed Stack Overflow in the last 24 hours!\nConsecutive days: " + str(log_return[1]) + "\nLast login: " + str(datetime.fromtimestamp(last_access)) + "\nSuccess: " + str(log_return[0]), notification=False)
	elif log_return[1] == 100:
		send("\U0001F389 You have accessed Stack Overflow for 100 consecutive days! \U0001F973", notification=True)

	logging.info("Done!")


if __name__ == "__main__":
	main()
