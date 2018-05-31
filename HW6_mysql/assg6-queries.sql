--1
SELECT st_name, st_major, st_netID, st_mobile 
FROM students 
ORDER BY st_name;
-- display the names of all of the students in alphabetical order 
-- along with his/her major, netid and mobile phone number


--2
SELECT cb_name, cb_url, cb_meeting_space 
FROM clubs 
WHERE cb_affil = 'CS';
-- display all of the clubs that are mentored by the Computer Science Department. 
-- Please list the club name, URL and regular meeting location


--3
SELECT cb.cb_id, COUNT(*) AS num, mi.mi_clubID 
FROM clubs cb, memberInfo mi 
WHERE cb.cb_id = mi.mi_clubID 
  AND mi.mi_resig_date IS NULL 
GROUP BY cb.cb_id 
ORDER BY num DESC 
LIMIT 5;
-- display the five clubs with the most members; 
-- list the largest club first and then in descending order by the number of members


--4
SELECT cb.cb_id, cb.cb_name, COUNT(*)*cb.cb_entry_due AS earnings
FROM clubs cb, memberInfo mi 
WHERE cb.cb_id = mi.mi_clubID 
GROUP BY cb.cb_id 
ORDER BY earnings DESC 
LIMIT 1;
-- Which club earned the most from dues to date

--5
SELECT cb_affil, AVG(cb_entry_due) 
FROM clubs 
GROUP BY cb_affil;
-- average cost of dues for each department (in alphabetical order by department)

--6
SELECT CONCAT(st.st_name," - ", COUNT(*)," clubs") as "Number of memberships"
FROM students st INNER JOIN memberInfo mi ON st.st_netID=mi.mi_netID 
WHERE mi.mi_resig_date IS NULL
GROUP BY st.st_name;
-- number of club memberships for each student on file and display the results with the student's name 
-- Do not display students who are not members of any club.

--7
SELECT st_name, membership
FROM (
    SELECT st_name, mi.mi_netID AS membership 
    FROM students st LEFT JOIN memberInfo mi ON st.st_netID = mi.mi_netID 
    GROUP by st.st_name) tmp
WHERE membership IS NULL 
ORDER BY st_name ASC;
-- alphabetically list all students who do not have a membership in any club

--8
SELECT st_name, cnt
FROM (
    SELECT st_name, COUNT(*) AS cnt 
    FROM students st LEFT JOIN memberInfo mi ON st.st_netID = mi.mi_netID 
    GROUP by st.st_name) tmp
WHERE cnt>1 
ORDER BY st_name DESC;
-- This query displays all the students who are members of more than one club

-- 9-1
SELECT pres.cb_id, pres.pres_id, mi.mi_resig_date
FROM (
    SELECT cb.cb_president AS pres_id, cb.cb_id AS cb_id FROM clubs cb) pres
INNER JOIN memberInfo mi ON pres.pres_id=mi.mi_netID AND pres.cb_id=mi.mi_clubID
WHERE mi.mi_resig_date IS NOT NULL;
-- This query displays all the presidents who already left the clubs but are still on the clubs list, 
-- so basically does some error checking.


--9-2
SELECT st_name, st_start_date, st_grad_date 
FROM students 
WHERE st_start_date>st_grad_date
UNION
SELECT st.st_name, mi.mi_join_date, mi.mi_resig_date 
FROM memberInfo mi RIGHT JOIN students st ON mi.mi_netID=st.st_netID 
WHERE mi.mi_join_date>mi.mi_resig_date;
-- This query displays all students who are written as enrolled before they started the school, 
-- so basically does some error checking.
