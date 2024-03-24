-- ComputeAverageWeightedScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE avgscore FLOAT;
	SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) INTO avgscore
	FROM corrections LEFT JOIN projects ON projects.id = corrections.project_id
	WHERE corrections.user_id = user_id;
	UPDATE users
	SET average_score = avgscore
	WHERE users.id = user_id;
END;//
DELIMITER ;