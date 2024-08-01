import boto3
import json

sfn_client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    # Extract bucket name and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Start the Step Function execution
    response = sfn_client.start_execution(
        stateMachineArn = 'arn:aws:states:us-east-1:xxxxxxxx:stateMachine:MyStateMachine',
        input=json.dumps({'bucket': bucket, 'key': key}))
    
    return response
