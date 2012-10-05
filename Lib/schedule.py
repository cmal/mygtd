#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of mygtd.
#
# File: schedule.py
# Description: .
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
# Created: 2012-10-05 10:31:52
# Last modified: 2012-10-05 10:45:17
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

import wx
import logging
logger = logging.getLogger('add_gtd')

# TODO: no! use a dialog
class AddGtdPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        addBtn = wx.Button(self, label=u'Add')
        addBtn.Bind(,onAdd)
        # TODO: add a choice field for big_or_not
        # TODO: add a ListView for showing today's schedule
        # TODO: 应该在listview中确认今日schedule，确认完毕后添加到数据库
    def onAdd(self, event):
        pass
