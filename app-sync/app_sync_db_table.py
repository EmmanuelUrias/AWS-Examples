import boto3

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def create_table():
    try:
        table = dynamodb.create_table(
            TableName='Fruits',
            KeySchema=[
                {
                    'AttributeName': 'FruitID',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'FruitID',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName='Fruits')
        print("Table created successfully.")
        return table
    except Exception as e:
        print(f"Error creating table: {e}")

def insert_data():
    try:
        table = dynamodb.Table('Fruits')
        fruits = [
            {'FruitID': '1', 'Fruit': 'PineApple', 'Rating': 8},
            {'FruitID': '2', 'Fruit': 'Papaya', 'Rating': 3},
            {'FruitID': '3', 'Fruit': 'Orange', 'Rating': 8}
        ]
        for fruit in fruits:
            table.put_item(Item=fruit)
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")

def main():
    create_table()
    insert_data()

if __name__ == '__main__':
    main()
