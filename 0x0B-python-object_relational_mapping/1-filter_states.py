#!/usr/bin/python3
'''print states that begin with "N" in order by id'''


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
    curse.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    print("\n".join(str(rec) for rec in curse.fetchall()))

    curse.close()
    db.close()
