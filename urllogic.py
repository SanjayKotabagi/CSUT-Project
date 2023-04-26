import requests

urltoscan = "sanjaykotabagi.ml"
API_KEY = "439c27d55859d6e3cbeec33776ef8729d62af602660f8d4b2c6c6cc97d590eb4"

import requests

url = "https://www.virustotal.com/api/v3/urls"

payload = f"url={urltoscan}"
headers = {
    "accept": "application/json",
    "x-apikey": "439c27d55859d6e3cbeec33776ef8729d62af602660f8d4b2c6c6cc97d590eb4",
    "content-type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)