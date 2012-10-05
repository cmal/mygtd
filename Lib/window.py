#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of mygtd
#
# File: window.py
# Description: mygtd Window.
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
# Created: 2012-10-04 12:46:20
# Last modified: 2012-10-05 22:03:54
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

import logging
log = logging.getLogger('window')

import wx
import images

class MyGtdWindow(wx.Frame):
    '''Main class of interest in MyGtd. Frame for the MyGtd app.
    All GUI logic here.
    '''

    def __init__(self, parent, id, title, style):
        '''Construct GUI, and bind GUI events to their handlers.'''
        wx.Frame.__init__(self, parent, wx.ID_ANY, "myGtd")

        self.createMenuBar()
        self.createToolBar()
        self.createStatusBar()
        self.createMainWindow()

    def menuData(self):
        return ((u"程序",
                    (u"退出", u"退出程序", self.OnCloseWindow)),
                (u"帮助",
                    (u"用户手册", u"用户手册", self.OnManual),
                    ("", "", ""),
                    (u"版权", u"本软件的版权信息", self.OnCopyRight),
                    (u"关于作者", u"本软件作者的相关信息", self.OnAuthor),
                    (u"关于本软件", u"本软件的相关信息", self.OnAbout)),
                )

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for each in self.menuData():
            menuLabel = each[0]
            menuItems = each[1:]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
            self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        """创建一个菜单 --从创建菜单栏函数中抽象出来的函数

        """
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            menuItem = menu.Append(-1, eachLabel, eachStatus)
            self.Bind(wx.EVT_MENU, eachHandler, menuItem)
        return menu

    def toolBarData(self):
        return ((u"开始新的一天", images.spinning_nb1.GetBitmap(), u"今天计划", self.OnStartToday),
                (u"点击查看今天\n计划完成情况", images.spinning_nb1.GetBitmap(), u"今天进度", self.OnSelectDay),
                (u"Week", images.spinning_nb2.GetBitmap(), u"", self.OnSelectWeek),
                )

    def createToolBar(self):
        tBar = self.CreateToolBar()
        for each in self.toolBarData():
            self.createSimpleTool(tBar, *each)
        tBar.Realize()
    
    def createSimpleTool(self, tbar, label, filename, help, handler):
        if not label:
            tbar.AddSeparator()
            return
        tool = tbar.AddSimpleTool(-1, filename, label, help)
        self.Bind(wx.EVT_MENU, handler, tool)

    def OnManual(self, event): pass
    def OnCopyRight(self, event): pass
    def OnAuthor(self, event): pass
    def OnAbout(self, event): pass

    def createStatusBar(self):
        self.statusBar = self.CreateStatusBar()
        self.statusBar.SetFieldsCount(3)
        self.statusBar.SetStatusWidths([-1,-2,-3])

    def createMainWindow(self):
        self.mainPanel = wx.Panel(self, wx.ID_ANY)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.mainPanel.SetSizer(self.mainSizer)

        self.splitter = wx.SplitterWindow(self.mainPanel,\
                style=wx.SP_LIVE_UPDATE | wx.SP_3DSASH)
        self.splitter.SetMinimumPaneSize(200)
        self.mainSizer.Add(self.splitter, 2, wx.EXPAND)

        self.lPanel = wx.Panel(self.splitter, wx.NewId())
        self.tree = wx.TreeCtrl(self.lPanel, style=wx.TR_DEFAULT_STYLE)
        self.lBox = wx.BoxSizer(wx.VERTICAL)
        self.lBox.Add(self.tree, wx.NewId(), wx.EXPAND)
        self.lPanel.SetSizer(self.lBox)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)

        self.rPanel = wx.Panel(self.splitter, wx.NewId())
        self.content = wx.TextCtrl(self.rPanel, wx.NewId())
        self.rBox = wx.BoxSizer(wx.VERTICAL)
        self.rBox.Add(self.content, wx.NewId(), wx.EXPAND)
        self.rPanel.SetSizer(self.rBox)

        self.splitter.SplitVertically(self.lPanel, self.rPanel, 25)

    def OnStartToday(self, event):
        import start_today
        start_today = start_today.StartTodayFrame(self)
        start_today.Show()
        #try:
        #    res = dlg.ShowModal()
        #    if res == wx.ID_OK:
        #        dlg.onAdd()
        #except:
        #    wx.MessageBox(u"添加失败")
        #    logger.debug(u"开始新的一天--保存失败")
        #    #self.onAdd(event)
        #    dlg.ShowModal()
        #dlg.Destroy()
    def OnSelectDay(self, event): pass
    def OnSelectWeek(self, event): pass
    def OnSelChanged(self, event): pass
    def OnCloseWindow(self, event):
        self.Destroy()
