---
layout: post
title: "Using Python CGI"
description: Using the CGI library to work with HTML forms and SQL database in frontend
---
<h1>U.S.  Flights Delay Records</h1>

This is a July 2017 Data of all domestic flights within the U.S. It contains information of the flights including the plane, origin, destination, and especially the times and delays.

This data is open to the public, on the website of Bureau of Transportation Statistics. This organization is a branch of the United States Department of Transportations and is maintained very well. The data is only a couple months behind and has great documentation including descriptions of each field, which already only uses official terms, and descriptions of values in each field. The bureau also provides information on which data is missing and why. Thus this data seems to be very reliable.

<hr>
<form name="ontime" action="resources/submit.py" method="POST">
	<fieldset>
	<legend>Options</legend>
	<div>
		<label for="carrier">See data for which carrier?</label>
		<select name="carrier" id="carrier">
			<option value="AS">AS</option>
			<option value="OO">OO</option>
			<option value="AA">AA</option>
			<option value="HA">HA</option>
			<option value="VX">VX</option>
			<option value="B6">B6</option>
			<option value="UA">UA</option>
			<option value="WN">WN</option>
			<option value="EV">EV</option>
			<option value="NK">NK</option>
			<option value="F9">F9</option>
			<option value="DL">DL</option>
			<option value="all">all</option>
		</select>
	</div>
	<div>
		<label for="limitTo">How many rows do you want to see?</label>
		<select name="limitTo" id="limitTo">
			<option value="10">10</option>
			<option value="25">25</option>
			<option value="50">50</option>
			<option value="100">100</option>
			<option value="200">200</option>
			<option value="all">all</option>
		</select>
	</div>
	<div>
		<label for="sortBy">What row do you want to sort by?</label>
		<select name="sortBy" id="sortBy">
			<option value="FL_DATE">Flight Date</option>
			<option value="FL_CODE">Flight Code</option>
			<option value="ORIGIN_TXT">Origin Airport</option>
			<option value="DEST_TXT">Destination Airport</option>
			<option value="CRS_DEP_TIME">Scheduled Departure</option>
			<option value="DEP_TIME">Actual Departure</option>
			<option value="DEP_DELAY">Departure Delay</option>
			<option value="CRS_ARR_TIME">Scheduled Arrival</option>
			<option value="ARR_TIME">Actual Arrival</option>
			<option value="ARR_DELAY">Arrival Delay</option>
			<option value="CRS_ELAPSED_TIME">Scheduled Elapsed Time</option>
			<option value="ACTUAL_ELAPSED_TIME">Acutal Elapsed Time</option>
		</select>
		<select name="ordering" id="ordering">
			<option value="ASC">Ascending</option>
			<option value="DESC">Descending</option>
		</select>
	</div>
	</fieldset>
	<fieldset>
		<legend>Choose fields you want to see</legend>
			<div><label><input type="checkbox" name="field" value="FL_DATE" checked>Flight Date</label></div>
			<div><label><input type="checkbox" name="field" value="FL_CODE" checked onclick='this.checked = !this.checked'>Flight Code (must check)</label></div>
			<div><label><input type="checkbox" name="field" value="ORIGIN_TXT" checked>Origin Airport</label></div>
			<div><label><input type="checkbox" name="field" value="DEST_TXT" checked>Destination Airport</label></div>
			<div><label><input type="checkbox" name="field" value="CRS_DEP_TIME">Scheduled Departure</label></div>
			<div><label><input type="checkbox" name="field" value="DEP_TIME">Actual Departure</label></div>
			<div><label><input type="checkbox" name="field" value="DEP_DELAY">Departure Delay</label></div>
			<div><label><input type="checkbox" name="field" value="CRS_ARR_TIME">Scheduled Arrival</label></div>
			<div><label><input type="checkbox" name="field" value="ARR_TIME">Actual Arrival</label></div>
			<div><label><input type="checkbox" name="field" value="ARR_DELAY">Arrival Delay</label></div>
			<div><label><input type="checkbox" name="field" value="CRS_ELAPSED_TIME">Scheduled Elapsed Time</label></div>
			<div><label><input type="checkbox" name="field" value="ACTUAL_ELAPSED_TIME">Actual Elapsed Time</label></div>
	</fieldset>
	<hr class="pbreak" />
	<input type="submit" value="SUBMIT" style="text-align: center;">
	<input type="reset" value="RESET" style="text-align: center;">
</form>