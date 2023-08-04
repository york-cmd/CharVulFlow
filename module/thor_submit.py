# -*- coding: utf-8 -*-
from time import sleep
from urllib.parse import urlparse
from tldextract import tldextract
from module.get_icp import get_icp
from module.thor_bypass import thor_bypass
from module.thor_upload import thor_upload

import json
import requests
import configparser
import os

# proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
# proxies = {}

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


def thor_submit(url, domain):
    # 判断是否存在domain
    if len(domain) > 0:
        company = get_icp(domain)
    else:
        company = get_icp(url)
    # 判断是否存在公司
    if company == []:
        return

    url1 = tldextract.extract(url)
    host = url1.domain + "." + url1.suffix
    image1 = thor_upload(os.path.join(BASE_DIR2, 'temp', 'site.png'))
    sleep(5)
    image2 = thor_upload(os.path.join(BASE_DIR2, 'temp', 'vul.png'))
    sleep(5)
    image3 = thor_upload(os.path.join(BASE_DIR2, 'temp', 'icp.png'))
    # print("img")
    if len(domain) > 0:
        image4 = thor_upload(os.path.join(BASE_DIR2, 'temp', 'domain.png'))
        whois = f'''
        [[§p§]]IP查询[[§/p§]][[§p§]][[§img src="{image4}"§]][[§br§]][[§/p§]]
        [[§p§]]ICP查询[[§/p§]][[§p§]][[§img src="{image3}"§]][[§br§]][[§/p§]]'''
    else:
        whois = f'''
        [[§p§]]ICP查询[[§/p§]][[§p§]][[§img src="{image3}"§]][[§br§]][[§/p§]]'''
    # 提交前获取验证识别
    code = thor_bypass()
    # print("bypass")
    data = {"companyName": company,
            "companyIp": ["36.134.45.156"],
            "companyDomainName": [host],
            "holeTitle": f"{company}敏感信息泄露",
            "industryCode": "000050",
            "provinceCode": "370000",
            "cityCode": "371500",
            "selfEvaluationTime": "",
            "selfEvaluationLevel": 2,
            "holeType": "信息泄露",
            "holeUrl": [url],
            "holeDetail": f'''
            [[§p§]]### 归属证明：[[§/p§]]
            {whois}
            [[§p§]]### 复现步骤：[[§/p§]]
            [[§p§]]1.网站首页[[§/p§]][[§p§]][[§img src="{image1}"§]][[§br§]][[§/p§]]
            [[§p§]]2.直接访问漏洞url即可发现敏感文件已下载，看浏览器右上角，打开如下[[§/p§]]
            [[§p§]]漏洞所在[[§/p§]][[§p§]][[§img src="{image2}"§]][[§br§]][[§/p§]]
            ''',
            "repairPropose": "鉴权过滤",
            "verifyCode": code,
            "holeDesc": "",
            "holeHarm": "",
            "userId": 1367
            }

    try:
        url1 = "https://bug.bountyteam.com/api/hole/add"
        res1 = requests.post(url=url1, headers=head, json=data, verify=False)
        # print(res1.text)
    except Exception as e:
        print(e)
    data = json.loads(res1.text)
    if data["code"] == 200:
        print(f"雷神成功提交{company}")
    # 验证失败
    elif data["code"] == 201:
        return thor_submit(url, domain)
    else:
        print(data["message"])

# url = ""
# domain = ""
# thor_submit(url, domain)
