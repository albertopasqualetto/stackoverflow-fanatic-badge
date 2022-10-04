import os

from dotenv import load_dotenv

import logging
import logging.config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

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

    driver = webdriver.Chrome(ChromeDriverManager().install())

	success = False

	try:
		driver.get("https://stackoverflow.com")

		driver.find_element(By.LINK_TEXT, "Log in").click()

		driver.find_element(By.ID, "email").send_keys(email)
		driver.find_element(By.ID, "password").send_keys(password)
		driver.find_element(By.ID, "submit-button").submit()

		driver.find_element(By.PARTIAL_LINK_TEXT, display_name).click()

		elem = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.ID, "js-daily-access-calendar-container"))
		)

		success = True
		logging.info("Logged into stackoverflow.com and accessed profile page - " + elem.text)

	except Exception as e:
		success = False
		message = "An error occurred while trying to access stackoverflow.com!"
		logging.error(message, e)

    finally:
        driver.close()

	return success


if __name__ == "__main__":
	login()
