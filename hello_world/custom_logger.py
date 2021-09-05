import os
import logging
import logging.config
import yaml


class CustomLogger(logging.Filter):
    APP_NAME = 'SampleApp'
    __instance = None

    @staticmethod 
    def get_instance():
        if CustomLogger.__instance == None:
            CustomLogger()
        return CustomLogger.__instance

    def __init__(self):
        if CustomLogger.__instance != None:
            raise Exception("CustomLoggerクラス")
        else:
            CustomLogger.__instance = self
        
    def filter(self, record):
        record.ip = self.__ip
        return True


    def init_logger(self, ip):
        # TODO: IPアドレス等を変数で渡す
        log_config = yaml.load(open(os.path.join(os.getcwd(), "log_config.yml")).read(), Loader=yaml.FullLoader)
        logging.config.dictConfig(log_config)
        self.logger = logging.getLogger(self.APP_NAME)
        self.__ip = ip

        # self.logger.setLevel(logging.INFO)

        # filter = ContextFilter('12345')
        # self.logger.addFilter(filter)

        # handler = logging.StreamHandler()
        # handler.setLevel(logging.INFO)
        # formatter = logging.Formatter('%(asctime)-15s %(name)-5s %(levelname)-8s  %(message)s  - %(ip)s')
        # handler.setFormatter(formatter)
        # self.logger.addHandler(handler)


    def get_logger(self, name):
        logger = logging.getLogger(f'{self.APP_NAME}.{name}')
        logger.addFilter(self)
        return logger