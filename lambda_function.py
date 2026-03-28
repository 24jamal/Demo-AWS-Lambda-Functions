import json


def lambda_handler(event, context):
    # TODO implement
    result = calculate(1, 2)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
