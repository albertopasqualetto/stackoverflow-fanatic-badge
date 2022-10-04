from dotenv import load_dotenv

import logging
import logging.config

from datetime import datetime, timedelta

load_dotenv()

logging.config.fileConfig('logging.conf')

from stack_overflow_page import login
from stack_exchange_api import fetch_me_last_access
from tg_send import send


def main():
	success = login()

	last_access = fetch_me_last_access()
	if not success or datetime.now() - timedelta(days=1) > datetime.fromtimestamp(last_access):
		send("You haven't accessed Stack Overflow in the last 24 hours!\nLast login: " + str(datetime.fromtimestamp(last_access)), "Success:" + str(success))
	else:
		send("You've accessed Stack Overflow in the last 24 hours!\nLast login: " + str(datetime.fromtimestamp(last_access)), notification=False)

	logging.info("Done!")


if __name__ == "__main__":
	main()
