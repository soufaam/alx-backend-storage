-- Triggers
CREATE TRIGGER decreases
AFTER INSERT ON `orders`
FOR EACH ROW
UPDATE `items`
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
