#!/usr/local/bin/python3

# TASKS:

# 1. set up the html and identify the variable names
## We are using "state" and "numDistricts"
# 2. set up credentials: create a python script to be used later
## This is one of the differences between the way we are using Python with SQLite on i6 vs. MySQL.
# 3. imports (cgi, etc.)

# We agreed in class that steps #4, #5 and #6 could happen in any order:
# 4. connect to the database
# 5. build a query
# 6. set up the web page for output display

# These are the steps to complete the project:
# 7. execute the query
# 8. display the query results (if any) to the webpage 
##   Include a title area with the name of the state and number of districts selected.
# 9. close the connection 

# imports:
import cgi, cgitb
cgitb.enable()

import pymysql
import os
from credentials import *


# Next we will retrieve the values that we need from the HTML form.
# This is the same as when we retrieved values from an HTML form for the Python/SQLite
# classwork and assignment #5.

form = cgi.FieldStorage()
state = form["state"].value
num   = form["numDistricts"].value

query  = '''SELECT sd_name,sd_pop_2010 FROM sd
            WHERE sd_state="{}"
            ORDER BY sd_pop_2010 DESC
            LIMIT {}'''.format(state,num)

# set up the  connection 
# c is for our cursor and r is for our rows
connection = pymysql.connect(host,user,passwd,db,charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)
c =connection.cursor()
c.execute(query)

r = c.fetchall()

# for testing purposes:
# Note that in the first class, we commented out the lines in which we assign the HTML data to the python variables.
# If we do that and then hard-code assignments to the state and num variables, we can test the python program
# by running "python3 ... .py" at the command line.
# print(query)

# set up the web page
print("Content-type: text/html;charset=utf-8")
print("\n\n")

print('''
<!DOCTYPE html>
<html>
  <head>
    <title>LAMP Exercise: Python and MySQL - Fall 2017</title>
    <link href="LAMP_schools.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <h3>School Districts - LAMP programming exercise using Python and MySQL</h3>
    <hr />   
     
    <h4>Hello, World!</h4>
    
''')

print("<p>Query: "+query+"</p>")
print("<hr />")
print("<p><em>Here are the results: </em></p>")

# Add to this print statement to include additional fields and display formatting:
for row in r:
	print('''<p>{}</p>'''.format(row['sd_name']))

print('''
  </body>
</html>
''')
# close the  connection
c.close()
