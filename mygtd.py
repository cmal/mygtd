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
# Last modified: 2012-10-05 00:23:30
#
# Copyright (C) 2012-2013 Yu Zhao.
#
#==============================================================================

import wx
import logging
from Lib.window import MyGtdWindow
from os import path
import sys

# set up loggers
for name in ['app', 'window',]:
    logger = logging.getLogger(name)
    apppath = path.abspath(path.dirname(sys.argv[0]))
    filehandler = logging.FileHandler(path.join(apppath,'mygtd.log'))
    formatter = logging.Formatter('%(asctime)s<==>%(name)s<==>%(message)s')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.FATAL)

log = logging.getLogger('app')

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
    log.debug("Finished MainLoop()...existing.")
