-- Creats the database 'htbn_0d_2' and the user 'user_0d_2'

-- User created if it doesn't exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Database created if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- SELECT privileges granted on hbtn_0d_2 to 'user_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
