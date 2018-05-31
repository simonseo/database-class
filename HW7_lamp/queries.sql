/*
* @Author: seo
* @Date:   2017-12-11 02:33:42
* @Last Modified by:   Simon Seo
* @Last Modified time: 2017-12-12 02:13:12
*/
-- CREATE TABLE photographers (
--   aid INT(4) NOT NULL,
--   a_name VARCHAR(32) NOT NULL,
--   a_yearBorn INT(4) NULL DEFAULT 0,
--   a_yearDied INT(4) NULL DEFAULT 0,
--   a_desc VARCHAR(1000) NULL DEFAULT NULL,
--   a_website VARCHAR(200) NULL DEfAULT NULL,

-- CREATE TABLE photos (
--   pid INT(4) NOT NULL,
--   p_title VARCHAR(32) NOT NULL,
--   aid INT(4) NOT NULL,
--   p_yearTaken INT(4) NULL DEFAULT 0,
--   p_desc VARCHAR(1000) NULL DEFAULT NULL,
--   p_cdn VARCHAR(300) NULL DEfAULT NULL,

-- CREATE TABLE mediums (
--   mid INT(4) NOT NULL,
--   m_name VARCHAR(32) NOT NULL,
--   m_desc VARCHAR(1000) NULL DEFAULT NULL,

-- CREATE TABLE photomediums (
--   pmid INT(4) NOT NULL,
--   pid INT(4) NOT NULL,
--   mid INT(4) NOT NULL,


SELECT p.p_title, p.p_yearTaken, a.a_name, a.aid, m.m_name, a.a_website, p.p_cdn
FROM photographers a
 INNER JOIN photos p ON p.aid = a.aid
 INNER JOIN photomediums pm ON pm.pid = p.pid
 INNER JOIN mediums m ON pm.mid = m.mid
WHERE a.a_name LIKE '%Simon%'
GROUP BY p.pid
;

SELECT p.p_title, p.p_yearTaken, p.p_cdn, p.p_desc, a.a_name, a.a_yearBorn, a.a_website, m.m_name, m.m_desc
FROM photographers a
 INNER JOIN photos p ON p.aid = a.aid
 INNER JOIN photomediums pm ON pm.pid = p.pid
 INNER JOIN mediums m ON pm.mid = m.mid
WHERE a.a_name LIKE '%Simon%'
-- GROUP BY p.pid
LIMIT 1
;
