import ast
import requests
from time import sleep

requests.packages.urllib3.disable_warnings()
# proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
proxies = {}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'}


def but_upload(pash):
    files = {"upfile": ("a.png", open(pash, "rb"), "image/jpeg")}
    try:
        rsp = requests.post("https://www.butian.net/Public/ueditor/php/controller.php?action=uploadimage", files=files,
                            verify=False, timeout=30, proxies=proxies)
        # print(rsp.text)
    except requests.exceptions.RequestException:
        print("上传图片超时")
        sleep(5)
        return but_upload(pash)
    zidian = ast.literal_eval(rsp.text)
    return zidian["url"]

# but_upload(pash="D:/360/CharVulFlow/temp/site.png")
