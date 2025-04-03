import json
import boto3
import uuid  # Import UUID to generate unique userId

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('UsersTable')  # Ensure this matches your table name

        # Parse the incoming request body
        body = json.loads(event['body'])
        user_name = body['userName']
        user_email = body['userEmail']

        # Generate a unique userId
        user_id = str(uuid.uuid4())  

        # Store data in DynamoDB
        response = table.put_item(
            Item={
                'userId': user_id,  # Mandatory primary key
                'userName': user_name,
                'userEmail': user_email
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "User added successfully", "userId": user_id})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

