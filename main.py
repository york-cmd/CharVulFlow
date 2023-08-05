from module.is_logic import is_but
from module.is_logic import is_thor
from module.is_logic import is_bugcloud
from module.is_unique import is_unique
from tqdm import tqdm
import time

banner = '''\033[32m[INFO] 目前支持补天[is_but] 雷神[is_thor] 360众包[is_bugcloud]；
_________ .__                ____   ____    .__  ___________.__                 
\_   ___ \|  |__ _____ ______\   \ /   /_ __|  | \_   _____/|  |   ______  _  __
/    \  \/|  |  \\__  \\_  __ \   Y   /  |  \  |  |    __)  |  |  /  _ \ \/ \/ /
\     \___|   Y  \/ __ \|  | \/\     /|  |  /  |__|     \   |  |_(  <_> )     / 
 \______  /___|  (____  /__|    \___/ |____/|____/\___  /   |____/\____/ \/\_/  
        \/     \/     \/                              \/                          
[INFO] 建议脚本Pycharm运行，方便修改代码；
[INFO] 建议脚本_VMware运行，不会干扰工作;\033[0m'''

path = "url.txt"    # 存在漏洞url文件
is_unique(path)     # 去重url.txt
print(banner)
with open(path, 'r', encoding="utf-8") as f:
    urls = f.readlines()
    for i in tqdm(urls):
        i = i.strip()
        try:
            is_but(i)       # 补天提交逻辑流
            # is_thor(i)      # 雷神提交逻辑流
            # is_bugcloud(i)  # 众包提交逻辑流
        except:
            pass
        time.sleep(15)
