#!/usr/bin/python3
'''Print city & state info'''


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    try:
        db = MySQLdb.connect(host='localhost',
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3],
                             port=3306
                             )
    except Exception:
        exit()

    curse = db.cursor()

    curse.execute(
        "SELECT cities.id, cities.name, states.name\
        FROM cities JOIN states ON cities.state_id=states.id\
        ORDER BY id")

    for rec in curse.fetchall():
        print(rec)

    curse.close()
    db.close()
