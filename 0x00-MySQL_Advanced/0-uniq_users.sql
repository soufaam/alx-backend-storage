-- script that creates a table users
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY,
	`name` VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL
);
