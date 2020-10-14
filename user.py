import boto3


def get_user(user_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('julian-test')
    response = table.get_item(Key={'userId': "1234"})
    item = response['Item']
    return item
    })