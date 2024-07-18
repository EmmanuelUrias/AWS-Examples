import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
sqs_client = boto3.client('sqs')

def receive_message(queue_url, attribute_names=['All'], message_attribute_names=['All'], max_number_of_messages=10):
    try:
        response = sqs_client.receive_message(
            QueueUrl=queue_url,
            AttributeNames=attribute_names,
            MessageAttributeNames=message_attribute_names,
            MaxNumberOfMessages=max_number_of_messages
        )
        print(response['Messages'][0]['Body'])
        return 
    except ClientError as error:
        logger.exception(f"Recieve message failed")
        raise error

queue_url = 'https://sqs.us-east-1.amazonaws.com/099001967703/StandardQueue'

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    receive_message(queue_url)
