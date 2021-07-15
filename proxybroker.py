
import json, socks5, socks

with open('Free_Proxy_List.json') as f:
    proxies = json.load(f)
    
len(proxies)
proxies[0]

def all_proxy_to_one(file='all_proxy.txt'):
     
    proxies_list = ['HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5']
    proxies = []   
    for p in proxies_list:
        with open(f'proxie_lists/Proxy_{p.lower()}.txt') as f:
            for url in f.readlines():
                proxies.append(f'{p.lower()}://{url}')
    with open('responses_proxy.pickle') as f:
        responses = pickle.load(f)
    for proxies in responses:
        for proxy in proxies['data']:
            gen_proxy = f'{proxy["protocols"][0]}://{proxy["ip"]}:{proxy["port"]}'
            proxies.append(gen_proxy)
    with open(file, 'w') as f:
        f.writelines(proxies)
    return proxies
    
import requests
responses = []
for n in range(1, 31):
    print(f'try {n} page')
    url = f'https://proxylist.geonode.com/api/proxy-list?limit=50&page={n}&sort_by=lastChecked&sort_type=desc'
    r = requests.get(url)
    responses.append(r.json())
    print(f'finish {n} page')
import pickle
with open('responses_proxy.pickle', 'wb') as f:
    pickle.dump(responses, f)

url = 'https://ifconfig.me/'
suc_proxy = []
proxies_count = 0
all_proxy = len(responses) * len(responses[0]['data'])
for proxies in responses:
    for proxy in proxies['data']:
        print(f'trying {proxies_count}/{all_proxy} proxy {100*proxies_count/all_proxy:.2f}%')
        
        gen_proxy   = f'{proxy["protocols"][0]}://{proxy["ip"]}:{proxy["port"]}'
        print(gen_proxy)
        proxyDict = { 
                    "http"  : gen_proxy, 
                    "https" : gen_proxy, 
                    "ftp"   : gen_proxy
                    }
        proxies_count += 1
        try:
            r = requests.get(url, proxies=proxyDict, timeout=2)
            print(r, r.text)
            print()
            suc_proxy.append(gen_proxy)
        except:
            pass
with open('succes2_proxy.txt', 'w') as f:
    f.writelines(suc_proxy)
suc_proxy

def new_session():
    import requestium
    from requestium import Session, Keys
    s = Session(webdriver_path='chromedriver',
        browser='chrome',
        default_timeout=15,
        webdriver_options={'arguments': ['headless', 'no-sandbox','disable-dev-shm-usage'],
                           "download.default_directory": r"C:\Users\xxx\downloads\Test",
                            "download.prompt_for_download": False,
                            "download.directory_upgrade": True,
                            "safebrowsing.enabled": True})#,
    # experimental_option={"download.default_directory": r"C:\Users\xxx\downloads\Test",
    #                         "download.prompt_for_download": False,
    #                         "download.directory_upgrade": True,
    #                         "safebrowsing.enabled": True})
    return s

# options.add_experimental_option("prefs", {
#   "download.default_directory": r"C:\Users\xxx\downloads\Test",
#   "download.prompt_for_download": False,
#   "download.directory_upgrade": True,
#   "safebrowsing.enabled": True
# })
url_proxie_site = 'https://www.proxy-list.download/'
proxies_list = ['HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5']
s = new_session()
for p in proxies_list:
    url = url_proxie_site + p
    s.driver.get(url)
    s.driver.find_element_by_xpath('//*[@id="downloadbtn"]').click()
    s.driver.execute_script('javascript:void(0)')
    

proxies = {}    
for p in proxies_list:
    with open(f'proxie_lists/Proxy_{p.lower()}.txt') as f:
        proxies[p] = f.readlines()

suc_proxy2 = []
proxies_count = 0
all_proxy = 0
for p in proxies:
    all_proxy += len(proxies[p])
for key, p in proxies.items():
    for proxy in p:
        print(f'trying {proxies_count}/{all_proxy} proxy {100*proxies_count/all_proxy:.2f}%')
        prox = proxy.split(':')
        gen_proxy   = f'{key.lower()}://{prox[0]}:{prox[1]}'
        print(gen_proxy)
        proxyDict = { 
                    "http"  : gen_proxy, 
                    "https" : gen_proxy, 
                    "ftp"   : gen_proxy
                    }
        proxies_count += 1
        try:
            r = requests.get(url, proxies=proxyDict, timeout=2)
            print(r, r.text)
            print()
            suc_proxy2.append(gen_proxy)
        except Exception as e:
            print(e)
with open('succes3_proxy.txt', 'w') as f:
    f.writelines(suc_proxy2)
suc_proxy2