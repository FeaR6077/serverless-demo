import json
from user import get_user
from adduser import add_user

def hello(event, context):

    data = json.loads(event["body"])  
    userID = data["userId"]

    user = get_user(userID)

    #print(event["body"]["userID"]) #was ich in der console sehe
    body = {
        "message": user,
        "input": event
    }

    return body #was der client zurueckbekommt

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def handler2(event, context):

    data = json.loads(event["body"])  
    userID = data["userId"]
    userName = data["name"]

    add_user(userID, userName)

    response = {
        "statusCode": 200,
    }
    return response