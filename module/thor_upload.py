import configparser
import json
import os
import requests

requests.packages.urllib3.disable_warnings()
BASE_DIR1 = os.path.dirname(os.path.abspath(__file__))
BASE_DIR2 = os.path.dirname(BASE_DIR1)
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR1, 'config.ini'))
cookie = config.get('thor', 'cookie')

head = {
    'Host': 'bug.bountyteam.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'Authorization': cookie,
    'Cookie': f"JSESSIONID={cookie}",
    'Acceptlanguage': 'zh',
    'Referer': 'https://bug.bountyteam.com/commitSrcBug'}


def thor_upload(path):
    file = {"file": ("a.png", open(path, "rb"), "image/jpeg")}
    try:
        url = "https://bug.bountyteam.com/api/uploadImg"
        res = requests.post(url=url, files=file, headers=head, verify=False, timeout=30)
        # print(res.text)
    except Exception as e:
        print(e)
    data = json.loads(res.text)
    data = data["data"]["url"]
    # print(data)
    return data

# thor_upload()
