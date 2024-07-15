import boto3
import botocore
from botocore.config import Config
import time
import requests
from requests_aws4auth import AWS4Auth

# Build the client using the default credential configuration.
# You can use the CLI and run 'aws configure' to set access key, secret
# key, and default region.

my_config = Config(
    # Optionally lets you specify a region other than your default.
    region_name='us-east-1'
)

client = boto3.client('opensearch', config=my_config)

domainName = 'practice-domain'  # The name of the domain

def deleteDomain(client, domainName):
    """Deletes an OpenSearch Service domain. Deleting a domain can take several minutes."""
    try:
        response = client.delete_domain(
            DomainName=domainName
        )
        print('Sending domain deletion request...')
        print(response)

    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'ResourceNotFoundException':
            print('Domain not found. Please check the domain name.')
        else:
            raise error


def waitForDomainProcessing(client, domainName):
    """Waits for the domain to finish processing changes."""
    try:
        response = client.describe_domain(
            DomainName=domainName 
        )
        # Every 15 seconds, check whether the domain is processing.
        while response["DomainStatus"]["Processing"] == True:
            print('Domain still processing...')
            time.sleep(15)
            response = client.describe_domain(
                DomainName=domainName)

        # Once we exit the loop, the domain is available.
        print('Amazon OpenSearch Service has finished processing changes for your domain.')
        print('Domain description:')
        print(response)

    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'ResourceNotFoundException':
            print('Domain not found. Please check the domain name.')
        else:
            raise error
        
def createGetAndDeleteIndex():
    host = 'https://search-practice-domain-6cryrnuujnx6x2x7xn3knaf3uu.us-east-1.es.amazonaws.com'
    index_name = 'new-index'
    url = f'{host}/{index_name}'
    headers = {"Content-Type": "application/json"}

    index_body = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
                "field1": {
                    "type": "text"
                },
                "field2": {
                    "type": "keyword"
                }
            }
        }
    }

   # Use boto3 to get AWS credentials
    session = boto3.Session()
    credentials = session.get_credentials()
    region = 'us-east-1'

    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, 'es', session_token=credentials.token)

    # Make the request to create the index
    response = requests.put(url, auth=awsauth, json=index_body, headers=headers)

    # Print the response from OpenSearch
    print(response.status_code)
    print(response.text)
    
    # Get the index
    response = requests.get(url, auth=awsauth, headers=headers)
    
    # Print the response from OpenSearch
    print("Get Index Response:")
    print(response.status_code)
    print(response.text)
    

    response = requests.delete(url, auth=awsauth, headers=headers)
    
    # Print the response from OpenSearch
    print("Delete Index Response:")
    print(response.status_code)
    print(response.text)


if __name__== "__main__":
    # createGetAndDeleteIndex()
    waitForDomainProcessing(client, domainName)
    # deleteDomain(client, domainName)