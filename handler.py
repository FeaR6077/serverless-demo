import json
from serverless-demo.user import get_user


def hello(event, context):

    data = json.loads(event["body"])  
    userID = data["userId"]  


    print(userID)
    #print(event["body"]["userID"]) #was ich in der console sehe
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response #was der client zurueckbekommt

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
