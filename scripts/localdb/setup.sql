CREATE DATABASE simpletracker;

\connect simpletracker;

CREATE USER app WITH ENCRYPTED PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE simpletracker TO app;
