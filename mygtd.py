#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#==============================================================================
#
# This file is a part of mygtd
#
# File: mygtd.py
# Description: Main app.
# Author: Yu Zhao 赵宇 <zyzy5730@163.com>
# Created: 2012-10-04 12:21:26
# Last modified: 2012-10-04 12:46:06
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

import wx
from Lib.window import MyGtdWindow

class MyGtdApp(wx.App):
    '''App class for MyGtd.'''
    def OnInit(self):
        self.frame = MyGtdWindow(None, -1, 'MyGtd',
                wx.DEFAULT_FRAME_STYLE|wx.NO_FULL_REPAINT_ON_RESIZE)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    # if called as a script, and not as a module
    app = MyGtdApp()
    app.MainLoop()
