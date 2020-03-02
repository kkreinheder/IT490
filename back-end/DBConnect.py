#!/usr/bin/python3

import pymysql

db = pymysql.connect("0.0.0.0", "test", "test", "db-mysql")

cursor = db.cursor()

write = "INSERT INTO user (first_name, last_name, email) VALUES (John, Smith, jsmith@gmail.com)"
        
read = "SELECT * FROM user"

try:
    cursor.execute(write)
    cursor.execute(read)
    db.commit()
    
except:
    db.rollback()

db.close()