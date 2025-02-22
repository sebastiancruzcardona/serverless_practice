import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def hello_world(event, context):    
    return {
        "statusCode": 200,
        "body": "Hello World!"
    }