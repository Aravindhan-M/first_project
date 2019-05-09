import requests
import json

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox1f9ec321f7534c6cb4a28ba396a5b9e7.mailgun.org/messages",
        auth=("api", "98ce546018f8d52c4c32902baee60cc0-b9c15f4c-909cf4b1"),
        data={"from": "aravindhan.sayone@gmail.com",
              "to": ["joys@sayonetech.com"],
              "subject": "Hello scheduled ",
              "text": "Testing some Mailgun Transactional scheduled IST"
              })



res = send_simple_message()
print(res.json())
