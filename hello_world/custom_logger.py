import os
import logging
import logging.config
import yaml
import json

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
        record.ip_address = self.__ip_address
        return True


    def init_logger(self, context):
        self.__ip_address = context['ip_address']

        # log_config = yaml.load(open(os.path.join(os.getcwd(), "log_config.yml")).read(), Loader=yaml.FullLoader)
        # logging.config.dictConfig(log_config)
        # self.logger = logging.getLogger(self.APP_NAME)

        self.logger = logging.getLogger(self.APP_NAME)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)

        # TODO: 時刻のフォーマットのカンマを直す
        # TODO: useridなどを追加する
        format = {
            'timestamp': '%(asctime)s',
            'file': '%(name)s',
            'level': '%(levelname)s',
            'message': '%(message)s',
            'ip_adderess': '%(ip_address)s'
        }
        formatter = logging.Formatter(json.dumps(format, ensure_ascii=False))
        handler.setFormatter(formatter)


    def get_logger(self, name):
        logger = logging.getLogger(f'{self.APP_NAME}.{name}')
        logger.addFilter(self)
        return logger