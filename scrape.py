#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @File Name: scrape.py
# @Created:   2017-09-20 04:25:27  seo (simon.seo@nyu.edu) 
# @Updated:   2017-09-20 16:36:00  Simon Seo (simon.seo@nyu.edu)

from urllib import request
import csv
from bs4 import BeautifulSoup as bs



# url = input("The URL of the data: ")
url = "http://i6.cims.nyu.edu/~ms9144/external/Species%20Search%20Results.htm"
try:
	page = request.urlopen(url).read()
except Exception as e:
	print("Invalid page or failed connection.")
	raise e

soup = bs(page, "html.parser")

# output_name = input('Name of the output csv file: ')
output_name = 'endangered_species_US.csv'
csv_file = open(output_name, 'w')
writer = csv.writer(csv_file, delimiter=',')

trs = soup.find_all('tr')
header = []
for field in trs[0]:
	header.append(field.text.strip())
writer.writerow(header)
for tr in trs[1:50]:
	tds = tr.find_all('td')
	# print(": {}, ".join([h.text for h in header]).format(*[td.text.strip() for td in tds]))
	data = []
	for td in tds:
		data.append(td.text.strip())
	writer.writerow(data)


csv_file.close()

