import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S %p',filename="test.log", level = logging.DEBUG)

logging.warning("warning message")
