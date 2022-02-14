CREATE TABLE demographics
	(student_number INT NOT NULL,
	 gpa_academic REAL,
	 gpa_academicW REAL,
	 gpa_total REAL,
	 gpa_totalW REAL,
	 religion VARCHAR,
	 ethnicity VARCHAR,
	 middle_school VARCHAR,
	 school_type VARCHAR,
	 PRIMARY KEY (student_number)
	 );

CREATE TABLE rhetoric_history_grade
	(student_number INT NOT NULL,
	course_number INT NOT NULL,
	grade VARCHAR NOT NULL,
	teacher VARCHAR NOT NULL,
	percent REAL,
	storecode VARCHAR(2),
	PRIMARY KEY (student_number, course_number)
);

CREATE TABLE music_grade
	(student_number INT NOT NULL,
	course_number INT NOT NULL,
	grade VARCHAR NOT NULL,
	teacher VARCHAR NOT NULL,
	percent REAL,
	storecode VARCHAR(2),
	PRIMARY KEY (student_number, course_number, storecode)
);

CREATE TABLE courses
	(course_number INT,
	course_name VARCHAR,
	PRIMARY KEY (course_number, course_name)
);

--queires
--religion for 115
SELECT d.religion
INTO rhetoric_religion
FROM demographics AS d
LEFT JOIN rhetoric_history_grade AS rhg
ON (d.student_number = rhg.student_number)
WHERE rhg.course_number = 115;

--religion for 211
SELECT d.religion
INTO history_religion
FROM demographics AS d
LEFT JOIN rhetoric_history_grade AS rhg
ON (d.student_number = rhg.student_number)
WHERE rhg.course_number = 211;

--rhetoric/history crossover to music
SELECT rhg.course_number, COUNT(rhg.student_number)/2
FROM rhetoric_history_grade AS rhg
INNER JOIN music_grade AS mg
ON (rhg.student_number = mg.student_number)
GROUP BY rhg.course_number;

--school type for 115
SELECT d.school_type, 1
INTO rhetoric_school_type
FROM demographics AS d
LEFT JOIN rhetoric_history_grade AS rhg
ON (d.student_number = rhg.student_number)
WHERE rhg.course_number = 115;

--school type for 211
SELECT d.school_type, 1
INTO history_school_type
FROM demographics AS d
LEFT JOIN rhetoric_history_grade AS rhg
ON (d.student_number = rhg.student_number)
WHERE rhg.course_number = 211;

--ethnicity for 115
SELECT d.ethnicity, 1 AS count
INTO rhetoric_ethnicity
FROM demographics AS d
LEFT JOIN rhetoric_history_grade AS rhg
ON (d.student_number = rhg.student_number)
WHERE rhg.course_number = 115;

--ethnicity for 211
SELECT d.ethnicity, 1
INTO history_ethnicity
FROM demographics AS d
LEFT JOIN rhetoric_history_grade AS rhg
ON (d.student_number = rhg.student_number)
WHERE rhg.course_number = 211;