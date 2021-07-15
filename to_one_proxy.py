import sys, pickle

def all_proxy_to_one(file='all_proxy.txt'):
     
    proxies_list = ['HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5']
    proxies = []   
    for p in proxies_list:
        with open(f'proxie_lists/Proxy_{p.lower()}.txt') as f:
            for url in f.readlines():
                proxies.append(f'{p.lower()}://{url}')
    with open('responses_proxy.pickle', 'rb') as f:
        responses = pickle.load(f)
    for proxie in responses:
        for proxy in proxie['data']:
            gen_proxy = f'{proxy["protocols"][0]}://{proxy["ip"]}:{proxy["port"]}\n'
            proxies.append(gen_proxy)
    with open(file, 'w') as f:
        f.writelines(proxies)
    return proxies

if __name__ == '__main__':
    p = all_proxy_to_one()
    print(p)