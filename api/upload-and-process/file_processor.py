import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Process the file (e.g., read its content)
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    file_content = response['Body'].read().decode('utf-8')
    
    # Example processing: Print file content (or do other processing)
    print(file_content)

    ## Add a sns to the clouformation template and connect to it here to recieve notifications that will trigger this function
    ## See if we can upload the processed file as a new object with a processed tag, and make unproccessed files unprocessed tag

    return {
        'statusCode': 200,
        'body': f'File {object_key} processed successfully!'
    }
