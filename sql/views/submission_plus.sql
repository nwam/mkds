SELECT q0.submissionID, q0.date AS date, course.courseID as courseID, q0.course AS course, q0.type AS type, q0.time AS time, standard_name.name AS standard, q0.pts AS pts, q0.comment AS comment FROM
(SELECT submission.submissionID, MAX(submission.date) AS date, submission.course, submission.type, submission.time, MIN(standard.pts) as pts, submission.comment FROM
(submission JOIN standard ON submission.course = standard.course AND submission.type = standard.type) 
WHERE submission.time < standard.time
GROUP BY submission.submissionID, submission.course, submission.type, submission.time, submission.comment) as q0
JOIN standard_name ON q0.pts = standard_name.pts
JOIN course ON q0.course = course.course
ORDER BY submissionID;