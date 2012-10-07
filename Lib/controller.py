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
# Last modified: 2012-10-07 21:24:56
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

from model import Catagory, Task, Record, engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy import or_
from datetime import date

def connectdb():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def addRecord(**args):
    session = connectdb()
    cat = session.query(Catagory).filter_by(name=args['cat'])
    if cat.all():
        catobj = cat.one()
    else:
        catobj = Catagory(args['cat'])
    taskobj = Task(args['task'])
    taskobj.cat = catobj
#    if True:
#        session.add(task)
#    date = args['date'].today()
    record = Record(args['date'], args['start_time'], args['big_or_not'])
    record.task = taskobj
    session.merge(record) # cat and task will save/update automatically and cascade due to the session's default setting?
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
    session.add(record)
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
