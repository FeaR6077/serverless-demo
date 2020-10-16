import json
from user.user import *


def hello(event, context):

    data = json.loads(event["body"])  
    userID = data["userId"]

    user = User.get_user(userID)
    print(user)
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

    if User.get_user(userID) == False:
        User.add_user(userID, userName)
        body = {
        "message": "you added "+ user["name"] 
        }
    else:
        body = {
            "message": "ID already taken"
        }

    response = {
        "body": json.dumps(body),
        "statusCode": 200
    }
    return response

def handler3(event,context):

    data = json.loads(event["body"])  
    userID = data["userId"]
    User.delete_user(userID)


    body = {
        "message": "you deleted user"+ userID
    }
    
    return {"statusCode": 200, "body": json.dumps(body)}