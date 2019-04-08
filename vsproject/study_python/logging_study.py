import logging
import time
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler
 
fname = "sms_polling"
#logHandler1 = TimedRotatingFileHandler(fname, when="s")
logHandler = RotatingFileHandler(filename=fname, maxBytes=1000, backupCount=500)
logFormatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
logHandler.setFormatter(logFormatter)
logger = logging.getLogger(__name__)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

for i in range(1000):
    logger.info("start log ")
    time.sleep(0.1)
