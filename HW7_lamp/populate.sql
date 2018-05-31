DROP TABLE IF EXISTS photographers;
CREATE TABLE photographers (
  aid INT(4) NOT NULL,
  a_name VARCHAR(32) NOT NULL,
  a_yearBorn INT(4) NULL DEFAULT 0,
  a_yearDied INT(4) NULL DEFAULT 0,
  a_desc VARCHAR(1000) NULL DEFAULT NULL,
  a_website VARCHAR(200) NULL DEfAULT NULL,
  PRIMARY KEY (aid));

LOAD DATA LOCAL INFILE 'photographers.csv'
INTO TABLE photographers
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM photographers;



DROP TABLE IF EXISTS photos;
CREATE TABLE photos (
  pid INT(4) NOT NULL,
  p_title VARCHAR(100) NOT NULL,
  aid INT(4) NOT NULL,
  p_yearTaken INT(4) NULL DEFAULT 0,
  p_desc VARCHAR(1000) NULL DEFAULT NULL,
  p_cdn VARCHAR(300) NULL DEfAULT NULL,
  PRIMARY KEY (pid),
  CONSTRAINT
    FOREIGN KEY (aid)
    REFERENCES photographers (aid));

LOAD DATA LOCAL INFILE 'photos.csv'
INTO TABLE photos
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM photos;


DROP TABLE IF EXISTS mediums;
CREATE TABLE mediums (
  mid INT(4) NOT NULL,
  m_name VARCHAR(32) NOT NULL,
  m_desc VARCHAR(1000) NULL DEFAULT NULL,
  PRIMARY KEY (mid));

LOAD DATA LOCAL INFILE 'mediums.csv'
INTO TABLE mediums
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM mediums;



DROP TABLE IF EXISTS photomediums;
CREATE TABLE photomediums (
  pmid INT(4) NOT NULL,
  pid INT(4) NOT NULL,
  mid INT(4) NOT NULL,
  PRIMARY KEY (pmid),
  CONSTRAINT
    FOREIGN KEY (pid)
    REFERENCES photos (pid),
  CONSTRAINT
    FOREIGN KEY (mid)
    REFERENCES mediums (mid));

LOAD DATA LOCAL INFILE 'photomediums.csv'
INTO TABLE photomediums
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM photomediums;

