#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @File Name: scrape.py
# @Created:   2017-09-20 04:25:27  seo (simon.seo@nyu.edu) 
# @Updated:   2017-09-20 12:01:07  Simon Seo (simon.seo@nyu.edu)

import urllib3
import csv
from bs4 import BeautifulSoup as bs

http = urllib3.PoolManager()

url = "http://i6.cims.nyu.edu/~ms9144/external/Species%20Search%20Results.htm"
try:
	page = http.request('GET', url).data
except Exception as e:
	print("Invalid page or failed connection.")
	raise e

soup = bs(page, "html.parser")

trs = soup.find_all('tr')
header = trs[0]
print(*['"{}"'.format(h.text) for h in header], sep=',')
for tr in trs[1:50]:
    tds = tr.find_all('td')
    # print(": {}, ".join([h.text for h in header]).format(*[td.text.strip() for td in tds]))
    print(*['"{}"'.format(td.text.strip()) for td in tds], sep=',')


