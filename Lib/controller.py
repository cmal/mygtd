#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of mygtd.
#
# File: controller.py
# Description: .
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
# Created: 2012-10-05 01:17:08
# Last modified: 2012-10-05 23:55:48
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

from model import Catagory, Task, Comment, Record
from sqlalchemy.orm import sessionmaker
#from sqlalchemy import or_
from datetime import date

def connectdb():
    Session = sessionmaker(bind=egngine)
    session = Session()
    return session

def addRecord(**argv):
    cat = Catagory(cat)
    task = Task(task)
    date = date.today()
    record = Record(date, start_time, big_or_not)
    session = connectdb()
    my_db_commit(session)
    session.close()

def confirmRecord(index, **argv):
    session = connectdb()
    record = session.query(Record).filter_by(id=index).one()
    record.state = state  # outside should have an exception handler
    if locals().has_key('tip'):
        record.tip = tip
    if locals().has_key('comment'):
        record.comment = comment
    my_db_commit(session)
    session.close()

def getCatagoryNameList():
    session = connectdb()
    result = session.query(Catagory).all()
    cat_list = []
    for index in result:
        cat_list.append(index.name)
    session.close()
    return cat_list

def my_db_commit(session):
    try:
        session.commit()
    except:
        session.rollback()
        raise
