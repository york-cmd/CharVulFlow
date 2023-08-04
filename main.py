from module.is_logic import is_but
from module.is_logic import is_thor
from module.is_unique import is_unique
from tqdm import tqdm
import time

banner = '''\033[32m
_________ .__                ____   ____    .__  ___________.__                 
\_   ___ \|  |__ _____ ______\   \ /   /_ __|  | \_   _____/|  |   ______  _  __
/    \  \/|  |  \\__  \\_  __ \   Y   /  |  \  |  |    __)  |  |  /  _ \ \/ \/ /
\     \___|   Y  \/ __ \|  | \/\     /|  |  /  |__|     \   |  |_(  <_> )     / 
 \______  /___|  (____  /__|    \___/ |____/|____/\___  /   |____/\____/ \/\_/  
        \/     \/     \/                              \/                          
[INFO] 目前支持补天、雷神提交，通过注释24、25行代码决定提交平台，可以一起提交；
[INFO] 建议脚本在IDEA中运行，方便修改代码；
[INFO] 建议脚本在虚拟机中运行，不干扰正常工作。\033[0m'''

path = "url.txt"    # 存在漏洞url文件
is_unique(path)     # 去重url.txt
print(banner)
with open(path, 'r', encoding="utf-8") as f:
    urls = f.readlines()
    for i in tqdm(urls):
        i = i.strip()
        try:
            # is_thor(i)  # 雷神提交逻辑流
            is_but(i)   # 补天提交逻辑流
        except:
            pass
        time.sleep(15)
