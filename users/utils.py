from django.conf import settings
import requests

# Constants for the API endpoints
TIMEZONE_API_BASE_URL = "https://ptvplqzlhh6754nlgl4kdwzuhq0vblxi.lambda-url.eu-west-1.on.aws"
CONVERT_ENDPOINT = "/convert"

def convert_timezone(original_time, original_timezone, target_timezone):
    """Convert a datetime from one timezone to another."""
    payload = {
        'original_time': original_time,
        'original_timezone': original_timezone,
        'target_timezone': target_timezone
    }
    response = requests.post(f"{TIMEZONE_API_BASE_URL}{CONVERT_ENDPOINT}", json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error, possibly logging it or raising an exception
        return None
    

#HUANG'S API
def send_welcome_email(user_email):
    api_url =  "http://18.201.185.103:5002/send-email"
    payload = {
        'email': user_email,
        'subject': 'Welcome to ECOTRACE!',
        'message': 'Hi, Thank you for signing up to CarbonTracker! We hope you enjoy using our platform to track your carbon footprint. Ecotrace is a platform that helps you track your carbon footprint and make more sustainable choices. We hope you enjoy using our platform to track your carbon footprint.'
    }
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)

