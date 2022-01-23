import requests

myToken = "xoxb-3002182518544-2995384619396-xxUuokQqwxpnFR225RnOqj0R"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

post_message(myToken,"#call_bit", "autotrade start??")