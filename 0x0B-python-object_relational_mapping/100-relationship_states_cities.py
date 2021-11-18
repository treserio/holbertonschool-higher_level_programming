#!/usr/bin/python3
'''List first states using SQLalchemy'''


if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    Eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(argv[1], argv[2], argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(Eng)
    Sess = sessionmaker(bind=Eng)
    s = Sess()

    n_st = State(name='California')
    n_st.cities.append(City(name='San Francisco'))
    s.add(n_st)

    s.commit()
    s.close()
