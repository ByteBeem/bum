import requests
import time

url = "https://heavenly-onyx-bun.glitch.me/"
port = 3000

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Request sent successfully!")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed with exception: {e}")
    
    time.sleep(5)  # Sleep for 5 seconds before sending the next request
