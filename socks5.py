#aiohttp
import aiohttp
import asyncio
from aiohttp_socks import ProxyConnector
import aiohttp
async def fetch(url):
    connector = ProxyConnector.from_url('socks5://127.0.0.1:1080')

    ### or use ProxyConnector constructor
    # connector = ProxyConnector(
    #     proxy_type=ProxyType.SOCKS5,
    #     host='127.0.0.1',
    #     port=1080,
    #     username='user',
    #     password='password',
    #     rdns=True
    # )

    ### proxy chaining (since ver 0.3.3)
    # connector = ChainProxyConnector.from_urls([
    #     'socks5://user:password@127.0.0.1:1080',
    #     'socks4://127.0.0.1:1081',
    #     'http://user:password@127.0.0.1:3128',
    # ])
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()

loop = asyncio.get_event_loop()
task = fetch("https://google.com.hk")
text = loop.run_until_complete(task)


#requests
pip install -U requests[socks]
import requests
resp = requests.get('https://google.com.hk', 
                    proxies=dict(http='socks5://127.0.0.1:1080',
                                 https='socks5://127.0.0.1:1080'))

#urllib2
import urllib.request as urllib2
import socket
import socks # you need to install pysocks (see above)

# Configuration
SOCKS5_PROXY_HOST = '127.0.0.1'
SOCKS5_PROXY_PORT = 1080

# Remove this if you don't plan to "deactivate" the proxy later
default_socket = socket.socket

# Set up a proxy
socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
socket.socket = socks.socksocket

        
