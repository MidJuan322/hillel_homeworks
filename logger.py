import logging


class LoggerClass:

    def __init__(self):
        self.logger = logging.getLogger("LOGGER")
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s ')

        self.fh = logging.FileHandler("event_log.log")
        self.fh.setLevel(logging.INFO)
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
