import os
import logging
import logging.config
import yaml

from context_filter import ContextFilter

# TODO シングルトンにする
class CustomLogger():
    APP_NAME = 'SampleApp'

    def __init__(self):
        pass

    def init_logger(self):
        # TODO: IPアドレス等を変数で渡す
        # TODO: Loaderのdepratedeの修正
        # TODO: moduleのパスの変更
        logging.config.dictConfig(yaml.load(open(os.path.join(os.getcwd(), "log_config.yml")).read()))
        self.logger = logging.getLogger(self.APP_NAME)

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
        filter = ContextFilter('123456')
        logger.addFilter(filter)
        return logger