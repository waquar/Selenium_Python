import logging
# if you call highest level first it will ignore all others.
#levels:
#debug (least)
#info
#warning
#error
#critical(highest)

logging.basicConfig(filename="test.log", level = logging.CRITICAL)

logging.critical("boss, ignore others")
logging.warning("check")
logging.info("check info")
logging.debug("check debug")
logging.error("check error")


