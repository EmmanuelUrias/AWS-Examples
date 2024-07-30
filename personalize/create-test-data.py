import csv
import random
from datetime import datetime, timedelta

# Function to generate a random timestamp
def generate_random_timestamp(start, end):
    return int((start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))).timestamp())

# Define the CSV file path
csv_file_path = 'interactions.csv'

# Define the header based on the schema
header = ['USER_ID', 'ITEM_ID', 'TIMESTAMP', 'EVENT_TYPE', 'EVENT_VALUE']

# Define some sample data
user_ids = [f'user_{i}' for i in range(1, 100)]
item_ids = [f'item_{i}' for i in range(1, 100)]
event_types = ['click', 'purchase', 'like', 'view']
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 7, 7)

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(header)
    
    # Write 100 rows of data
    for _ in range(1000):
        user_id = random.choice(user_ids)
        item_id = random.choice(item_ids)
        timestamp = generate_random_timestamp(start_date, end_date)
        event_type = random.choice(event_types)
        event_value = round(random.uniform(1, 100), 2)
        writer.writerow([user_id, item_id, timestamp, event_type, event_value])

print(f'CSV file "{csv_file_path}" with 1000 items created successfully.')
