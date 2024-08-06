import boto3

# Create the DynamoDB client
dynamo = boto3.client('dynamodb')

# Create the table
resp = dynamo.create_table(
    TableName='Books',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Partition Key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
    ],
    BillingMode='PAY_PER_REQUEST',
    TableClass='STANDARD'
)

print('Table creation response:')
print(resp)

# Wait until the table exists.
dynamo.get_waiter('table_exists').wait(TableName='Books')

# Insert items into the table
table = boto3.resource('dynamodb').Table('Books')

items = [
    {'id': 1, 'title': 'Book 1', 'year': 2021},
    {'id': 2, 'title': 'Book 2', 'year': 2022},
    {'id': 3, 'title': 'Book 3', 'year': 2023}
]

for item in items:
    table.put_item(Item=item)

print('Items inserted into the table.')
