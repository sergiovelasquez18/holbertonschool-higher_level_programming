#!/usr/bin/python3
"""script that takes in the name of a state as
an argument and lists all cities of that state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    current = connect.cursor()
    query = "SELECT cities.name FROM cities"
    query = query + " INNER JOIN states ON cities.state_id = states.id"
    query = query + " WHERE states.name = %s ORDER BY cities.id ACS"
    current.execute(query,[sys.argv[4]])

    query_r = current.fetchall()
    print(', '.join(row[0] for row in query_r))
    current.close()
    connect.close()
