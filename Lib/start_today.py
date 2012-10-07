#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of mygtd.
#
# File: start_today.py
# Description: .
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
# Created: 2012-10-05 10:31:52
# Last modified: 2012-10-07 21:38:22
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

import wx
import logging
logger = logging.getLogger('add_gtd')

import controller as ct
from ObjectListView import ObjectListView, ColumnDefn

import datetime
#import time

class Task(object):
    def __init__(self, cat, task, big_or_not):
        self.cat = cat
        self.task = task
        self.big_or_not = big_or_not
    def show(self):
        if self.big_or_not:
            hour = u'2小时'
        else:
            hour = u'1小时'
        return {"cat":self.cat, "task":self.task, "big":hour}

class StartTodayPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # init data
        self.tasks = []
        # GUI
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Add a Choice for Catagories, a ComboBox for Tasks,
        # a Choice for big_or_not, and a "Add" Button
        # EVT_COMBOBOX(id, func) 	Process a wxEVT_COMMAND_COMBOBOX_SELECTED command, which is generated by a wxComboBox control. 
        self.catBox = wx.ComboBox(self, -1, choices=ct.getCatagoryNameList()) 
        self.catBox.Bind(wx.EVT_COMBOBOX, self.onChangeCat)
        topSizer.Add(self.catBox)

        self.taskBox = wx.ComboBox(self, -1, choices=[])
        topSizer.Add(self.taskBox)

        self.bigChoice = wx.Choice(self, -1, choices=[u'1小时',u'2小时']) 
        topSizer.Add(self.bigChoice)

        addBtn = wx.Button(self, label=u'Add', style=wx.BU_EXACTFIT)
        topSizer.Add(addBtn, flag=wx.RIGHT)
        addBtn.Bind(wx.EVT_BUTTON, self.onAdd)

        self.recOlv = ObjectListView(self, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.recOlv.SetEmptyListMsg(u"今天还没有安排好呢！")
        self.setList()

        botSizer = wx.BoxSizer(wx.HORIZONTAL)
        clrBtn = wx.Button(self, label='Clear', style=wx.BU_EXACTFIT)
        clrBtn.Bind(wx.EVT_BUTTON, self.onClear)
        botSizer.Add(clrBtn, 1, wx.ALL, 10)
        saveBtn = wx.Button(self, label='Save&&Start', style=wx.BU_EXACTFIT)
        saveBtn.Bind(wx.EVT_BUTTON, self.onSave)
        botSizer.Add(saveBtn, 1, wx.ALL, 10)
        # TODO: 应该在listview中确认今日schedule，确认完毕后添加到数据库
        mainSizer.Add(topSizer, flag=wx.EXPAND)
        #mainSizer.Add(lvSizer, flag=wx.EXPAND)
        mainSizer.Add(self.recOlv, 1, wx.ALL|wx.EXPAND, 10)
        mainSizer.Add(botSizer, flag=wx.EXPAND)
        self.SetSizer(mainSizer)
        self.SetAutoLayout(True)
    def onAdd(self, event):
        c = self.catBox.GetValue()
        t = self.taskBox.GetValue()
        b = self.bigChoice.GetSelection()
        if c and t:
            if not b:
                b = 0
            task = Task(c,t,b)
            self.tasks.append(task.show())
            self.setList()
    def onSave(self, event):
        date = datetime.date.today()
        #start_time = time.strftime("%H:%M")
        now = datetime.datetime.now()
        for index in self.tasks:
            if index['big'] == u'1小时':
                now = now + datetime.timedelta(hours=1)
                big_or_not = False
            else:
                now = now + datetime.timedelta(hours=2)
                big_or_not = True
            ct.addRecord(**({'cat':index['cat'], 'task':index['task'],
                'date':date, 'start_time':now, 'big_or_not':big_or_not}))
        #TODO: should trigger a event to close frame (here is the panel)
#    def OnCloseWindow(self, event):
#        self.Destroy()
        
    def onChangeCat(self, event):
        pass
#    def onDel(self, event):
#        pass
    def onClear(self, event):
        # TODO: a comfirm dialog is needed
        self.tasks = []
        self.setList()
    def setList(self):
        self.recOlv.SetColumns([
            ColumnDefn('Catagory', 'left', 120, 'cat'),
            ColumnDefn('Task', 'left', 180, 'task'),
            ColumnDefn(u'1小时/2小时', 'left', 90, 'big'),
            ])
        self.recOlv.SetObjects(self.tasks)

class StartTodayFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, None, -1, u"制定新一天的计划", size=(480,360))
        panel = StartTodayPanel(self)
        self.Show()
