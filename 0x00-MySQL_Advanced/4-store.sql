-- Triggers
CREATE TRIGGER decreases
AFTER INSERT ON `orders`
FOR EACH ROW
BEGIN
    UPDATE `items`
	SET quantity = quantity - NEW.number;
END;
