import boto3


def get_user(user_id):
    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(TableName='julian-test',Item ={'userId':{'S':user_id}})
    
    