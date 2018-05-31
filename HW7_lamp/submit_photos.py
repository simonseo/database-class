#!/usr/local/bin/python3

import cgi
import cgitb
cgitb.enable()

import pymysql
import os
from credentials import *

def main():
	startPage()
	try:
		connection = pymysql.connect(host,user,passwd,db,charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
	except Exception as e:
		print('Error in connecting to SQL server.')
		raise e
	else:
		c = connection.cursor()
		form = cgi.FieldStorage()

	# Retrieve values from the form
	aName = form.getvalue('artists')
	mName = form.getvalue('mediums')
	sortBy = form.getvalue('sortBy')
	ordering = form.getvalue('ordering')

	# Build query and execute it
	query = '''SELECT p.p_title, p.p_yearTaken, p.p_cdn, p.p_desc, a.a_name, a.a_yearBorn, a.a_website, m.m_name, m.m_desc
FROM photographers a
 INNER JOIN photos p ON p.aid = a.aid
 INNER JOIN photomediums pm ON pm.pid = p.pid
 INNER JOIN mediums m ON pm.mid = m.mid
WHERE a.a_name LIKE '%{aName}%'
  AND m.m_name LIKE '%{mName}%'
GROUP BY p.pid
ORDER BY {sortBy} {ordering}
'''.format(aName=aName if aName != 'all' else '', mName=mName if mName != 'all' else '', sortBy=sortBy, ordering=ordering)
	
	try:
		c.execute(query)
		rs = c.fetchall()
	except Exception as e:
		print('Error while executing query {}'.format(query))
		raise e

	# Display the query results
	for r in rs:
		pDesc = '{}\nThis photo was taken in {} medium. {}'.format(r['p_desc'], r['m_name'], r['m_desc'])
		print(photoBox(r['a_name'], r['a_website'], r['p_title'], r['p_cdn'], pDesc, r['p_yearTaken']))
	if r is None:
		print('<h4>The search did not produce any results.</h4>')
	endPage()

def startPage():
	print ("Content-Type: text/html\r\n\r\n")
	print("""<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="description" content="Using LAMP stack to make a interactive webpage">
		<title>LAMP Website</title>
		<link rel="stylesheet" href="/~ms9144/database/css/style.css">
		<meta property="og:title" content="LAMP Website"/>
		<meta property="og:type" content="article" />
		<link rel="alternate" type="application/rss+xml" href="/~ms9144/database/feed.xml" title="Blog RSS Feed">
		<style>
			.photobox {
				border-radius: 10px;
				box-shadow: rgba(0,0,0,0.1) 1px 1px 5px;
			}
			.photobox-artist {
				height: 10%;
				border-bottom: #00000017 1px solid;
			}
			.photobox-artist h3 {
				margin-left: 7%;
				padding-top: 4%;
			}
			.photobox-photo {
				padding-top: 4%;
				width: 100%;
			}
			.photobox-photo a {
				display: block;
			}
			.photobox-photo img {
				max-width: 80%;
				max-height: 400px;
				display: block;
				margin: 0 auto;
			}
			.photobox-description {
				padding-bottom: 4%;
			}
			.photobox-date {
				font-weight: bolder;
			}
		</style>
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
			<h1 class="postTitle">Photographers and their mediums of expression</h1>
			<div class="postDescription"><i>4 December 2017</i></div>

			<article>
				<h1>Search Results</h1>""")

def endPage():
	print("""		</article>

		</div>
		<div class="feed">
			<a type="application/rss+xml" href="/~ms9144/database/feed.xml">RSS Feed</a>
		</div>
	</body>
	</html>""")

def photoBox(aName, aWeb, pTitle, pCdn, pDesc, pDate):
	return '''<div class="photobox">
	<div class="photobox-artist">
		<a href="{artistWebsite}"><h3>{artistName} - {photoTitle}</h3></a>
	</div>
	<div class="photobox-photo">
		<a href="{photoLink}"><img src="{photoLink}"></a>
	</div>
	<div class="photobox-description">
		<p class="photobox-desc">{photoDescription}</p>
		<p>Photo taken in <span class="photobox-date">{photoDate}</span></p>
	</div>
	</div>'''.format(artistWebsite=aWeb, artistName=aName, photoTitle=pTitle, photoLink=pCdn, photoDescription=pDesc, photoDate=pDate)

if __name__ == '__main__':
	main()


