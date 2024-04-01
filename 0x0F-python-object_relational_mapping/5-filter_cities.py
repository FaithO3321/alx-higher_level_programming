#!/usr/bin/python3
"""All states from the database hbtn_0e_0-usa"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    state_name = sys.argv[4]
    cur.execute("""SELECT cities.name
                   FROM cities
                   INNER JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s""", (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
