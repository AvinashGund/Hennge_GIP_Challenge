import requests
import base64
import hmac
import hashlib
import time
import json

# Function to generate TOTP
def generate_totp(key, digits=10, window=30):
    # Calculate the current time in seconds
    current_time = int(time.time())
    time_counter = current_time // window

    # Convert the counter to bytes
    counter_bytes = time_counter.to_bytes(8, byteorder='big')

    # Calculate the HMAC-SHA-512 hash
    hmac_hash = hmac.new(key, counter_bytes, hashlib.sha512).digest()

    # Dynamic truncation to get the OTP
    offset = hmac_hash[-1] & 0x0F
    binary = ((hmac_hash[offset] & 0x7F) << 24 |
              (hmac_hash[offset + 1] & 0xFF) << 16 |
              (hmac_hash[offset + 2] & 0xFF) << 8 |
              (hmac_hash[offset + 3] & 0xFF))

    totp = str(binary % 10**digits)

    # Ensure the OTP has the desired number of digits
    return totp.zfill(digits)

# Function to make the HTTP POST request
def make_post_request(github_url, contact_email, solution_language, totp):
    # Construct the JSON string
    json_data = {
        "github_url": github_url,
        "contact_email": contact_email,
        "solution_language": solution_language
    }
    json_string = json.dumps(json_data)

    # Construct the Authorization header
    authorization = f"Basic {base64.b64encode(f'{contact_email}:{totp}'.encode()).decode()}"

    # Define the headers and URL
    headers = {
        'Authorization': authorization,
        'Content-Type': 'application/json',
    }

    url = "https://api.challenge.hennge.com/challenges/003"

    # Send the HTTP POST request
    response = requests.post(url, headers=headers, data=json_string)

    return response

# Replace with your own values
github_url = "https://gist.github.com/AvinashGund/8244872ac49ac12214c11c5e209aef62"
contact_email = "avinashgund95@gmail.com"
solution_language = "python"

# Replace with your shared secret as described in the mission
shared_secret = "avinashgund95@gmail.comHENNGECHALLENGE003"

# Generate the TOTP
totp = generate_totp(shared_secret.encode(), digits=10, window=30)

# Make the HTTP POST request
response = make_post_request(github_url, contact_email, solution_language, totp)

# Print the response
print(response.status_code)
print(response.json())
