# CODED BY LARRAVELL
correct_password = "larravell"

# CODED BY LARRAVELL
password = input("Put Password: ")

# CODED BY LARRAVELL
if password == correct_password:
    print("2023 WEBSITE VISITOR CONTACT TG: @larravell")
    
    import requests

    url = input("PUT LINK FOR VISITORS: ")
    headers = {
        "Sec-Ch-Ua": '"Not:A-Brand";v="99", "Chromium";v="112"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close"
    }
    repeat_count = int(input("How Many Views ? : "))

    for i in range(repeat_count):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Sent {i+1} Successfully")
        else:
            print(f"Cant {i+1} Be Sent {response.status_code}")

    print("Successfully Sent Visitors")
else:
    print("Wrong Password. ")
    exit()
