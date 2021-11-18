#!/usr/bin/python3
'''List first states using SQLalchemy'''


if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    Eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(argv[1], argv[2], argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(Eng)
    Sess = sessionmaker(bind=Eng)

    for rec in Sess().query(State, City).join(
            City, State.id == City.state_id).order_by(City.id):
        print("{}: ({}) {}".format(rec[0].name, rec[1].id, rec[1].name))

    Sess().close()
