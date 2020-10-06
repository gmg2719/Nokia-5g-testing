import logging


def test_loggingDemo(self):
        logger = logging.getLogger(__name__)



        fileHandler = logging.FileHandler('logfile.log')

        logger.addHandler(fileHandler)  # filehandler object


        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)



        logger.setLevel(logging.debug)
        logger.debug("A debug statement is executed")
        logger.info("Information statement")
        logger.debug("A debug statement is executed")
        logger.warning("Something is in warning mode")
        logger.error("A Major error has happend")
        logger.critical("Critical issue")
        return logger
