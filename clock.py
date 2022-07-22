import logging
import logging.config

from apscheduler.schedulers.blocking import BlockingScheduler

import stack_overflow_page

logging.config.fileConfig('logging.conf')
schedule = BlockingScheduler()


@schedule.scheduled_job('interval', hours=3)
def access_stack_overflow_page():
    stack_overflow_page.login()



schedule.start()
