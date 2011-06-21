#! /bin/sh
mysql -uroot -p'sharp7&7' -e "CREATE USER 'jayd3e'@'localhost' IDENTIFIED BY 'sharp7&7'; CREATE DATABASE jayd3e_db; GRANT ALL ON jayd3e_db.* TO 'jayd3e'@'localhost';"
