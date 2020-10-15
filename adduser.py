import boto3

def add_user(user_id, user_name):
    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(TableName='julian-test', Item={'userId':{"S": user_id},'name':{"S": user_name}})