CREATE TABLE student_grades 
	(Student_Number INT NOT NULL,
	ClassOf INT NOT NULL,
	LastFirst VARCHAR,
	Course_Name VARCHAR(30),
	Course_Number INT NOT NULL,
	EarnedCrHrs INT NOT NULL,
	Grade VARCHAR,
	Grade_Level INT NOT NULL,
	StudentID INT NOT NULL,
	Teacher_Name VARCHAR,
	GradeScale_Name VARCHAR,
	GPA_Points INT,
	Percent REAL,
	StoreCode VARCHAR,
	ExcludeFromGPA INT,
	GPA_AddedValue INT,
	SectionID INT,
	ExcludeFromTranscripts BOOLEAN,
	TermID INT,
	PRIMARY KEY (StudentID, Course_Name)
);
	
CREATE TABLE test_ID 
	(ID INT NOT NULL,
	name VARCHAR(4),
	description VARCHAR,
	PRIMARY KEY (ID)
			);
					
CREATE TABLE test_scores
	(ID INT NOT NULL,
	studentID INT,
	test_ID INT,
	score INT,
	PRIMARY KEY (ID),
	FOREIGN KEY (studentID) REFERENCES student_grades (StudentID)
	);
	
DROP TABLE student_grades CASCADE;

SELECT ts.studentID, tID.name, tID.description, ts.score
INTO test_results
FROM test_scores AS ts
LEFT JOIN test_ID AS tID
ON (ts.test_ID = tID.ID)
WHERE (ts.test_ID = 66 OR ts.test_ID = 52 OR ts.test_ID = 53 OR ts.test_ID = 51)
;

SELECT sg.Student_Number AS ID, sg.Course_Name AS Course_Name, sg.Course_Number AS Course_Number, sg.Grade AS Grade, sg.Teacher_Name AS Teacher,
	tr.name AS Abbreviation, tr.description AS Test_Name, tr.score AS Test_Score
INTO compile
FROM test_results AS tr
LEFT JOIN student_grades AS sg
ON (tr.studentid = sg.StudentID)
WHERE sg.ClassOf <= 2024
ORDER BY id;

SELECT *
FROM student_grades
WHERE studentid = 10843;

--did for all 4 tests and 211 and 115
SELECT c.abbreviation AS test_code, c.test_score AS HSPT_Score, c.test_name AS test_name, sg.percent AS grade_percent, sg.course_number AS course
INTO MTNP_115
FROM compile AS c
INNER JOIN student_grades AS sg
ON (c.id = sg.student_number)
WHERE c.abbreviation = 'MTNP' AND sg.course_number = 115;

--avg of HSPT
SELECT c.abbreviation AS test_code, c.test_score AS HSPT_Score, c.test_name AS test_name, sg.percent AS grade_percent, sg.course_number AS course
INTO all_tests_courses
FROM compile AS c
INNER JOIN student_grades AS sg
ON (c.id = sg.student_number)
WHERE sg.course_number = 211 OR sg.course_number = 115;