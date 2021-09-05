from custom_logger import CustomLogger

class SampleModule:

    def __init__(self):
        custom_logger = CustomLogger.get_instance()
        self.logger = custom_logger.get_logger(__name__)

    def some_method(self):
        self.logger.info('test')