-- Before TRIGGER
DELIMITER //
CREATE TRIGGER resets
BEFORE UPDATE ON `users`
FOR EACH ROW
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0 ;
	END IF; // DELIMITER;
