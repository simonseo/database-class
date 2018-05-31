Currently this database holds few renowned works of photographers that I admire, as well as works by myself. This is meant to be used for test data and as such, descriptions for the photographers and mediums are brought in from unreliable sources and I made a lot of fictional assumptions about each work, due to lack of information about each work as well as for the sake of database integrity at the current level.
This webpage is created as part of a project for designing and creating a LAMP stack website. It is a catalogue of photographers and photos. Users are able to choose whose works and which mediums that they wish to see. I created this for photographers practicing different mediums. For example, I recently became interested in film cameras. Looking at works of my role models who used the film medium would be helpful for me to know what kind of photos I should aim for in the beginning.



select (optional) artist
select (optional) medium
see newest/oldest photos first
see albhabetical/youngest/oldest people first
check to see if either artist or medium is selected.

If there are no results, print no results.



photographers (all photographers)
aid
name: annie leibovitz, simon seo, Linda McCartney, todd selby
birthdate
deathdate (null if alive)
description
website

photos (all photos)
pid
title
aid
date/year (null if unknown)
description
cdn

medium (all mediums existing in the world)
mid
name: film digital phone dslr paper a4 canvas copper
description

photomedium (multiple mediums per photo)
pid
mid