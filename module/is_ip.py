import socket
from urllib.parse import urlparse


def is_ip(url):
    url = urlparse(url).netloc
    url = url.split(":")[0]
    # print(url)
    try:
        ip = socket.gethostbyname(url)
        if ip == url:
            return True
        else:
            return False
    except:
        return False

# print(is_ip("http://www.baidu.com:8080/123"))  # domain
