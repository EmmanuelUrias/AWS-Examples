import json
import sys
import os

# Get the path of the parent directory
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to sys.path
sys.path.insert(0, parent_directory)

# Now you can import your module
import file_processor

# Load the event
with open('event.json') as f:
    event = json.load(f)

# Create a dummy context
class Context:
    def __init__(self):
        self.function_name = "test_function"
        self.memory_limit_in_mb = "128"
        self.invoked_function_arn = "arn:aws:lambda:us-east-1:123456789012:function:test_function"
        self.aws_request_id = "1234567890"

context = Context()

# Invoke the lambda function
response = file_processor.lambda_handler(event, context)
print(response)
