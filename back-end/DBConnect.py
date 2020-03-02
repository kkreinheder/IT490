#!/usr/bin/python3

import pymysql

db = pymysql.connect("0.0.0.0", "test", "test", "db-mysql")

cursor = db.cursor()

sql = "INSERT INTO user(first_name, last_name, email)
        VALUES (John, Smith, jsmith@gmail.com)"
        
sql = "SELECT * FROM user"

db.close()
