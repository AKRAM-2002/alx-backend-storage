-- A script that creates a stored procedure
-- ComputerAverageScoreForUser that computes
-- and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN

	DECLARE user_total INT DEFAULT 0;
	DECLARE total_projects INT DEFAULT 0;
        
	SELECT COUNT(*) INTO total_projects 
	FROM corrections
	WHERE corrections.user_id = user_id;

	SELECT SUM(score) INTO user_total 
	FROM corrections
	WHERE corrections.user_id = user_id;

	IF total_projects != 0 THEN
		UPDATE users
		SET users.average_score = (user_total / total_projects) 
		WHERE users.id = user_id;

	END IF;

END $$

DELIMITER ;
