#!/usr/bin/python3
"""script that takes in the name of a state as
an argument and lists all cities of that state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                    RIGHT JOIN states ON states.id = cities.state_id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ACS", (argv[4], ))
    r = cursor.fetchall()
    new_list = []
    for row in r:
        new_list.append(row[0])
    print(", ".join(new_list))
