#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @File Name: scrape.py
# @Created:   2017-09-20 04:25:27  seo (simon.seo@nyu.edu) 
# @Updated:   2017-09-20 04:54:38  Simon Seo (simon.seo@nyu.edu)

import urllib3
import csv
from bs4 import BeautifulSoup as bs

http = urllib3.PoolManager()

url = "http://i6.cims.nyu.edu/~ms9144/external/Species%20Search%20Results.htm"

page = http.request('GET', url).data
soup = bs(page, "html.parser")

trs = soup.find_all('tr')
header = trs[0]
for tr in trs[1:50]:
    tds = tr.find_all('td')
    print(len(header), len(tds))
    print(": {}, ".join([h.text for h in header]).format(*[td.text.strip() for td in tds]))