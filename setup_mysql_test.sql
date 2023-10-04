-- Create hbnb_dev_db database and hbnb_dev user
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- add the user hbnb_dev with password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_test_pwd';
-- add privileges to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';