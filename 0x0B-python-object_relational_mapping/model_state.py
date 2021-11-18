#!/usr/bin/python3
'''module for state class/table'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class State(declarative_base()):
    '''class for states table'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
