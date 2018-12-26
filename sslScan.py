# -*- coding: utf-8 -*-
#!/usr/bin/env python
from action import action
from data2Text import data2Text
import requests
import sys
import os
sys.dont_write_bytecode = True#不生成pyc文件


username = 'yubanbanz@gmail.com'
key = '35e0d390d9ebb997b429d049b34054958bfd355a7f7adfbbb709f4139a200892'
auth = (username, key)
base_url = 'https://api.passivetotal.org'

class sslScan(action):
    def do(self,url,ssl):
        a = data2Text(url)
        if not a.getInfo("sslInfo.txt"):
            a.APIInfo()
            pdns_results = self.passivetotal_get('/v2/ssl-certificate/history', ssl)
            for resolve in pdns_results['results']:
                data = []
                data.append('FirstSeen:' + resolve['firstSeen'])
                data.append('LastSeen:' + resolve['lastSeen'])
                for i in resolve['ipAddresses']:
                    data.append(i)
                a.sslInfo(data)
                a.getInfo("sslInfo.txt")
    # 请求获得SSL解析历史
    def passivetotal_get(self,path,query):
        url = base_url + path
        data = {'query': query}
        # Important: Specifying json= here instead of data= ensures that the
        # Content-Type header is application/json, which is necessary.
        response = requests.get(url, auth=auth, json=data)
        # This parses the response text as JSON and returns the data representation.
        return response.json()

# a = sslScan()
# a.do("www.baidu.com","8f529b2596c716254b7443af454524b76a58383a")

# def passivetotal_get(path, query):
#     url = base_url + path
#     data = {'query': query}
#     # Important: Specifying json= here instead of data= ensures that the
#     # Content-Type header is application/json, which is necessary.
#     response = requests.get(url, auth=auth, json=data)
#     # This parses the response text as JSON and returns the data representation.
#     return response.json()
#
# pdns_results = passivetotal_get('/v2/ssl-certificate/history', '8f529b2596c716254b7443af454524b76a58383a')
# for resolve in pdns_results['results']:
#     data = []
#     data.append('FirstSeen:' + resolve['firstSeen'])
#     data.append('LastSeen:' + resolve['lastSeen'])
#     for i in resolve['ipAddresses']:
#         data.append(i)
#     for i in data:
#         print i
# Alias get_dns_passive to a GET to /v2/dns/passive
# from functools import partial
# get_dns_passive = partial(passivetotal_get, '/v2/dns/passive')
# pdns_results_example = get_dns_passive('example.org')
