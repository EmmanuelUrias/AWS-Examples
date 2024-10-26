import boto3
import json
import time

# Initialize the CloudWatch Logs client
client = boto3.client('logs', region_name='us-east-1')

# CloudWatch Logs group and stream details
log_group_name = '/example/basic/app'
log_stream_name = '1729887685'

# Load logs from a JSON file
def load_logs_from_file(file_path):
    with open(file_path, 'r') as log_file:
        return json.load(log_file)

# Create the log stream if it doesn't already exist
def create_log_stream():
    try:
        client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
    except client.exceptions.ResourceAlreadyExistsException:
        pass  # Log stream already exists, continue

# Get the next sequence token for the log stream
def get_sequence_token():
    response = client.describe_log_streams(logGroupName=log_group_name, logStreamNamePrefix=log_stream_name)
    for log_stream in response['logStreams']:
        if log_stream['logStreamName'] == log_stream_name:
            return log_stream.get('uploadSequenceToken')
    return None

# Put the log events into CloudWatch Logs
def put_log_event(log_entry, sequence_token=None):
    # Convert timestamp to milliseconds since Unix epoch
    timestamp = int(time.mktime(time.strptime(log_entry['timestamp'], "%Y-%m-%d %H:%M:%S +0000")) * 1000)

    # Create the log event payload
    log_event = {
        'logGroupName': log_group_name,
        'logStreamName': log_stream_name,
        'logEvents': [
            {
                'timestamp': timestamp,
                'message': json.dumps(log_entry)
            }
        ]
    }

    if sequence_token:
        log_event['sequenceToken'] = sequence_token

    # Send the log event to CloudWatch Logs
    if sequence_token:
        response = client.put_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            logEvents=log_event['logEvents'],
            sequenceToken=sequence_token
        )
    else:
        response = client.put_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            logEvents=log_event['logEvents']
        )
    return response

# Main function to send logs one by one
def main():
    create_log_stream()
    sequence_token = get_sequence_token()

    # Load logs from the specified file
    logs = load_logs_from_file('events.json')

    for log_entry in logs['logs']:
        try:
            response = put_log_event(log_entry, sequence_token)
            # Update the sequence token for the next event
            sequence_token = response['nextSequenceToken']
        except client.exceptions.InvalidSequenceTokenException as e:
            # If sequence token is invalid, retrieve the correct one and retry
            sequence_token = e.response['expectedSequenceToken']
            response = put_log_event(log_entry, sequence_token)
            sequence_token = response['nextSequenceToken']

if __name__ == "__main__":
    main()