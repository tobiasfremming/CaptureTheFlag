import requests

# Define the target URL and headers
url = "http://koala.hackingarena.no:801/fruit.php"
headers = {
    "Host": "koala.hackingarena.no:801",
    "Accept-Language": "en-US",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://koala.hackingarena.no:801/fruit.php",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Define the cookie
cookies = {
    "CalypId": "KoalaKoala1731681658"
}

# List of fruits to try
fruits = [
    "Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Lemon",
    "Mango", "Nectarine", "Orange", "Papaya", "Quince", "Raspberry", "Strawberry", "Tangerine", "Watermelon"
]

# Get a baseline response with a random fruit
baseline_params = {"fruit": "RandomFruit"}
baseline_response = requests.get(url, headers=headers, cookies=cookies, params=baseline_params).text

# Loop through the list of fruits and make a request for each
for fruit in fruits:
    params = {"fruit": fruit}
    print(f"Trying fruit: {fruit}")
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    
    # Compare the response to the baseline
    if response.text != baseline_response:
        print(f"Different response detected with fruit: {fruit}")
        print(response.text)
        break
else:
    print("No differing response found. Try with a larger set of fruits or investigate further.")
