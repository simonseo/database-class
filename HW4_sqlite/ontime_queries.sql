-- CSCI-UA.60-1 Myunggun Seo
-- 2017 July Data of Flight Delays in US
-- Data Source: https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time

-- 1. Write a query to count how many records there are in your table.
.print "Count records"
SELECT COUNT(*) FROM ontime; --509070





-- 2. Write a query to logically group the data in your table and 
-- print out only the last (or highest) value for each category.
-- We already have a "distance group" field that divides the data into groups of similar flight distances
-- I'll print the distance group and also the delay 
.print "Maximum arrival delay for each distance group"
SELECT 
  DISTANCE_GROUP,
  COUNT(*),
  MAX(ARR_DELAY),
  ORIGIN_CITY_NAME,
  DEST_CITY_NAME
FROM ontime
WHERE ARR_DELAY <> ''
GROUP BY DISTANCE_GROUP
ORDER BY DISTANCE_GROUP;





-- 3. Display three important fields; at least one should be in alphabetical order
SELECT FL_DATE FROM ontime GROUP BY FL_DATE ORDER BY FL_DATE ASC LIMIT 10; --2017-07-01
SELECT FL_DATE FROM ontime GROUP BY FL_DATE ORDER BY FL_DATE DESC LIMIT 10; --2017-07-31

.print "Flight number"
SELECT FL_NUM FROM ontime GROUP BY FL_NUM ORDER BY FL_NUM ASC LIMIT 10; --1
SELECT FL_NUM FROM ontime GROUP BY FL_NUM ORDER BY FL_NUM DESC LIMIT 10; --999
-- I knew from the database specs that FL_NUM is a number with 1~4 digits.
-- This seemed to be an issue because I set FL_NUM as text.
SELECT FL_NUM FROM ontime GROUP BY FL_NUM ORDER BY CAST(FL_NUM as decimal) ASC LIMIT 10; --1
SELECT FL_NUM FROM ontime GROUP BY FL_NUM ORDER BY CAST(FL_NUM as decimal) DESC LIMIT 10; --7439

SELECT ORIGIN FROM ontime GROUP BY ORIGIN ORDER BY ORIGIN ASC LIMIT 10; --ABE
SELECT ORIGIN FROM ontime GROUP BY ORIGIN ORDER BY ORIGIN DESC LIMIT 10; --YUM

.print "Scheduled departure time"
SELECT CRS_DEP_TIME FROM ontime GROUP BY CRS_DEP_TIME ORDER BY CRS_DEP_TIME ASC LIMIT 10; --0001
SELECT CRS_DEP_TIME FROM ontime GROUP BY CRS_DEP_TIME ORDER BY CRS_DEP_TIME DESC LIMIT 10; --2359

SELECT DEP_TIME FROM ontime GROUP BY DEP_TIME ORDER BY DEP_TIME ASC LIMIT 10; --0001
SELECT DEP_TIME FROM ontime GROUP BY DEP_TIME ORDER BY DEP_TIME DESC LIMIT 10; --2400

SELECT DEP_DELAY FROM ontime WHERE DEP_DELAY <> '' ORDER BY DEP_DELAY ASC LIMIT 10; -- -56.0
SELECT DEP_DELAY FROM ontime WHERE DEP_DELAY <> '' ORDER BY DEP_DELAY DESC LIMIT 10; -- N/A, next is 1916.0

SELECT DISTANCE FROM ontime GROUP BY DISTANCE ORDER BY DISTANCE ASC LIMIT 10; --31.0 Wrangell, AK to Petersburg, AK
SELECT DISTANCE FROM ontime GROUP BY DISTANCE ORDER BY DISTANCE DESC LIMIT 10; --4983.0 New York to Honolulu




-- 4. Use GROUP BY to find averages on a numerical field in a reasonable breakdown.
.print "Average departure and arrival delay for each distance group"
SELECT 
  DISTANCE_GROUP,
  COUNT(*),
  AVG(DEP_DELAY),
  AVG(ARR_DELAY)
FROM ontime
WHERE ARR_DELAY <> ''
GROUP BY DISTANCE_GROUP
ORDER BY DISTANCE_GROUP;





-- 5. Create a user-friendly listing of the first 15 records in alphabetical order by creating a text field using concatenation
SELECT 
  UNIQUE_CARRIER || FL_NUM || " from " || ORIGIN_CITY_NAME || " to " || DEST_CITY_NAME AS txt, 
  COUNT(*)
FROM ontime
WHERE ARR_DELAY <> ''
GROUP BY txt
ORDER BY UNIQUE_CARRIER || substr('0000' || FL_NUM, -4, 4)
LIMIT 15;





-- 6. How many flights did the top 5 airlines account for?
-- 6-1. How many flights did each of the top 5 airlines operate?
SELECT *
FROM (
    SELECT 
      UNIQUE_CARRIER, 
      COUNT(*) AS cnt
    FROM ontime
    GROUP BY UNIQUE_CARRIER
    ORDER BY cnt DESC
    ) t
    LIMIT 5;

-- 6-2. How many flights did the top 5 airlines opearate in total?
SELECT SUM(top.cnt)
FROM (
    SELECT 
      UNIQUE_CARRIER, 
      COUNT(*) AS cnt
    FROM ontime
    GROUP BY UNIQUE_CARRIER
    ORDER BY cnt DESC
    LIMIT 5
    ) top;

-- 6-3. What percentage of all US flights is operated by the top 5 airlines?
SELECT
  SUM(top.cnt) AS "Flights Operated by Top 5 Airlines",
  total.cnt AS "Total Flight in U.S.",
  round(100*CAST(SUM(top.cnt) AS float)/CAST(total.cnt AS float), 2) AS "Percentage"
FROM
  (
    SELECT 
      UNIQUE_CARRIER, 
      COUNT(*) AS cnt
    FROM ontime
    GROUP BY UNIQUE_CARRIER
    ORDER BY cnt DESC
    LIMIT 5
    ) top,
  (
    SELECT COUNT(*) as cnt
    FROM ontime
    ) total;

-- 6-4. What percentage does each top 5 airline account for
SELECT
  top.UNIQUE_CARRIER,
  top.cnt AS "Flights Operated by Top 5 Airlines",
  total.cnt AS "Total Flight in U.S.",
  round(100*CAST(top.cnt AS float)/CAST(total.cnt AS float), 2) AS "Percentage"
FROM
  (
    SELECT 
      UNIQUE_CARRIER, 
      COUNT(*) AS cnt
    FROM ontime
    GROUP BY UNIQUE_CARRIER
    ORDER BY cnt DESC
    LIMIT 5
    ) top,
  (
    SELECT COUNT(*) as cnt
    FROM ontime
    ) total;




-- 7. How many flights flew out of top 10 airports?
-- 7-1. Individually
SELECT
  top.ORIGIN AS "Origin Airport Code",
  top.city AS "City of Origin",
  top.cnt AS "Flights that flew out",
  total.cnt AS "Total Flights in U.S.",
  round(100*CAST(top.cnt AS float)/CAST(total.cnt AS float),2) AS Percentage
FROM
  (
    SELECT 
      ORIGIN, 
      ORIGIN_CITY_NAME AS city, 
      COUNT(*) AS cnt
    FROM ontime
    GROUP BY ORIGIN
    ORDER BY cnt DESC
    LIMIT 10
    ) top,
  (
    SELECT COUNT(*) AS cnt
    FROM ontime
    ) total;

-- 7-2. All of top 10 airports
SELECT
  SUM(top.cnt) AS "Total Flights from top 10 airports",
  total.cnt AS "Total Flights in U.S.",
  round(100*CAST(SUM(top.cnt) AS float)/CAST(total.cnt AS float),2) AS Percentage
FROM
  (
    SELECT COUNT(*) AS cnt
    FROM ontime
    GROUP BY ORIGIN
    ORDER BY cnt DESC
    LIMIT 10
    ) top,
  (
    SELECT COUNT(*) AS cnt
    FROM ontime
    ) total;





-- 8. How delayed were departures from busy airports? What is the average delay at busy airports?
-- We can see that it's not very related to "how many" flights there are
-- 8-1. Sorted by number of flights
SELECT
  top.ORIGIN AS "Origin Airport",
  top.city AS "City of Origin",
  top.cnt AS "# of Departures",
  round(top.delay, 2) AS "Average Departure Delay (min)"
FROM
  (
    SELECT 
      COUNT(*) AS cnt, 
      AVG(DEP_DELAY) as delay, 
      ORIGIN, 
      ORIGIN_CITY_NAME AS city
    FROM ontime
    GROUP BY ORIGIN
    ORDER BY cnt DESC
    LIMIT 50
    ) top;

-- 8-2. Sorted by delay
SELECT
  top.ORIGIN AS "Origin Airport",
  top.city AS "City of Origin",
  top.cnt AS "# of Departures",
  round(top.delay, 2) AS "Average Departure Delay (min)"
FROM
  (
    SELECT 
      COUNT(*) AS cnt, 
      AVG(DEP_DELAY) as delay, 
      ORIGIN, 
      ORIGIN_CITY_NAME AS city
    FROM ontime
    GROUP BY ORIGIN
    ORDER BY delay DESC
    LIMIT 50
    ) top;





-- 9. Which carrier was the most delayed?
-- 9-1. Sorted by departure delay
SELECT
  top.UNIQUE_CARRIER AS "Carrier Code",
  top.cnt AS "# of flights",
  round(top.delay, 2) AS "Average Departure Delay (min)"
FROM
  (
    SELECT 
      COUNT(*) AS cnt, 
      AVG(DEP_DELAY) as delay, 
      UNIQUE_CARRIER
    FROM ontime
    GROUP BY UNIQUE_CARRIER
    ORDER BY delay DESC
    ) top;

-- 9-2. Sorted by Arrival delay
SELECT
  top.UNIQUE_CARRIER AS "Carrier Code",
  top.cnt AS "# of flights",
  round(top.delay, 2) AS "Average Arrival Delay (min)"
FROM
  (
    SELECT 
      COUNT(*) AS cnt, 
      AVG(ARR_DELAY) as delay, 
      UNIQUE_CARRIER
    FROM ontime
    GROUP BY UNIQUE_CARRIER
    ORDER BY delay DESC
    ) top;

-- 10. Which are not null vals?
SELECT COUNT(*) FROM ontime WHERE ARR_DELAY = "";
SELECT COUNT(*) FROM ontime WHERE DEP_DELAY = "";
SELECT COUNT(*) FROM ontime WHERE DEP_DELAY = "" OR ARR_DELAY = "";
SELECT COUNT(*) FROM ontime WHERE DEP_DELAY <> "" AND ARR_DELAY = "";

-- 11. Which flight number was busiest?
SELECT 
  UNIQUE_CARRIER || FL_NUM as FL_CODE,
  ORIGIN_CITY_NAME || " to " || DEST_CITY_NAME,
  COUNT(*) as cnt
FROM ontime
WHERE ARR_DELAY <> '' AND DEP_DELAY <> ''
GROUP BY UNIQUE_CARRIER || substr('0000' || FL_NUM, -4, 4) || ":" || ORIGIN || DEST
ORDER BY cnt DESC

-- 11-2. There are too many that operate once a day. How many are there?
SELECT
  t.cnt,
  COUNT(t.cnt)
FROM (
  SELECT 
    UNIQUE_CARRIER || FL_NUM as FL_CODE,
    ORIGIN_CITY_NAME || " to " || DEST_CITY_NAME,
    COUNT(*) as cnt
  FROM ontime
  WHERE ARR_DELAY <> '' AND DEP_DELAY <> ''
  GROUP BY UNIQUE_CARRIER || substr('0000' || FL_NUM, -4, 4) || ":" || ORIGIN || DEST
  ORDER BY cnt DESC
  ) t
GROUP BY t.cnt
ORDER BY t.cnt DESC