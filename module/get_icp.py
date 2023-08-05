import json
from urllib.parse import urlparse

import requests
import configparser
import ast
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'config.ini'))


def get_icp(url):
    if url.startswith("http"):
        url = urlparse(url).netloc
    else:
        url = f"http://{url}"
    key = config.get('config', 'chinaz')
    url = f"https://apidatav2.chinaz.com/single/icp?key={key}&domain={url}"
    res = requests.get(url=url)
    # print(res.text)
    data = json.loads(res.text)
    if data["Result"] == None:
        return []
    elif data["Result"]["CompanyType"] == "个人":
        return []
    elif data["StateCode"] == 1:
        return data["Result"]["CompanyName"]
    elif data["StateCode"] == 10022:
        print("[WARN] chinaz调用次数不足")
    else:
        print(data["Reason"])
        return []

# print(get_icp(url="mingshang.cc"))
