CREATE DATABASE ecommerce CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT all privileges ON *.* to 'ecommerce_user'@'%' identified by 'ecommerce_password';
flush privileges;