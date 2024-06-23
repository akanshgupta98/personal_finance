import logging
from personal_finance.settings import LOGGING


class Logger:
    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)

    def Info(self, msg: str):
        self.logger.info(msg)

    def Debug(self, msg: str):
        self.logger.debug(msg)

    def Error(self, msg: str):
        self.logger.error(msg)
