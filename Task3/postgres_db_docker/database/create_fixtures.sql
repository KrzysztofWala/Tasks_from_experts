CREATE TABLE IF NOT EXISTS users (
    id_user INT NOT NULL,
    first_name VARCHAR(64),
    last_name VARCHAR(64)
);

BEGIN;
INSERT INTO users VALUES ('1', 'Adam', 'Malysz');
INSERT INTO users VALUES ('2', 'Mariusz', 'Pudzianowski');
INSERT INTO users VALUES ('3', 'Lech', 'Roch-Pawlak');
COMMIT;