import json
import logging
import sys
import os 
sys.path.append(os.path.join(os.getcwd(), 'lib'))

# import requests

import custom_logger
from sample_module import SampleModule

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    # print('---------event--------')
    # print(event)
    # print('---------context--------')
    # print(context)

    # loggerのinit
    logger = custom_logger.CustomLogger()
    logger.init_logger()

    # logger.get_logger('test').info('aaaaa')

    # sample_moduleの呼び出し
    SampleModule().some_method()

    # TODO: シーケンス図直し


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
