---
layout: post
title: "Visualizing Data of Endangered Species"
description: Visualizing Data as Tables, Geographical Maps, and Bar Graphs using plotly
---

Last week, I scraped data from the [U.S. Fish & Wildlife Service ECOS Environmental Conservation Online System](https://ecos.fws.gov/ecp/) and <a href="i6.cims.nyu.edu/~ms9144/external/Species_All.htm">mirrored</a> it on this website. This data consists of plants and animals that have been mentioned in the Federal Registers for regarding their threatened existence. In other words, this is a loosely tied list of orgnaisms that were possibly considered to be threatened or endangered by some individuals. Of these species, few organisms were put to review and finally listed in the "Federal Listing" of endangered and threatened species. 

I was interested in which kind of species got more attention by academics, administrators, conservationists, etc. Are they the cuter ones? Or the ones that are in places with high biodiversity? Or the ones that are threatened by human activity most?

To answer these questions I had to reorganize the data. I have more than 9,000 species and I cannot try to figure it out just by scrolling through the data. First, I decided to see if the geographical location matters. So I wrote a python script to count how many tracked species exist in each state, and how many of those are listed on the US FWS (US Fish & Wildlife Service) as threatened or endangered.

![Table of endangered species grouped by states](resources/00_table_states.png)
Data from [U.S. Fish & Wildlife Service ECOS Environmental Conservation Online System](https://ecos.fws.gov/ecp/) <a href="i6.cims.nyu.edu/~ms9144/external/Species_All.htm">[Mirror]</a>
The above is the reformatted data of species by state in Alphabetical order. 'etc' signifies smaller groups of federal listing catgories such as 'under review' or 'delisted' but these are were of little meaning to me and thus grouped them separately. This time I will try to visualize the data and represent it in different ways. I used [plotly](http://plot.ly) for all of the following graphic data in this post.


![](resources/10_map_total.png)
Data from [U.S. Fish & Wildlife Service ECOS Environmental Conservation Online System](https://ecos.fws.gov/ecp/) <a href="i6.cims.nyu.edu/~ms9144/external/Species_All.htm">[Mirror]</a>
In this map we can see that there are a lot of records in the Southwest and less but similar amount in the Southeast. There is almost an aggressively large number of species in the database especially in Hawaii and California. This seems to suggest either that in these regions there are lot of vulnerable species or that people actively scout for such species.

![](resources/11_map_federal.png)
Data from [U.S. Fish & Wildlife Service ECOS Environmental Conservation Online System](https://ecos.fws.gov/ecp/) <a href="i6.cims.nyu.edu/~ms9144/external/Species_All.htm">[Mirror]</a>
This map of number of species in the Federal Listing (US FWS Endangered & Threatened Species) displays a similar trend witht the first map. It seems, and as common sense suggests, that generally the more species that are being tracked in one state, the more species will be put on the Federal Listing. However, since the Federal Listing was much smaller than the entire database, I was curious if researchers were being conservative with the database. It seemed that there were species that might or might not be actually threatened/endangered but they were on the database since more species on the database would be considered better than not, even if they're not threatened/endangered. I was curious if California and Hawaii listed more species than they 'should'. (The word'Should' can be misleading, I think people 'should' put as many species as possible on the database) To check this, I created the following map.

![](resources/12_map_relative.png)
Data from [U.S. Fish & Wildlife Service ECOS Environmental Conservation Online System](https://ecos.fws.gov/ecp/) <a href="i6.cims.nyu.edu/~ms9144/external/Species_All.htm">[Mirror]</a>
This map shows the ratio of species in the databse that were put on the Federal Listing. The map shows that in some states, around a third of the species in the database is recognized federally as threatened or endangered. It is interesting to see that Rhode Island, Mississipi, and Nevada appears darker than most. These states have small number of species both in the database and the Federal Listing but species in these states are more likely to be on the Federal Listing if they already caught the eyes of researchers and was put on this database. On the other hand, California, which had the largest number of species on the database, is mediocre in terms of the ratio of thos species being recognized federally. It could be that entities like conservationists in RI, MS, NE strive to have individual species be recognized at a higher level (quality over quantity) where as entities in CA might strive to have as many species as possible be known but disperse their focus on individual species in doing so.

![](resources/01_table_species.png)
Data from [U.S. Fish & Wildlife Service ECOS Environmental Conservation Online System](https://ecos.fws.gov/ecp/) <a href="i6.cims.nyu.edu/~ms9144/external/Species_All.htm">[Mirror]</a>
I was originally curious about polar bears but since this database provides more information than just polar bears, I decided to see what kind of organisms were listed. There are 20 species groups -- it is good to see that people focus on more than just cute polar bears. 

![](resources/20_bar_sum.png)
Data from [U.S. Fish & Wildlife Service ECOS Environmental Conservation Online System](https://ecos.fws.gov/ecp/) <a href="i6.cims.nyu.edu/~ms9144/external/Species_All.htm">[Mirror]</a>
I ordered all 20 species groups by the size of each group. The number of plants in the database is surprisingly large. While it is known that there are much more plant species than bird or mammal species, this number seemed too big even when compared to insect species. I recall from my experience interning at an ecology research institute that a lot of researchers conduct research on plant species because they are easier to work with since, well, they don't move. This tendency to focus more on plant species might be an explanation for the large number. It could also be that there simply is a lot more plant species or that a lot of plant species are actually endangered.

![](resources/22_bar_endangered.png)
Data from [U.S. Fish & Wildlife Service ECOS Environmental Conservation Online System](https://ecos.fws.gov/ecp/) <a href="i6.cims.nyu.edu/~ms9144/external/Species_All.htm">[Mirror]</a>
This time I ordered all 20 species groups by the number of federally recognized endangered species. It is notable that flowering plants still hold the top place because of their massive number while insect species went lower down the rank because insect species are less likely to be endangered due to their adaptiveness.

![](resources/21_bar_relative.png)
Data from [U.S. Fish & Wildlife Service ECOS Environmental Conservation Online System](https://ecos.fws.gov/ecp/) <a href="i6.cims.nyu.edu/~ms9144/external/Species_All.htm">[Mirror]</a>
I was still curious about whether plant species were listed more because they are more likely to be victims of extinction or because they are easier to work with. So I created a stacked bar graph with each section of the bar representing the relative number of species in each Federal Listing Category and order them in desceding order of ratio of endangered species. This graph provides valuable information. It shows us that advanced species like birds and mammals were most prone to endangerment. I also learned for the first time that clams and fern species were also prone to endangerment. The plants group on the other hand, ranked lower because this group has a high proportion of species that are not on the Federal Listing.
