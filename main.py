import json, requests, os
from dotenv import load_dotenv

load_dotenv()

# https://omahaproxy.appspot.com/win
def web_hook_trigger(msg):
    url = os.getenv('web_hook')
    payload = {
        "channel":"#scripts_alerts",
        "text": f"{msg}",
        "username":"webhookbot",
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.text.encode('utf8'))


def get_version():
    url = 'https://omahaproxy.appspot.com/win'
    resp = requests.get(url).content.decode('utf-8')
    with open('version.txt', 'r+') as f:
        current_version = f.read()
        if current_version != resp:
            msg = f"THERE IS A NEW VERSION 🎉 '{resp}' OLDER VERSION IS '{current_version}'🤕"
            print(msg)
            web_hook_trigger(msg)
            with open('version.txt', 'w') as new_file_content: new_file_content.write(resp)
            

if __name__ == "__main__":
    get_version()