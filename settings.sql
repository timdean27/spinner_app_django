CREATE DATABASE spinner_app_db;
CREATE USER spinner_buser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE spinner_app_db TO spinner_buser;
