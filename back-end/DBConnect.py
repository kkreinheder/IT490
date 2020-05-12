#!/usr/bin/python3

import pymysql

while True:
    db_rw = pymysql.connect("db_rw", "test", "test", "db-mysql")
    cursor1 = db_rw.cursor()

    db_r = pymysql.connect("db_r", "test", "test", "db-mysql")
    cursor2 = db_r.cursor()


write = "INSERT INTO user (first_name, last_name, email) VALUES (first_name, last_name, email)"
read1 = "SELECT * FROM user"

try:
    cursor1.execute(write)
    cursor1.execute(read)
    db_rw.commit()

except:
    db.rollback()

    
read2 = "SELECT * FROM user"

try:
    cursor2.execute(read)
    
db.close()
