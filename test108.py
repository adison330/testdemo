#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignal,pyqtSlot

class MymainWindow(QMainWindow):
    SIG_UPDATE_ITEM_PIC = pyqtSignal(tuple)

    def __int__(self):
        super(MyMainWindow,self).__int__()

        # 从ui文件加载Qt Designer 设计好的界面
        uic.loadUi('MainWindow.ui',self)

        # 事件关联操作
        self.btnLoadNextBatch.clicked.connect(self.cmd_load_next_batch)
        self.btnClearList.clicked.connect(self.cmd_clear_list)
        self.lwPicsList.itemDoubleClicked.connect(self.cmd_lw_double_click)
        #自定义信号关联事件
        self.SIG_UPDATE_ITEM_PIC.connect(self.update_item_pic)

    # 界面相关，更新列表中的图片
    @pyqtSlot(tuple)
    def update_item_pic(self,args):
        pass
