CREATE DATABASE ecommerce CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'ecommerce_user'@'%' IDENTIFIED BY 'ecommerce_password';
GRANT ALL PRIVILEGES ON *.* TO 'ecommerce_user'@'%';
flush privileges;