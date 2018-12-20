# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\python\pyModSlave\ui\about.ui'
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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(400, 80)
        About.setMinimumSize(QtCore.QSize(400, 80))
        About.setMaximumSize(QtCore.QSize(400, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/info16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        About.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(About)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblVersion = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblVersion.setFont(font)
        self.lblVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVersion.setObjectName(_fromUtf8("lblVersion"))
        self.verticalLayout.addWidget(self.lblVersion)
        self.lblLibVer = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblLibVer.setFont(font)
        self.lblLibVer.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLibVer.setObjectName(_fromUtf8("lblLibVer"))
        self.verticalLayout.addWidget(self.lblLibVer)
        self.lblURL = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblURL.setFont(font)
        self.lblURL.setAlignment(QtCore.Qt.AlignCenter)
        self.lblURL.setOpenExternalLinks(True)
        self.lblURL.setObjectName(_fromUtf8("lblURL"))
        self.verticalLayout.addWidget(self.lblURL)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "About", None))
        self.lblVersion.setText(_translate("About", "pyModSlave", None))
        self.lblLibVer.setText(_translate("About", "modbus_tk lib", None))
        self.lblURL.setText(_translate("About", "http://", None))

import pyModSlaveQt_rc
