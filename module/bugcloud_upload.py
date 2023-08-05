import json
import requests
from time import sleep

requests.packages.urllib3.disable_warnings()
# proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
proxies = {}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
}
# print(proxies)

def bugcloud_upload(path):
    files = {"qh_img": ("a.png", open(path, "rb"), "image/jpeg")}
    try:
        res = requests.post("https://src.360.net/api/frontend/fpublic/imgupload", files=files,
                            verify=False, timeout=5, proxies=proxies)
        # print(res.text)
    except Exception as e:
        print(e)
        # sleep(5)
        return bugcloud_upload(path)
    data = json.loads(res.text)
    data = data["result"]["img_url"]
    # print(data)
    return data

# bugcloud_upload(path="D:/360/CharVulFlow/temp/site.png")
