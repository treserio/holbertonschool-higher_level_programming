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
    new_st = State(name='Louisiana')

    Sess().add(new_st)
    Sess().commit()

    print("{}".format(new_st.id))

    Sess().close
