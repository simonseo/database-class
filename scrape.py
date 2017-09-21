#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# @File Name: scrape.py
# @Created:   2017-09-20 04:25:27  seo (simon.seo@nyu.edu) 
# @Updated:   2017-09-21 00:55:57  Simon Seo (simon.seo@nyu.edu)

from urllib import request
import csv
from bs4 import BeautifulSoup as bs

def main():
	# url = input("The URL of the data: ")
	url = "http://i6.cims.nyu.edu/~ms9144/external/Species_All.htm"
	page = download(url)

	# csv_name = input('Name of the output csv file: ')
	dataname = 'endangered_species'
	parsed = parse(page, dataname + '.csv')
	filter(parsed, dataname + '_filtered.csv', 'CurrentDistribution', 'NY', 'Regions ofOccurrence', '5')

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

	# Save the header (only the ones that we require)
	header = []
	req = "Scientific Name,Common Name,CurrentDistribution,Family,Species Group,Federal Listing Status,Regions ofOccurrence,Vertebrate/Invertebrate/Plant"
	req = req.split(',')
	i = 0
	req_idx = [] # index of the header fields that we require
	for field in trs[0]:
		field = field.text.strip()
		if field in req:
			header.append(field)
			req_idx.append(i)
		i += 1
	writer.writerow(header)

	# Save the data rows
	for tr in trs[1:]:
		tds = tr.find_all('td')
		# print(": {}, ".join([h.text for h in header]).format(*[td.text.strip() for td in tds]))
		row = []
		i = 0
		for td in tds:
			if i in req_idx:
				data = td.text.strip()
				row.append(data)
			i += 1
		writer.writerow(row)
	csv_file.close()

	print("Page parsed and the data was saved in {}".format(output_name))
	return output_name

def filter(input_name, output_name, *args):
	'''Clean up the csv file and add new columns 
	that checks if each species satisfy a condition'''

	# Create CSV reader and writer
	try:
		csv_in = open(input_name, 'r')
	except Exception as e:
		print('Check if unfiltered file exists.')
		raise e
	else:
		print('Checking for some filters')
	reader = csv.reader(csv_in, delimiter=',')
	csv_out = open(output_name, 'w')
	writer = csv.writer(csv_out, delimiter=',')

	# save the filter conditions and update header with the conditions
	filters = []
	header = next(reader)
	for i in range(0, len(args), 2):
		header.append('{1} in {0}'.format(args[i], args[i+1]))
		filters.append((args[i], args[i+1]))
	writer.writerow(header)

	# for each species check whether conditions satisifies
	for row in reader:
		for filter_field, keyword in filters:
			for i in range(len(row)):
				if header[i] == filter_field:
					row.append(keyword in row[i])
		writer.writerow(row)

	csv_in.close()
	csv_out.close()
	print('All filter conditions were checked and the data was saved in {}.'.format(output_name))


main()
