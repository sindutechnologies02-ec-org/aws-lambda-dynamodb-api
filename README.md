i# AWS Lambda with DynamoDB
#project Overview
This project demonstrates how to build a **serverless REST API** using:
✅ AWS Lambda  
✅ API Gateway  
✅ DynamoDB  
✅ Python (boto3)  

## 🚀 Features
- Handles user data storage using DynamoDB
- Serverless architecture reduces costs
- Uses IAM roles for secure access  

## 🛠️ Technologies Used
- AWS Lambda  
- AWS API Gateway  
- DynamoDB  
- Python (boto3, uuid)  

## 🔧 Setup & Deployment
1️⃣ Clone this repository  
```bash
git clone https://https://github.com/sindutechnologies02-ec-org/aws-lambda-dynamodb-api.git
2️⃣ Install dependencies
pip install boto3
3️⃣ Deploy using AWS Lambda
POST /users - Add user to DynamoDB
Example request:
curl -X POST "https://xyz1234.execute-api.us-east-1.amazonaws.com/dev/users" \
     -H "Content-Type: application/json" \
     -d '{"userName": "John Doe", "userEmail": "john@example.com"}'
Expected Output:
{
    "statusCode": 200,
    "body": "{\"message\": \"User added successfully\", \"userId\": \"some-unique-id\"}"
}

