import requests

# Define the API endpoint and the file to upload
api_url = "https://your-api-id.execute-api.your-region.amazonaws.com/dev/upload"
file_path = "/path/to/your/file.txt"

# Open the file in binary mode
with open(file_path, 'rb') as file:
    # Send a POST request with the file
    response = requests.post(api_url, files={'file': file})

# Print the response from the server
print(response.status_code)
print(response.text)
