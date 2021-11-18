#!/usr/bin/python3
'''List first states using SQLalchemy'''


if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    Eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(argv[1], argv[2], argv[3]),
                        pool_pre_ping=True)

    Sess = sessionmaker(bind=Eng)
    s = Sess()
    recs = s.query(State).filter(State.name.like('%a%'))
    for rec in recs:
        s.delete(rec)
    s.commit()
    s.close()
