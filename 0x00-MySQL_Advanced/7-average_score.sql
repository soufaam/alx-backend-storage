-- SQL script that creates a stored procedure ComputeAverageScoreForUser

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT )
BEGIN
	DECLARE Avgscore FLOAT;
    SELECT AVG(score) INTO avgscore FROM corrections 
	WHERE user_id = corrections.user_id;
	UPDATE users
	SET users.average_score = Avgscore
	WHERE users.id = user_id;
END;//
DELIMITER ;