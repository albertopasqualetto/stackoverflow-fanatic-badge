# Earn the Fanatic Badge on Stack Overflow

A Python script deployed to Heroku that performs automatic logins on stackoverflow.com on a regular basis, so that you can earn the **Fanatic** badge, effortlessly.

[Fanatic Badge](https://stackoverflow.com/help/badges/83/fanatic)
> Visit the site each day for 100 consecutive days. (Days are counted in UTC.).

Moreover, you get notified, via telegram when the script runs.

ℹ️ To count as a visit, besides the login, the script also accesses your profile page: https://meta.stackoverflow.com/a/298532.


## How to use

1. Make sure you have the following dependencies:

    - Python 3.6+ (along with pip)

    - Chrome installed (or another browser of choice, though you will have to edit the script)

    - Python packages: use `pip install -r requirements.txt` to get them

2. Edit `.env` to include your data.

    - WARNING: don't push this to a public repository!

3. Run `python3 main.py` to see the script work.

4. If you want to be notified by email add in your `.env` file the Telegram bot token and the chat id. You can get the token from the [BotFather](https://t.me/BotFather) and the chat id from the [userinfobot](https://t.me/userinfobot).

5. To schedule the script use `crontab` or something similar and schedule it to run every day.


## Troubleshooting

The script can trigger a CAPTCHA from StackOverflow. A human has to resolve this.

StackOverflow sometimes changes their UI, so that the old CSS identifiers don't match anymore. This can cause one of lines in `stack_overflow_page.py` which contain `By.ID` to fail. To debug this in Chrome, look for the correct identifier to use instead using the "inspect element" feature in developer tools (Ctrl+Shift+C).

## Credits
[Here](https://medium.com/coders-do-read/earn-the-fanatic-badge-on-stack-overflow-828d2c46930) and [here](https://medium.com/coders-do-read/fanatic-badge-on-stack-overflow-part-two-email-notification-820f5394f8f0) you can find a step-by-step guide on how to set up the original script.

I removed the email notification and added the telegram notification.