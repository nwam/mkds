CREATE TABLE `submission` (
  `submissionID` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `course` text,
  `type` text,
  `time` text,
  `comment` text,
  PRIMARY KEY (`submissionID`)
) 
