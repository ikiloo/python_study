import requests

myToken = "xoxb-3002182518544-2991571896097-bAwKGB5kaLEWoJ4gQkL9x0ey"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

post_message(myToken,"#stock_ai", "autotrade start")