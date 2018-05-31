DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS clubs;
DROP TABLE IF EXISTS memberInfo;

CREATE TABLE students (
  st_netID VARCHAR(10) NOT NULL,
  st_name VARCHAR(30) NOT NULL,
  st_major VARCHAR(30) NOT NULL,
  st_mobile VARCHAR(10) NOT NULL,
  st_secondary_email VARCHAR(30) NOT NULL,
  st_start_date DATE NOT NULL,
  st_grad_date DATE NOT NULL,
  PRIMARY KEY (st_netID)
);

CREATE TABLE clubs (
  cb_id INT(4) NOT NULL,
  cb_name VARCHAR(10) NOT NULL,
  cb_affil VARCHAR(30) NOT NULL,
  cb_email VARCHAR(30) NOT NULL,
  cb_url VARCHAR(40) NOT NULL,
  cb_description VARCHAR(200) NOT NULL,
  cb_meeting_space VARCHAR(40) NOT NULL,
  cb_entry_due INT(3) NOT NULL,
  cb_president VARCHAR(10) NOT NULL,
  cb_secretary VARCHAR(10) NOT NULL,
  cb_treasurer VARCHAR(10) NOT NULL,
  PRIMARY KEY (cb_id),
  CONSTRAINT
    FOREIGN KEY (cb_president)
    REFERENCES students (st_netID),
  CONSTRAINT
    FOREIGN KEY (cb_secretary)
    REFERENCES students (st_netID),
  CONSTRAINT
    FOREIGN KEY (cb_treasurer)
    REFERENCES students (st_netID)
);

CREATE TABLE memberInfo (
  mi_id INT(8) NOT NULL,
  mi_join_date DATE NOT NULL,
  mi_resig_date DATE NULL DEFAULT NULL,
  mi_netID VARCHAR(10) NOT NULL,
  mi_clubID INT(4) NOT NULL,
  PRIMARY KEY (mi_id),
  CONSTRAINT
    FOREIGN KEY (mi_netID)
    REFERENCES students (st_netID),
  CONSTRAINT
    FOREIGN KEY (mi_clubID)
    REFERENCES clubs (cb_id)
);
