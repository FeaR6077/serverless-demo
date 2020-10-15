import json
from user import get_user
from adduser import add_user
from deleteuser import delete_user


def hello(event, context):

    data = json.loads(event["body"])  
    userID = data["userId"]

    user = get_user(userID)

    #print(event["body"]["userID"]) #was ich in der console sehe
    
    body = {
        "message": "you found "+ user["name"] 
    }
    return {"statusCode": 200, "body": json.dumps(body)}
     #was der client zurueckbekommt

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

    body = {
        "message": "you added " +userName 
    }

    response = {
        "body": json.dumps(body),
        "statusCode": 200
    }
    return response

def handler3(event,context):
    data = json.loads(event["body"])  
    userID = data["userId"]
    delete_user(userID)

    body = {
        "message": "you deleted user"+ userID
    }
    
    return {"statusCode": 200, "body": json.dumps(body)}