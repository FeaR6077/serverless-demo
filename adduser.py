import boto3

def add_user(user_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('julian-test')
    response = table.put_item(Item={'userId': user_id})