from custom_logger import CustomLogger

class SampleModule:

    def __init__(self):
        self.logger = CustomLogger().get_logger(__name__)

    def some_method(self):
        self.logger.info('test')