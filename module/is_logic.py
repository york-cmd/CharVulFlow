from module.but_submit import but_submit
from module.get_shoot import shoot_isip
from module.get_shoot import shoot_noip
from module.get_domain import getsite_all
from module.thor_submit import thor_submit
from module.is_ip import is_ip
from urllib.parse import urlparse


def is_thor(i):
    if is_ip(i):
        url = urlparse(i).netloc
        ip = url.split(":")[0]
        domain = getsite_all(ip)
        if domain == "":
            print("查无域名")
            pass
        else:
            # print(i, domain)
            shoot_isip(i, domain)
            thor_submit(i, domain)
    else:
        # print(i)
        shoot_noip(i)
        thor_submit(i, "")


def is_but(i):
    if is_ip(i):
        url = urlparse(i).netloc
        ip = url.split(":")[0]
        domain = getsite_all(ip)
        if domain == "":
            print("查无域名")
            pass
        else:
            # print(i, domain)
            shoot_isip(i, domain)
            but_submit(i, domain)
    else:
        # print(i)
        shoot_noip(i)
        but_submit(i, "")
