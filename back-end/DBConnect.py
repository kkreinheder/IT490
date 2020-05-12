#!/usr/bin/python3

import pymysql

db_rw = pymysql.connect("db_rw", "test", "test", "db-mysql")
cursor = db_rw.cursor()

db_r = pymysql.connect("db_r", "test", "test", "db-mysql")
cursor = db_r.cursor()

while True:
    write = "INSERT INTO user (first_name, last_name, email) VALUES (John, Smith, jsmith@gmail.com)"

    read = "SELECT * FROM user"

    try:
        cursor.execute(write)
        cursor.execute(read)
        db.commit()

    except:
        db.rollback()

    db.close()
