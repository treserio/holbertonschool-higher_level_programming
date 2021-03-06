#!/usr/bin/python3
'''Print all states where name matches given str + protection'''


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
        "SELECT * FROM states\
        WHERE name LIKE BINARY '{}'\
        ORDER BY id".format(argv[4].split(" ")[0]))

    for rec in curse.fetchall():
        print(rec)

    curse.close()
    db.close()
