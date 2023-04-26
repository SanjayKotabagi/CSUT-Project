import requests

# Set API key
API_KEY = "fac215e1049404090b0122f3d9d888e0386f10d59daac20995a33d112c3a45de"
def get_url_report(url):
    # Set URL to scan

    # Set API endpoint
    endpoint = f"https://pulsedive.com/api/info.php?indicator={url}&pretty"

    # Set API headers
    headers = {"X-Api-Key": API_KEY}

    # Make API request
    response = requests.get(endpoint, headers=headers)
    print(response)
    # Check if request was successful
    if response.status_code == 404:
        return False
    if response.status_code == 200:
        # Get results
        results = response.json()
        # Print results
        # print(results)
        return results
    else:
        return (f"Error: {response.status_code}")
