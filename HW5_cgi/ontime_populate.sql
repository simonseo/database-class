-- CSCI-UA.60-1 Myunggun Seo
-- 2017 July Data of Flight Delays in US
-- Data Source: https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time

DROP TABLE IF EXISTS ontime;
CREATE TABLE ontime (
  FL_DATE text,
  UNIQUE_CARRIER text,
  FL_NUM integer,
  ORIGIN_AIRPORT_ID integer,
  ORIGIN_AIRPORT_SEQ_ID integer,
  ORIGIN_CITY_MARKET_ID integer,
  ORIGIN text,
  ORIGIN_CITY_NAME text,
  DEST_AIRPORT_ID integer,
  DEST_AIRPORT_SEQ_ID integer,
  DEST_CITY_MARKET_ID integer,
  DEST text,
  DEST_CITY_NAME text,
  CRS_DEP_TIME text,
  DEP_TIME text,
  DEP_DELAY real,
  CRS_ARR_TIME text,
  ARR_TIME text,
  ARR_DELAY real,
  CRS_ELAPSED_TIME real,
  ACTUAL_ELAPSED_TIME real,
  AIR_TIME real,
  FLIGHTS real,
  DISTANCE real,
  DISTANCE_GROUP integer,
  CARRIER_DELAY real,
  WEATHER_DELAY real,
  NAS_DELAY real,
  SECURITY_DELAY real,
  LATE_AIRCRAFT_DELAY real
  );

.mode csv
.import ontime.csv ontime
.mode column
.header on

-- DELETE Header row
.print "Deleting header row"
DELETE FROM ontime WHERE FL_DATE NOT LIKE "20%";





