import requests

from API_JWT_generator import generate_api_jwt

# produce JWT token
jwt_token = generate_api_jwt()


def call(command):
    # Specify the API endpoint you're targeting
    base_api_url = 'https://api.zoom.us/v2'
    command_api_url = command

    # Prepare the request headers with the Authorization
    headers = {
        'Authorization': f'Bearer {jwt_token}',
        'Content-Type': 'application/json'
    }

    # Make the GET request to the Zoom API
    response = requests.get(base_api_url+command_api_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Process the response data (which is in JSON format)
        data = response.json()
        print("Response Data:", data)
    else:
        # Handle request error
        print("Error:", response.status_code, response.text)

    return response