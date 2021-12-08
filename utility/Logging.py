import inspect
import logging


class Logging:

    def get_log(self):
        loggerName = inspect.stack()[1][3]  # To get the class name
        logger=logging.getLogger(loggerName)
        filehandler=logging.FileHandler('StaticWorkstation.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s :%(name)s: %(message)s ")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        return logger
