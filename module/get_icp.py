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
    rsp = requests.get(f"https://apidatav2.chinaz.com/single/icp?key={key}&domain={url}")
    # print(rsp.text)
    if "null" in rsp.text:
        return []
    res = ast.literal_eval(rsp.text)
    if res["Result"]["CompanyType"] == "个人":
        return []
    elif res["StateCode"] == 1:
        return res["Result"]["CompanyName"]
    elif res["StateCode"] == 10022:
        print("[WARN] chinaz调用次数不足")
    else:
        print(res["Reason"])
        return []

# print(get_icp(url="mingshang.cc"))
