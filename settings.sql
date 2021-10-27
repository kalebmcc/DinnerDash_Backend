-- settings.sql
DROP DATABASE dinnerdash;

CREATE DATABASE dinnerdash;
CREATE USER dduser WITH PASSWORD 'dinnerdash';
GRANT ALL PRIVILEGES ON DATABASE dinnerdash TO dduser;