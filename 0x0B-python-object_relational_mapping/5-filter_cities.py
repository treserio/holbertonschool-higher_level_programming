#!/usr/bin/python3
'''Print all states where name matches given str'''


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    try:
        db = MySQLdb.connect(host='localhost',
                             user=argv[1],
                             passwd='',
                             db=argv[3],
                             port=3306
                             )
    except Exception:
        exit()

    curse = db.cursor()
    curse.execute(
        "SELECT cities.name\
        FROM states JOIN cities ON states.id=cities.state_id\
        WHERE states.name = '{}'\
        ORDER BY cities.id".format(argv[4].split(" ")[0]))

    fetch = curse.fetchall()
    if fetch:
        print(', '.join(rec[0] for rec in fetch))

    curse.close()
    db.close()
