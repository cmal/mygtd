#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of mygtd.
#
# File: model.py
# Description: .
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
# Created: 2012-10-05 00:24:18
# Last modified: 2012-10-07 01:48:40
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

from sqlalchemy import create_engine
# SQLite must use dialet to use DATETIME and TIME types, and I don't like it.
#engine = create_engine('sqlite+pysqlite:///gtd.db', echo=True) # &use_unicode=0
engine = create_engine('mysql+mysqldb://root:89362556@localhost:3306/mygtd?charset=utf8', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Unicode, ForeignKey,\
                        Boolean, Date, UnicodeText, Enum, Time
from sqlalchemy.orm import relationship, backref

##################################################################

class Catagory(Base):
    '''任务类别'''
    __tablename__ = 'catagory'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Unicode(10), nullable=False, unique=True)
    task = relationship("Task", uselist=True, backref="cat")
    def __init__(self, name):
        self.name = name

class Task(Base):
    '''任务名称'''
    __tablename__ = 'task'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Unicode(10), nullable=False)
    catagory_id = Column('catagory_id', Integer, ForeignKey('catagory.id'))
    record = relationship("Record", uselist=False, backref="task")
    def __init__(self, name):
        self.name = name

#class Comment(Base):
#    '''每次任务结束时中断的点，记下以备下次开始时同一任务时提示并继续'''
#    __tablename__ = 'comment'
#    id = Column('id', Integer, primary_key=True)
#    comment = Column('comment', UnicodeText)
#    record = relationship("Record", uselist=False, backref="record")
#    def __init__(self, comment):
#        self.comment = comment

class Record(Base):
    '''任务记录'''
    __tablename__ = 'record'
    id = Column('id', Integer, primary_key=True)
    task_id = Column('task_id', Integer, ForeignKey('task.id'))
    date = Column('date', Date)
    start_time = Column('start_time', Time)
    big_or_not = Column('big_or_not', Boolean)  # 1小时的任务还是两小时的任务
    state = Column('state', Enum('none', 'skipped', 'finished'), default='none')
    # 每次任务结束时中断的点，记下以备下次开始时同一任务时提示并继续
    tip = Column('tip', UnicodeText)
    # 顺便也记录一些有用的笔记、收获之类的
    comment = Column('comment', UnicodeText)
#    comment_id = Column('comment_id', Integer, ForeignKey('comment.id'))
    def __init__(self, date, start_time, big_or_not):
        self.date = date
        self.start_time = start_time
        self.big_or_not = big_or_not

Base.metadata.create_all(engine)
