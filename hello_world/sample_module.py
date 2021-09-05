import logging

from custom_logger import CustomLogger
# loggerの取得


# logの出力

class SampleModule:

    def __init__(self):
        self.logger = CustomLogger().get_logger(__name__)

    def some_method(self):
        self.logger.info('test')