import os

from dotenv import load_dotenv
load_dotenv()

import logging
import logging.config

from requests_oauthlib import OAuth2Session

from stackapi import StackAPI

logging.config.fileConfig('logging.conf')

def get_authorization_url():
	client_id = os.environ.get('STACK_EXCHANGE_CLIENT_ID')
	if client_id is None:
		logging.warning("Set 'STACK_EXCHANGE_CLIENT_ID' env variable to obtain the authorization URL")
		return None

	oauth = OAuth2Session(client_id, redirect_uri='https://stackexchange.com/oauth/login_success', scope='no_expiry')
	authorization_url, state = oauth.authorization_url('https://stackexchange.com/oauth/dialog')

	logging.info("Access the following URL to obtain the access token: %s", authorization_url)

	return authorization_url


def fetch_me_last_access(my_key=os.environ.get('STACK_EXCHANGE_KEY'), my_access_token=os.environ.get('STACK_EXCHANGE_ACCESS_TOKEN')):
	"""
	Fetches the user info
	"""
	SITE = StackAPI('stackoverflow', key=my_key, access_token=my_access_token)
	logging.info("Getting user's last access date")
	return SITE.fetch('me')['items'][0]['last_access_date']


if __name__ == '__main__':
	#get_authorization_url()
	print(fetch_me_last_access())
