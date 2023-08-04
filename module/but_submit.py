# -*- coding: utf-8 -*-
from time import sleep
from urllib.parse import urlparse
from tldextract import tldextract
from module.get_icp import get_icp
from module.but_bypass import but_bypass
from module.but_upload import but_upload

import random
import json
import requests
import configparser
import os

requests.packages.urllib3.disable_warnings()
BASE_DIR1 = os.path.dirname(os.path.abspath(__file__))
BASE_DIR2 = os.path.dirname(BASE_DIR1)
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR1, 'config.ini'))
cookie = config.get('but', 'cookie')

session = requests.session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'Cookie': f'{cookie}'}

# proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
proxies = {}


def but_submit(url, domain):
    if len(domain) > 0:
        company = get_icp(domain)
    else:
        company = get_icp(url)
    # print(company)
    if company == []:
        return
    # 获取主页截图上传
    url1 = tldextract.extract(url)
    host = url1.domain + "." + url1.suffix

    image1 = but_upload(os.path.join(BASE_DIR2, 'temp', 'site.png'))
    image1 = image1.replace("\/", "/")
    sleep(5)
    image2 = but_upload(os.path.join(BASE_DIR2, 'temp', 'vul.png'))
    image2 = image2.replace("\/", "/")
    sleep(5)
    image3 = but_upload(os.path.join(BASE_DIR2, 'temp', 'icp.png'))
    image3 = image3.replace("\/", "/")

    if len(domain) > 0:
        image4 = but_upload(os.path.join(BASE_DIR2, 'temp', 'domain.png'))
        image4 = image4.replace("\/", "/")
        whois = f'''
        <img src="{image3}" title="" alt="index.png"/>
        <img src="{image4}" title="" alt="index.png"/>'''
    else:
        whois = f'''
        <img src="{image3}" title="" alt="index.png"/>'''
    # 滑块识别
    challenge, validate = but_bypass()
    if (challenge == "shibai"):
        return
    detail = f"""<p>归属证明截图：{whois}
    访问首页截图：<img src="{image1}" title="" alt="index.png"/></p>
    <p>漏洞所在url:<a href="http://m.dota.uuu9.com/dota.rar">{url}</a></p>
    <p><br/></p>
    <p>漏洞验证步骤：</p><ol style="list-style-type: decimal;" class=" list-paddingleft-2"><li>
    <p>直接访问漏洞url即可下载数据库配置文件，观察浏览器右上角发现已经下载</p></li></ol><p><br/></p>
    <p>配置文件截图：<img src="{image2}" title="" alt="index.png"/></p><p><br/></p>
    """

    files = {
        'attachment': (None, ''),
        'attachment_name': (None, ''),
        'url': (None, url),
        'attribute': (None, '1'),  # 漏洞类型，1：事件 2：通用
        'company_name': (None, company),
        'host': (None, host),
        'origin': (None, '1'),
        'title': (None, company + '1网站存在数据库配置信息泄露'),
        'active_id': (None, ''),  # 活动id
        'type': (None, '10'),  # 漏洞类型 67弱口令 10信息泄露
        'level': (None, '1'),  # 漏洞等级 2：高危
        'description': (None, company + '关联网站存在数据库账号密码明文信息泄露'),
        'detail': (None, detail),
        'repair_suggest': (None, '加强拦截策略，不允许接口访问'),
        'tag3': (None, 'class1|18,class2|19'),
        'province': (None, '青海省'),  # 所属地区 省
        'city': (None, '西宁市'),  # 所属地区 市
        'county': (None, '市辖区'),
        'company_contact': (None, ''),
        'anonymous': (None, '1'),  # 匿名提交
        'agree': (None, '1'),  # 是否同意用户协议
        'id': (None, ''),  # 未知属性
        'geetest_challenge': (None, challenge),
        'geetest_validate': (None, validate),
        'geetest_seccode': (None, validate + '|jordan')
    }
    try:
        url_but = "https://www.butian.net/Home/Loo/submit"
        rsp = session.post(url=url_but, files=files, headers=headers, verify=False,
                           timeout=15, proxies=proxies)
    except:
        return but_submit(url, domain)
    # print(rsp.text)
    data = json.loads(rsp.text)
    if "QTVA" in data["data"]:
        print(f"补天成功提交{company}")
        pass
    elif data["info"] == "\u64cd\u4f5c\u8fc7\u4e8e\u9891\u7e41\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5":
        # print(f"{url}操作过于频繁")
        sleep(random.randint(20, 30))
        but_submit(url, domain)
    elif rsp.status_code == 302:
        print(f"补天COOKIE失效")
        pass
    else:
        print(f'补天{data["info"]}')
        pass

# but_submit("http://1.14.8.252:8088/808gps/MobileAction_downLoad.action?path=/WEB-INF/classes/config/jdbc.properties",
#            "mingshang.cc")
