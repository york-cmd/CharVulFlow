import json
import requests
import re

proxies = {}
# proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
requests.packages.urllib3.disable_warnings()


def getsite_ip138(url):
    ip138_head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"}
    ip138_path = f"https://site.ip138.com/{url}/"
    try:
        ip138_res = requests.get(url=ip138_path, headers=ip138_head, timeout=10, verify=False, proxies=proxies)
        if '暂无结果' not in ip138_res.text:
            site = re.findall(r"""</span><a href="/(.*?)/" target="_blank">""", ip138_res.text)
            # print(f"ip138查询{site}")
            return site
        else:
            return []
    except Exception as e:
        print(f"ip138{e}")
        return []
        pass


def getsite_webscan(url):
    webscan_head = {"Referer": "https://dns.aizhan.com/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"}
    webscan_path = f"http://api.webscan.cc/?action=query&ip={url}/"
    try:
        # proxies = random.choice(proxies_list)
        webscan_res = requests.get(url=webscan_path, headers=webscan_head, timeout=10, verify=False, proxies=proxies)
        domains_reg = r"(?P<protocol>https?://)?(?P<domain>[^:/\s]+\.[a-zA-Z]{2,})"
        webscan_res = json.loads(webscan_res.text)
        sites = []
        for item in webscan_res:
            match = re.search(domains_reg, item["domain"])
            if match:
                domain = match.group("domain")
                sites.append(domain)
                return sites
            else:
                return []
        # print(sites)
    except Exception as e:
        print(f"webscan{e}")
        return []
        pass


def getsite_all(url):
    ip138 = getsite_ip138(url)
    # webscan = getsite_webscan(url)
    # sites = ip138 + webscan
    sites = ip138[0]
    # print(sites)
    return sites

# print(getsite_all("112.27.219.239"))
