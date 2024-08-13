import boto3

sm = boto3.client('secretsmanager')

secret_id = ''

def get_secret():
    resp = sm.get_secret_value(
        SecretId=secret_id
    )

    print(resp)