import os

from dotenv import load_dotenv

import logging
import logging.config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

load_dotenv()

logging.config.fileConfig('logging.conf')


def login():
	logging.info("Logging into stackoverflow.com")

	email = os.environ.get('STACK_OVERFLOW_EMAIL')
	password = os.environ.get('STACK_OVERFLOW_PASSWORD')
	display_name = os.environ.get('STACK_OVERFLOW_DISPLAY_NAME')

	if None in (email, password, display_name):
		print(email, password, display_name)
		logging.error("Set 'STACK_OVERFLOW_EMAIL' 'STACK_OVERFLOW_PASSWORD' 'STACK_OVERFLOW_DISPLAY_NAME' env variables to successfully log into Stack Overflow for " + email + ", " + display_name)
		return

	driver = webdriver.Chrome(options=chrome_options)
	# driver = webdriver.Remote(
	# 			command_executor='http://localhost:4444/wd/hub',
	# 			options=chrome_options
	# 		)

	stealth(driver,
		 languages=["en-US", "en"],
		 vendor="Google Inc.",
		 platform="Win32",
		 webgl_vendor="Intel Inc.",
		 renderer="Intel Iris OpenGL Engine",
		 fix_hairline=True
		 )

	success = False
	consecutive_days = 0

	try:
		driver.get("https://stackoverflow.com")

		driver.find_element(By.LINK_TEXT, "Log in").click()

		driver.find_element(By.ID, "email").send_keys(email)
		driver.find_element(By.ID, "password").send_keys(password)
		driver.find_element(By.ID, "submit-button").submit()

		account_link = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, display_name))
		)
		account_link.click()

		cal = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "js-daily-access-calendar-container"))
		)

		success = True
		consecutive_days = int(cal.text.split(", ")[1].strip().split(" ")[0])
		logging.info("Logged into stackoverflow.com and accessed profile page - " + str(consecutive_days) + " consecutive days")

	except Exception as e:
		success = False
		message = "An error occurred while trying to access stackoverflow.com!"
		logging.error(message, e)

	finally:
		driver.close()

	return success, consecutive_days		# this is a tuple


if __name__ == "__main__":
	login()
