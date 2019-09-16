import  logging

class loggerdemo():

    def testlog(self):
        #creating logger
        logger = logging.getLogger('sample.log')
        #logger = logging.getLogger(loggerdemo.__name__)              displays the classname in log
        logger.setLevel(logging.INFO)

        #creating console handler
        consolehandler = logging.StreamHandler()
        consolehandler.setLevel(logging.INFO)

        #creating formatter
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S %p')
        consolehandler.setFormatter(formatter)

        #adding consolehandler to logger
        logger.addHandler(consolehandler)

        #log message
        logging.critical("boss, ignore others")
        logging.warning("check")
        logging.info("check info")
        logging.debug("check debug")
        logging.error("check error")

l = loggerdemo()
l.testlog()




