from urllib.parse import urlparse
from module.is_ip import is_ip


def is_unique(path):
    unique_domains = set()
    new_is = []

    with open(path, 'r') as file:
        for i in file:
            url = i.strip()
            netloc = urlparse(url).netloc
            if is_ip(i):
                domain = netloc.split(':')[0]
                # print(domain)
            else:
                domain = '.'.join(netloc.split('.')[-2:])
            if domain not in unique_domains:
                unique_domains.add(domain)
                new_is.append(url)

    with open(path, 'w') as file:
        for i in new_is:
            file.write(i + '\n')
        print(f"Complete deduplication! Start {len(new_is)} tasks")
