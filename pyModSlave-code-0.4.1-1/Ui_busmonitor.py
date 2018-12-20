# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\python\pyModSlave\ui\busmonitor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BusMonitor(object):
    def setupUi(self, BusMonitor):
        BusMonitor.setObjectName(_fromUtf8("BusMonitor"))
        BusMonitor.setWindowModality(QtCore.Qt.NonModal)
        BusMonitor.resize(450, 500)
        BusMonitor.setMinimumSize(QtCore.QSize(450, 500))
        BusMonitor.setMaximumSize(QtCore.QSize(450, 580))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/view-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BusMonitor.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(BusMonitor)
        self.centralwidget.setMinimumSize(QtCore.QSize(450, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblRawData = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblRawData.setFont(font)
        self.lblRawData.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblRawData.setObjectName(_fromUtf8("lblRawData"))
        self.verticalLayout.addWidget(self.lblRawData)
        self.lstRawData = QtGui.QListView(self.centralwidget)
        self.lstRawData.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lstRawData.setFont(font)
        self.lstRawData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lstRawData.setAlternatingRowColors(True)
        self.lstRawData.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lstRawData.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.lstRawData.setSelectionRectVisible(False)
        self.lstRawData.setObjectName(_fromUtf8("lstRawData"))
        self.verticalLayout.addWidget(self.lstRawData)
        self.lblPDU = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPDU.setFont(font)
        self.lblPDU.setObjectName(_fromUtf8("lblPDU"))
        self.verticalLayout.addWidget(self.lblPDU)
        self.txtPDU = QtGui.QPlainTextEdit(self.centralwidget)
        self.txtPDU.setReadOnly(True)
        self.txtPDU.setObjectName(_fromUtf8("txtPDU"))
        self.verticalLayout.addWidget(self.txtPDU)
        BusMonitor.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(BusMonitor)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        BusMonitor.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClear = QtGui.QAction(BusMonitor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/edit-clear-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon1)
        self.actionClear.setIconVisibleInMenu(True)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionExit = QtGui.QAction(BusMonitor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/Close-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave = QtGui.QAction(BusMonitor)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/save-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))

        self.retranslateUi(BusMonitor)
        QtCore.QMetaObject.connectSlotsByName(BusMonitor)

    def retranslateUi(self, BusMonitor):
        BusMonitor.setWindowTitle(_translate("BusMonitor", "Bus Monitor", None))
        self.lblRawData.setText(_translate("BusMonitor", "Raw Data", None))
        self.lblPDU.setText(_translate("BusMonitor", "PDU", None))
        self.toolBar.setWindowTitle(_translate("BusMonitor", "toolBar", None))
        self.actionClear.setText(_translate("BusMonitor", "Clear", None))
        self.actionClear.setToolTip(_translate("BusMonitor", "Clear", None))
        self.actionExit.setText(_translate("BusMonitor", "Exit", None))
        self.actionExit.setToolTip(_translate("BusMonitor", "Exit", None))
        self.actionSave.setText(_translate("BusMonitor", "Save", None))
        self.actionSave.setToolTip(_translate("BusMonitor", "Save", None))

import pyModSlaveQt_rc
