CREAT DATABASE IF NOT EXISTS flask_intro;

\c flask_intro

CREATE TABLE IF NOT EXISTS reminders (
    title VARCHAR(255) NOT NULL,
    description TEXT
);

-- Run this file
--  psql < creat.sql postgres

-- in UBUNTU first:
-- sudo -i -u postgres

INSERT INTO reminders (title, description) VALUES ('Emily', 'Even more awesome'), ('Fausto', 'The Italian');
INSERT INTO reminders (title, description) VALUES('Mirjam is awesome', 'She is learning to code'),('Eat', 'Food is healthy'), ('Exercise', 'Get your heart moving');
