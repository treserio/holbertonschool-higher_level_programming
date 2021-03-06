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
    Base.metadata.create_all(Eng)
    Sess = sessionmaker(bind=Eng)

    try:
        print('{}: {}'.format(Sess().query(State).first().id,
                              Sess().query(State).first().name))
    except Exception:
        print('Nothing')

    Sess().close
