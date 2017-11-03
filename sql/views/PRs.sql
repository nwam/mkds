SELECT submission_plus.* FROM submission_plus INNER JOIN
(SELECT MAX(submissionID) as recID FROM submission_plus GROUP BY course, type) as recID
ON recID.recID = submission_plus.submissionID
ORDER BY courseID, type;