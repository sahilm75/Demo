import requests
import json

def test_classify_api():
    # Define the API endpoint URL
    url = 'http://localhost:3000/classify'

    # Define the headers
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # Define the request body (in this case, a list with a single element, 0)
    data = [0]

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the status code and print the response
    if response.status_code == 200:
        print(f"API Test Passed: Status code {response.status_code}")
        print(f"Response: {response.json()}")
    else:
        print(f"API Test Failed: Status code {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    test_classify_api()