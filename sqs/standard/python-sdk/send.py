import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
sqs_client = boto3.client('sqs')

def send_message(queue_url, message_body, message_attributes=None):
    if not message_attributes:
        message_attributes = {}

    try:
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body,
            MessageAttributes=message_attributes
        )
        logger.info(f"Sent message: {message_body}")
        return response
    except ClientError as error:
        logger.exception(f"Send message failed: {message_body}")
        raise error

queue_url = 'https://sqs.us-east-1.amazonaws.com/099001967703/StandardQueue'
message_body = 'Hello World'
message_attributes = {
    "User": {
        "DataType": "String",
        "StringValue": "Emmanuel"
    }
}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    send_message(queue_url, message_body, message_attributes)
