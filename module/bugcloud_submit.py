# -*- coding: utf-8 -*-
from time import sleep
from urllib.parse import urlparse
from tldextract import tldextract
from module.get_icp import get_icp
from module.bugcloud_upload import bugcloud_upload

import json
import requests
import configparser
import os

# proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
proxies = {}

BASE_DIR1 = os.path.dirname(os.path.abspath(__file__))
BASE_DIR2 = os.path.dirname(BASE_DIR1)
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR1, 'config.ini'))
cookie = config.get('bugcloud', 'cookie')
head = {
    'Host': 'src.360.net',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'Cookie': f"{cookie}",
    'Acceptlanguage': 'zh',
    'Referer': 'https://src.360.net/submit-bug'}

def bugcloud_csrf():
    url2 = "https://src.360.net//api/frontend/user/userdetail"
    try:
        res2 = requests.post(url=url2, headers=head, verify=False)
    except Exception as e:
        print(e)
    data = json.loads(res2.text)
    data = data["result"]["csrf_token"]
    return data

# print(bugcloud_csrf())

def bugcloud_submit(url, domain):
    # 判断是否存在domain
    if len(domain) > 0:
        company = get_icp(domain)
    else:
        company = get_icp(url)
    # print(company)
    # 判断是否存在公司
    if company == []:
        return

    url1 = tldextract.extract(url)
    host = url1.domain + "." + url1.suffix
    image1 = bugcloud_upload(os.path.join(BASE_DIR2, 'temp', 'site.png'))
    sleep(5)
    image2 = bugcloud_upload(os.path.join(BASE_DIR2, 'temp', 'vul.png'))
    sleep(5)
    image3 = bugcloud_upload(os.path.join(BASE_DIR2, 'temp', 'icp.png'))
    # print("img")
    if len(domain) > 0:
        image4 = bugcloud_upload(os.path.join(BASE_DIR2, 'temp', 'domain.png'))
        whois = f'''
        <p>IP查询：<img src=\"{image4}\"></p><p>归属查询：<img src=\"{image3}\"></p>'''
    else:
        whois = f'''
        <p>归属查询：<img src=\"{image3}\"></p>'''
    # print(whois)
    # 提交前获取验证识别
    csrf = bugcloud_csrf()
    # print("csrf")
    data = {"business_name": f"{company}所属网站",
            "title": f"{company}敏感信息泄露",
            "bug_type": "1",
            "bug_level": "5",
            "desc_v": f"{company}敏感信息泄露",
            "rec_step": f'''<p>归属证明：{whois}</p><p>1.网站首页：<img src=\"{image1}\"></p><p>2.漏洞截图：<img src=\"{image2}\"></p>''',
            "repair_plan": "<p>鉴权过滤，限制接口访问，及时更新</p>",
            "annex": {},
            "web_name": f"{company}",
            "web_ip": f"{domain}",
            "province": "北京市",
            "city": "北京市",
            "area": "市辖区",
            "bug_category_main": "1",
            "bug_category": "45",
            "bug_url": f"{url}",
            "csrf_token": f"{csrf}",
            "is_use_common_bug": "5",
            "component_name": "",
            "first_industry": "1",
            "second_industry": "122",
            # "bug_id": "7lYPXe4aG/k="
        }
    # print(data)
    try:
        url1 = "https://src.360.net/api/frontend/hacker/bugmanage/submitbug"
        res1 = requests.post(url=url1, headers=head, json=data, verify=False, proxies=proxies)
        # print(res1.text)
    except Exception as e:
        print(e)
    data = json.loads(res1.text)
    if data["code"] == 200:
        print(f"360众包成功提交{company}")
    # 验证失败
    elif data["code"] == 201:
        return bugcloud_submit(url, domain)
    else:
        print(data["msg"])

# url = "http://1.14.8.252:8088/808gps/MobileAction_downLoad.action?path=/WEB-INF/classes/config/jdbc.properties"
# domain = "mingshang.cc"
# bugcloud_submit(url, domain)
