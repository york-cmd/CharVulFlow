import base64
import configparser
import os
import ddddocr
import requests
import json

BASE_DIR1 = os.path.dirname(os.path.abspath(__file__))
BASE_DIR2 = os.path.dirname(BASE_DIR1)
# print(BASE_DIR2)
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR1, 'config.ini'))
cookie = config.get('thor', 'cookie')
head = {
    'Host': 'bug.bountyteam.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
    'Authorization': cookie,
    'Cookie': f'{cookie}',
    'Acceptlanguage': 'zh',
    'Referer': 'https://bug.bountyteam.com/commitSrcBug'}


# 获取雷神提交验证图形
def get_img():
    url1 = "https://bug.bountyteam.com/api/pictureVerifyCode"
    data = {"type": 1}
    res1 = requests.post(url=url1, headers=head, json=data, verify=False)
    # print(res.text)
    data = json.loads(res1.text)
    img = data["data"]["photo"].split(',')[1]
    img = base64.b64decode(img)
    file = open(os.path.join(BASE_DIR2, 'temp', 'thor.png'), "wb")
    file.write(img)


# 识别图像
def get_ocr():
    ocr = ddddocr.DdddOcr()
    with open(os.path.join(BASE_DIR2, 'temp', 'thor.png'), 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes).upper()
    if len(res) == 4:
        # print(res)
        return res
    else:
        get_ocr()


def thor_bypass():
    get_img()
    return get_ocr()

# print(thor_bypass())
