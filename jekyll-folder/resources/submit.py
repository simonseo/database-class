#!/usr/local/bin/python3

import sqlite3
import cgi
import cgitb

def main():
	cgitb.enable()

	conn = sqlite3.connect('ontime.db')
	c = conn.cursor()
	form = cgi.FieldStorage()

	startPage()
	
	selectFields = form.getlist('field')
	q = {header : header for header in selectFields}
	q["FL_CODE"] = "UNIQUE_CARRIER || substr('0000' || FL_NUM, -4, 4) AS FL_CODE"
	q["ORIGIN_TXT"] = 'ORIGIN_CITY_NAME || " (" || ORIGIN || ")" AS ORIGIN_TXT'
	q["DEST_TXT"] = 'DEST_CITY_NAME || " (" || DEST || ")" AS DEST_TXT'
	selectQuery = ', '.join([q[header] for header in selectFields])

	filterBy = 'carrier,limitTo,sortBy,ordering'.split(',')
	filters = {f : form.getvalue(f) for f in filterBy}

	query = 'SELECT {} FROM ontime '.format(selectQuery)
	query += '' if filters['carrier'] == 'all' else 'WHERE UNIQUE_CARRIER = "{}" '.format(filters["carrier"])
	query += 'ORDER BY {} {} '.format(filters["sortBy"], filters["ordering"])
	query += '' if filters['limitTo'] == 'all' else 'LIMIT {} '.format(filters["limitTo"])
	c.execute(query, filters)


	friendlyHeader = {}
	friendlyHeader["FL_DATE"] = "Flight Date"
	friendlyHeader["FL_CODE"] = "Flight Code"
	friendlyHeader["ORIGIN_TXT"] = "Origin Airport"
	friendlyHeader["DEST_TXT"] = "Destination Airport"
	friendlyHeader["CRS_DEP_TIME"] = "Scheduled Departure"
	friendlyHeader["DEP_TIME"] = "Actual Departure"
	friendlyHeader["DEP_DELAY"] = "Departure Delay"
	friendlyHeader["CRS_ARR_TIME"] = "Scheduled Arrival"
	friendlyHeader["ARR_TIME"] = "Actual Arrival"
	friendlyHeader["ARR_DELAY"] = "Arrival Delay"
	friendlyHeader["CRS_ELAPSED_TIME"] = "Scheduled Elapsed Time"
	friendlyHeader["ACTUAL_ELAPSED_TIME"] = "Acutal Elapsed Time"

	print('<table><thead>')
	print('<tr>' + ''.join(['<td>{}</td>'.format(friendlyHeader[header]) for header in selectFields]) + '</tr>')
	print('</thead><tbody><tr>')
	for row in c:
		for el in row:
			print('<td>{}</td>'.format(str(el)))
		print('</tr><tr>')
	print('</tr></tbody></table>')
	endPage()

def startPage():
	print ("Content-Type: text/html\r\n\r\n")
	print("""<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="utf-8">
	<meta name="description" content="Using the CGI library to work with HTML forms and SQL database in frontend">
	<title>Using Python CGI</title>
	<link rel="stylesheet" href="/~ms9144/database/css/style.css">
	<meta property="og:title" content="Using Python CGI"/>
	<meta property="og:type" content="article" />
	<link rel="alternate" type="application/rss+xml" href="/~ms9144/database/feed.xml" title="Blog RSS Feed">
	</head>
	<body>
		<div class="header">
	<ul>
	<li><a href="/~ms9144">Bellisimon's</a></li>
	<li><a href="/~ms9144/database/">Database Design and Web Implementation</a></li>
	</ul>
	</div>



	<div class="pageContent">
	<div class="logo">
	<a href="http://i6.cims.nyu.edu"><img src="/~ms9144/database/img/logo.png"></a>
	</div>
	<h1 class="postTitle">Using Python CGI</h1>
	<div class="postDescription"><i>21 October 2017</i></div>

	<article>
	<h1>U.S.  Flights Delay Records</h1>""")

def endPage():
	print("""</article>

	</div>
	<div class="feed">
	<a type="application/rss+xml" href="/~ms9144/database/feed.xml">RSS Feed</a>
	</div>
	</body>
	</html>""")

if __name__ == '__main__':
	main()


