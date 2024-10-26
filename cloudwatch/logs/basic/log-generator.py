import random
import json
from datetime import datetime, timedelta

number_of_entries = 100

# Generate a random IP address
def generate_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

# Generate a random user agent
def generate_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(user_agents)

# Generate a random HTTP method
def generate_method():
    return random.choice(["GET", "POST", "DELETE", "PUT"])

# Generate a random HTTP status code
def generate_status():
    return random.choice([200, 201, 301, 302, 404, 500])

# Generate a random request path
def generate_path():
    paths = [
        "/home",
        "/about",
        "/contact",
        "/products",
        "/products/item",
        "/login",
        "/signup"
    ]
    return random.choice(paths)

# Generate a random timestamp
def generate_timestamp(last_time):
    # Increase time by a random number of minutes (for example, between 1 and 10)
    increment = random.randint(1, 10)
    last_time += timedelta(minutes=increment)
    return last_time, last_time.strftime("%Y-%m-%d %H:%M:%S +0000")

# Generate a random user identifier
def generate_user_identifier():
    user_identifiers = ["user123", "guest456", "admin789", "john_doe", "jane_smith"]
    return random.choice(user_identifiers)

# Generate the log entry in JSON format
def generate_log_entry(last_time):
    ip = generate_ip()
    user_identifier = generate_user_identifier()  # Generate realistic user identifier
    user_id = "-"  # Common placeholder for missing data
    last_time, timestamp = generate_timestamp(last_time)
    method = generate_method()
    path = generate_path()
    protocol = "HTTP/1.1"
    status = generate_status()
    bytes_transferred = random.randint(500, 5000)
    referrer = "-"  # Common placeholder for missing data
    user_agent = generate_user_agent()

    log_entry = {
        "ip": ip,
        "user_identifier": user_identifier,
        "user_id": user_id,
        "timestamp": timestamp,
        "method": method,
        "path": path,
        "protocol": protocol,
        "status": status,
        "bytes_transferred": bytes_transferred,
        "referrer": referrer,
        "user_agent": user_agent
    }
    return last_time, log_entry

# Write the log entries directly to a file
def generate_log_file(file_name, num_entries=100):
    last_time = datetime.now() - timedelta(minutes=1000)
    log_entries = []
    for _ in range(num_entries):
        last_time, log_entry = generate_log_entry(last_time)
        log_entries.append(log_entry)
    
    with open(file_name, "w") as log_file:
        json.dump({"logs": log_entries}, log_file, indent=2)

if __name__ == "__main__":
    # Specify the file name and number of log entries to generate
    generate_log_file("events.json", num_entries=number_of_entries)
    print("Simulated log file 'events.log' created.")