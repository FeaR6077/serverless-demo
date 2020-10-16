import boto3
from user import get_user


def add_user(user_id, user_name):
    dynamodb = boto3.client('dynamodb')
    
    if get_user(user_id):
        print("hola")
    else:
        dynamodb.put_item(TableName='julian-test', Item={'userId':{"S": user_id},'name':{"S": user_name}})
        print("Worked")