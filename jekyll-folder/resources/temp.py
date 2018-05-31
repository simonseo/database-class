#!/usr/local/bin/python3

# python/cgi script for the database class schools demo
# variables coming from schools_demo.html: state, quantity, sortKey
#
# 8. Write the python script to retrieve the user's selections
#   along with running the query and to display the results.
#
# a. receive the user selections from the HTML
# b. open a dynamic web page
# c. several imports (e.g. sqlite, cgi, etc)
# d. run the query
# e. display the results of running the query
# f. close the database and finish up

import cgi
import sqlite3

import cgitb ## allow for debugging and good error message
cgitb.enable()


print("Content-Type: text/html\r\n\r\n")
print("your mom")
# print("<html>")
# print("<head>")
# print("<title>Assignemnt 5 - Python CGI data selection</title>")
# print('''<link rel="stylesheet" type="text/css" href="asg5Style.css" >''')
# print("</head>")
# print("<body>")
# print("<h3>These are your results</h3>")
# print("<hr />")
#
# conn = sqlite3.connect('countrydata.db')
# c = conn.cursor()
#
# form = cgi.FieldStorage()
# user_country = form["country"].value
# user_quantity = form["quantity"].value
#
# # create the query:
# #sqlite> SELECT sd_state,sd_name,sd_pop_2010
# #   ...> FROM sd
# #   ...> WHERE sd_state="CT"
# #   ...> ORDER BY sd_pop_2010 DESC
# #   ...> LIMIT 5;
#
# query = "SELECT name,population,area FROM countrydatabase WHERE name = "user_country"
# query += " LIMIT "+user_quantity
# print("<p>Query: "+query+"</p>\n")
# print("<hr />\n")
#
# c.execute(query)
#
# print("<table>")
# print("<tr>")
# print("\t<th>Name</th>")
# print("\t<th>Population</th>")
# print("\t<th>Area</th>")
# print("</tr>")
# # print the data
# for name,population,area in c:
# # Note: in class, this part of the program caused an error.
# # Upon opening this python script on i6 using the editor "pico",
# # it became clear that i6 did not recognize the tab character
# # used by this text editor. When I substituted spaces for the tab
# # character, the program resumed running again.
#
# # Note that this was not a problem that we could see
# # as the file appeared fine in our local text editor.
#
# # Checking your data files and programs on i6 is a standard
# # part of de-bugging in this environment in order to catch
# # these (unusual) anomalies.
#
# #	print("<p>new line</p>")
#     print("<tr>")
#     print("\t<td>"+name+"</td>")
#     print("\t<td>"+str(population)+"</td>")
#     print("\t<td>"+str(area)+"</td>")
#     print("</tr>")
# print("</table>\n")
# c.close()
# print("</body>")
# print("</html>")
