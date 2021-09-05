import json
import logging
import sys
import os 
# sys.path.append(os.path.join(os.getcwd(), 'lib'))

# import requests

from custom_logger import CustomLogger
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

    ip_address = event['requestContext']['identity']['sourceIp']
    context = {
        'ip_address': ip_address
    }

    # loggerのinit
    custom_logger = CustomLogger.get_instance()
    custom_logger.init_logger(context)

    # sample_moduleの呼び出し
    SampleModule().some_method()


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
