from time import sleep
import configparser
import requests
import ast
import os

requests.packages.urllib3.disable_warnings()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'config.ini'))
appkey = config.get('config', 'appkey')

def but_bypass():
    try:
        rsp = requests.get("https://www.butian.net/Loo/startCaptcha", verify=False)
    except:
        return but_bypass()
    zidian = ast.literal_eval(rsp.text)
    date = {'appkey': f'{appkey}', 'gt': '4fd5d5dbea6b9365f94fc525fee2cf20',
            'challenge': zidian["challenge"], 'referer': 'https://www.butian.net/Loo/submit'}
    rsp = requests.post(url="http://api.rrocr.com/api/recognize.html", data=date)
    # print(rsp.text)
    if "识别成功" in rsp.text:
        zidian = ast.literal_eval(rsp.text)
        return zidian["data"]["challenge"], zidian["data"]["validate"]
        pass
    elif "识别失败" in rsp.text:
        return but_bypass()
    elif "积分不足" in rsp.text:
        print("验证识别账户积分不足")
        return []
    else:
        sleep(3)
        return but_bypass()

# but_bypass()
