import boto3

class User:

    def get_user(user_id):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('julian-test')
        response = table.get_item(Key={'userId': user_id})
        try:
            return response["Item"]
        except:
            return False
            
    def get_user(user_id):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('julian-test')
        response = table.get_item(Key={'userId': user_id})
        try:
            return response["Item"]
        except:
            return False

    def add_user(user_id, user_name):
        dynamodb = boto3.client('dynamodb')
        dynamodb.put_item(TableName='julian-test', Item={'userId':{"S": user_id},'name':{"S": user_name}})
        print("Worked")