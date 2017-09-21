#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @File Name: scrape.py
# @Created:   2017-09-20 04:25:27  seo (simon.seo@nyu.edu) 
# @Updated:   2017-09-20 23:18:46  Simon Seo (simon.seo@nyu.edu)

from urllib import request
import csv
from bs4 import BeautifulSoup as bs

def main():
	# url = input("The URL of the data: ")
	url = "http://i6.cims.nyu.edu/~ms9144/external/Species_All.htm"
	page = download(url)

	# output_name = input('Name of the output csv file: ')
	output_name = 'endangered_species_US.csv'
	parse(page, output_name)

def download(url):
	'''Downloads and returns a webpage'''
	try:
		print("Attempting download of the page.")
		page = request.urlopen(url).read()
	except Exception as e:
		print("Invalid page or failed connection.")
		raise e
	else:
		print("Download successful. Parsing page.")
	return page

def parse(page, output_name):
	'''Parses the given webpage and saves table data in the output file'''
	soup = bs(page, "html.parser")
	csv_file = open(output_name, 'w')
	writer = csv.writer(csv_file, delimiter=',')

	trs = soup.find_all('tr')
	header = []
	for field in trs[0]:
		header.append(field.text.strip())
	writer.writerow(header)
	for tr in trs[1:]:
		tds = tr.find_all('td')
		# print(": {}, ".join([h.text for h in header]).format(*[td.text.strip() for td in tds]))
		row = []
		for td in tds:
			data = td.text.strip()
			row.append(data)
		writer.writerow(row)
	csv_file.close()

	print("Page saved in {}".format(output_name))
	return output_name

