---
layout: post
title: "LAMP Website"
description: Using LAMP stack to make a interactive webpage
---
<h1>Photographers and their mediums of expression</h1>

Currently this database holds few renowned works of photographers that I admire, as well as works by myself. This is meant to be used for test data and as such, descriptions for the photographers and mediums are brought in from unreliable sources and I made a lot of fictional assumptions about each work, due to lack of information about each work as well as for the sake of database integrity at the current level.

This webpage is created as part of a project for designing and creating a LAMP stack website. It is a catalogue of photographers and photos. Users are able to choose whose works and which mediums that they wish to see. I created this for photographers practicing different mediums. For example, I recently became interested in film cameras. Looking at works of my role models who used the film medium would be helpful for me to know what kind of photos I should aim for in the beginning.

I recommend you check out 

1. Annie Leibovitz's works in all mediums
1. All artists' works in canvas medium
1. All artists' works in film medium

<hr>
<form name="photos" action="resources/submit_photos.py" method="POST">
	<fieldset>
	<legend>Options</legend>
	<div>
		<label for="artists">Whose photos do you want to see?</label>
		<select name="artists" id="artists">
			<option value="Annie">Annie Leibovitz</option>
			<option value="Todd">Todd Selby</option>
			<option value="Simon">Simon Myunggun Seo</option>
			<option value="Linda">Linda McCartney</option>
			<option value="all">all</option>
		</select>
	</div>
	<div>
		<label for="mediums">Photos of what mediums do you want to see?</label>
		<select name="mediums" id="mediums">
			<option value="Film">Film</option>
			<option value="Digital">Digital</option>
			<option value="DSLR">DSLR</option>
			<option value="Smartphone">Smartphone</option>
			<option value="Paper">Paper</option>
			<option value="Canvas">Canvas</option>
			<option value="Copperplate">Copperplate</option>
			<option value="all">all</option>
		</select>
	</div>
	<div>
		<label for="sortBy">How do you want to sort the photos?</label>
		<select name="sortBy" id="sortBy">
			<option value="p.p_yearTaken">Year the photos were taken</option>
			<option value="-a.a_yearBorn">Age of photographers</option>
			<option value="p.p_title">Alphabetical order of photo titles</option>
		</select>
		<select name="ordering" id="ordering">
			<option value="ASC">Ascending</option>
			<option value="DESC">Descending</option>
		</select>
	</div>
	</fieldset>
	<hr class="pbreak" />
	<div style="text-align: center;">
		<input type="submit" value="SUBMIT" style="text-align: center;">
		<input type="reset" value="RESET" style="text-align: center;">
	</div>
</form>