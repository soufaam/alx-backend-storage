-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers 
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users AS u
JOIN (
    SELECT user_id, 
           SUM(c.score * p.weight) / SUM(p.weight) AS weighted_score
    FROM corrections AS c
    LEFT JOIN projects AS p ON c.project_id = p.id
    GROUP BY user_id
) AS weighted_scores ON u.id = weighted_scores.user_id
SET u.average_score = weighted_scores.weighted_score;
END://
DELIMITER ;