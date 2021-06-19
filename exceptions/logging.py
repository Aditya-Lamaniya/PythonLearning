from logging import *

logging.basicConfig(filename=" mylog.log",level=logging.ERROR)
logging.critical("critical")
logging.error("error")
logging.warn("warning")
logging.info("info")
logging.debug("debug")
