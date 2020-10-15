import boto3

def delete_user(user_id):
    dynamodb = boto3.client('dynamodb')
    dynamodb.delete_item(TableName='julian-test',Key={'userId':{"S": user_id}})