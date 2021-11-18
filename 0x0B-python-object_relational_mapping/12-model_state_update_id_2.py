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
    s.query(State).where(State.id == 2)[0].name = 'New Mexico'
    s.commit()
    s.close()
