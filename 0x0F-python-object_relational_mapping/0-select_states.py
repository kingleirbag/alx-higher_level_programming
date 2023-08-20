#!/usr/bin/python3
"""lists all states from the database """
import MySQLdb
import sys


if __name__ == "__main__":
    dbconnect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = dbconnect.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    dbconnect.close()
