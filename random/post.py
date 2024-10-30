import requests
import json
import base64

# Information for the request
email = "ashwathkannan266@gmail.com"
auth_password = "1165201317"  # TOTP provided
auth_string = f"{email}:{auth_password}"
auth_header = base64.b64encode(auth_string.encode()).decode()

# JSON Payload
payload = {
    "github_url": "https://gist.github.com/Ash-2k3/3495f51cf271fb5c389903423eb3934c",
    "contact_email": "ashwathkannan266@gmail.com",
    "solution_language": "python"
}

# HTTP Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {auth_header}"
}

# Send POST Request
response = requests.post("https://api.challenge.hennge.com/challenges/003", headers=headers, data=json.dumps(payload))

# Check the response
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.status_code, response.text)
