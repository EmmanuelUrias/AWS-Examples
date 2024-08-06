from pymongo import MongoClient

# Replace these values with your actual connection details
username = 'emmanuel'
password = 'emmanuel'
cluster_endpoint = 'my-docdb-cluster-099001967703.us-east-1.docdb-elastic.amazonaws.com:27017'

# Create a connection to the DocumentDB cluster
client = MongoClient(
    f'mongodb://{username}:{password}@{cluster_endpoint}/?ssl=true&tls=true&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false'
)

# Access a database (will be created if it doesn't exist)
db = client['my_database']

# Access a collection within the database (will be created if it doesn't exist)
collection = db['my_collection']

# Insert sample data into the collection
sample_data = [
    {"name": "John Doe", "age": 29, "email": "john.doe@example.com"},
    {"name": "Jane Doe", "age": 25, "email": "jane.doe@example.com"},
    {"name": "Alice", "age": 32, "email": "alice@example.com"}
]

# Insert the sample data into the collection
result = collection.insert_many(sample_data)

# Print the IDs of the inserted documents
print("Inserted document IDs:", result.inserted_ids)

# Verify the insertion by retrieving and printing the data
for doc in collection.find():
    print(doc)
