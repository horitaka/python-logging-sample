import logging
from random import choice

# TODO シングルトンにする
class ContextFilter(logging.Filter):

    USERS = ['jim', 'fred', 'sheila']
    IPS = ['123.231.231.123', '127.0.0.1', '192.168.0.1']

    def __init__(self, context):
        self._ip = context

    def filter(self, record):
        record.ip = self._ip
        return True