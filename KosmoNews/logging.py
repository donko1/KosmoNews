
from django.conf import settings
import logging
import datetime

def log(message):
    if settings.DEBUG:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_time} - {message}"
        logging.basicConfig(filename='log.log', level=logging.INFO)
        logging.info(log_message)
    else:
        pass