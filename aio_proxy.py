#!/usr/bin/env python

from aiohttp import ClientSession
import asyncio
from itertools import islice
import sys, pickle

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
            gen_proxy = f'{proxy["protocols"][0]}://{proxy["ip"]}:{proxy["port"]}\n'
            proxies.append(gen_proxy)
    with open(file, 'w') as f:
        f.writelines(proxies)
    return proxies
import aiohttp
import asyncio

# MAXREQ = 500
MAXTHREAD = int(sys.argv[1])

URL = "http://ifconfig.me"


g_thread_limit = asyncio.Semaphore(MAXTHREAD)


async def worker(session, proxy):
    async with session.get(URL, proxy=proxy) as response:
        # await response.read()
        status = await response.status
        return (status, proxy)


async def run(worker, *argv):
    async with g_thread_limit:
        await worker(*argv)


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[run(worker, session, proxy) for proxy in open('all_proxy.txt')])


if __name__ == '__main__':
    # Don't use asyncio.run() - it produces a lot of errors on exit.
    asyncio.get_event_loop().run_until_complete(main())
