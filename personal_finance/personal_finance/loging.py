import logging
from personal_finance.settings import LOGGING


def get_logger(name):
    """Get Logger object"""
    return Logger(name)


class Logger:
    """Singleton Class for Logging"""

    def __new__(cls, logger_name):
        if not hasattr(cls, "instance"):
            cls.instance = super(Logger, cls).__new__(cls)

        return cls.instance

    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)

    def Info(self, msg: str):
        self.logger.info(msg)

    def Debug(self, msg: str):
        self.logger.debug(msg)

    def Error(self, msg: str):
        self.logger.error(msg)
