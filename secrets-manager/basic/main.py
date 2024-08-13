import boto3
import json

sm = boto3.client('secretsmanager')

def get_secret():
    secrets = sm.list_secrets()

    print(secrets)

    # Get the ARN of the first secret in the list
    secret_id = secrets['SecretList'][1]['ARN']

    # Retrieve the secret value
    resp = sm.get_secret_value(
        SecretId=secret_id
    )

    # Parse the JSON string from the secret
    secret_string = resp.get('SecretString')
    secret_dict = json.loads(secret_string)  # Convert JSON string to dictionary

    # Extract username and password
    username = secret_dict.get('username')
    password = secret_dict.get('password')

    # Print or use the username and password
    print(f"Username: {username}")
    print(f"Password: {password}")

    return username, password

# Run the function
get_secret()