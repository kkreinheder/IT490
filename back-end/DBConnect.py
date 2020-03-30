#!/usr/bin/python3

import pymysql

db = pymysql.connect("172.18.0.3", "test", "test", "db-mysql")

cursor = db.cursor()

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
