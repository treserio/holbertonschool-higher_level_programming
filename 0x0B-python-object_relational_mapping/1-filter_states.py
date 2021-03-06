#!/usr/bin/python3
'''Print all states beginning with N'''


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
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")

    for rec in curse.fetchall():
        print(rec)

    curse.close()
    db.close()
