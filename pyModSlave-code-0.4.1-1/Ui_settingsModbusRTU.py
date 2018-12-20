# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\python\pyModSlave\ui\settingsmodbusrtu.ui'
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

class Ui_SettingsModbusRTU(object):
    def setupUi(self, SettingsModbusRTU):
        SettingsModbusRTU.setObjectName(_fromUtf8("SettingsModbusRTU"))
        SettingsModbusRTU.resize(220, 240)
        SettingsModbusRTU.setMinimumSize(QtCore.QSize(220, 240))
        SettingsModbusRTU.setMaximumSize(QtCore.QSize(220, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/options-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsModbusRTU.setWindowIcon(icon)
        SettingsModbusRTU.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(SettingsModbusRTU)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cmbStopBits = QtGui.QComboBox(SettingsModbusRTU)
        self.cmbStopBits.setObjectName(_fromUtf8("cmbStopBits"))
        self.cmbStopBits.addItem(_fromUtf8(""))
        self.cmbStopBits.addItem(_fromUtf8(""))
        self.cmbStopBits.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbStopBits, 4, 1, 1, 1)
        self.cmbPort = QtGui.QSpinBox(SettingsModbusRTU)
        self.cmbPort.setMinimum(1)
        self.cmbPort.setMaximum(128)
        self.cmbPort.setObjectName(_fromUtf8("cmbPort"))
        self.gridLayout.addWidget(self.cmbPort, 1, 1, 1, 1)
        self.lblPort = QtGui.QLabel(SettingsModbusRTU)
        self.lblPort.setMinimumSize(QtCore.QSize(0, 0))
        self.lblPort.setObjectName(_fromUtf8("lblPort"))
        self.gridLayout.addWidget(self.lblPort, 1, 0, 1, 1)
        self.lblStopBits = QtGui.QLabel(SettingsModbusRTU)
        self.lblStopBits.setObjectName(_fromUtf8("lblStopBits"))
        self.gridLayout.addWidget(self.lblStopBits, 4, 0, 1, 1)
        self.cmbDataBits = QtGui.QComboBox(SettingsModbusRTU)
        self.cmbDataBits.setObjectName(_fromUtf8("cmbDataBits"))
        self.cmbDataBits.addItem(_fromUtf8(""))
        self.cmbDataBits.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbDataBits, 3, 1, 1, 1)
        self.lblDataBits = QtGui.QLabel(SettingsModbusRTU)
        self.lblDataBits.setObjectName(_fromUtf8("lblDataBits"))
        self.gridLayout.addWidget(self.lblDataBits, 3, 0, 1, 1)
        self.cmbBaud = QtGui.QComboBox(SettingsModbusRTU)
        self.cmbBaud.setObjectName(_fromUtf8("cmbBaud"))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.cmbBaud.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbBaud, 2, 1, 1, 1)
        self.lblBaud = QtGui.QLabel(SettingsModbusRTU)
        self.lblBaud.setObjectName(_fromUtf8("lblBaud"))
        self.gridLayout.addWidget(self.lblBaud, 2, 0, 1, 1)
        self.cmbParity = QtGui.QComboBox(SettingsModbusRTU)
        self.cmbParity.setObjectName(_fromUtf8("cmbParity"))
        self.cmbParity.addItem(_fromUtf8(""))
        self.cmbParity.addItem(_fromUtf8(""))
        self.cmbParity.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbParity, 5, 1, 1, 1)
        self.lblParity = QtGui.QLabel(SettingsModbusRTU)
        self.lblParity.setObjectName(_fromUtf8("lblParity"))
        self.gridLayout.addWidget(self.lblParity, 5, 0, 1, 1)
        self.lblDev = QtGui.QLabel(SettingsModbusRTU)
        self.lblDev.setObjectName(_fromUtf8("lblDev"))
        self.gridLayout.addWidget(self.lblDev, 0, 0, 1, 1)
        self.cmbDev = QtGui.QComboBox(SettingsModbusRTU)
        self.cmbDev.setEditable(True)
        self.cmbDev.setObjectName(_fromUtf8("cmbDev"))
        self.cmbDev.addItem(_fromUtf8(""))
        self.cmbDev.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbDev, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsModbusRTU)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.lblStopBits.setBuddy(self.cmbStopBits)
        self.lblDataBits.setBuddy(self.cmbDataBits)
        self.lblBaud.setBuddy(self.cmbBaud)
        self.lblParity.setBuddy(self.cmbParity)

        self.retranslateUi(SettingsModbusRTU)
        self.cmbStopBits.setCurrentIndex(0)
        self.cmbDataBits.setCurrentIndex(1)
        self.cmbBaud.setCurrentIndex(4)
        self.cmbParity.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsModbusRTU.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsModbusRTU.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsModbusRTU)

    def retranslateUi(self, SettingsModbusRTU):
        SettingsModbusRTU.setWindowTitle(_translate("SettingsModbusRTU", "Modbus RTU Settings", None))
        self.cmbStopBits.setItemText(0, _translate("SettingsModbusRTU", "1", None))
        self.cmbStopBits.setItemText(1, _translate("SettingsModbusRTU", "1.5", None))
        self.cmbStopBits.setItemText(2, _translate("SettingsModbusRTU", "2", None))
        self.lblPort.setText(_translate("SettingsModbusRTU", "Serial port", None))
        self.lblStopBits.setText(_translate("SettingsModbusRTU", "Stop Bits", None))
        self.cmbDataBits.setItemText(0, _translate("SettingsModbusRTU", "7", None))
        self.cmbDataBits.setItemText(1, _translate("SettingsModbusRTU", "8", None))
        self.lblDataBits.setText(_translate("SettingsModbusRTU", "Data Bits", None))
        self.cmbBaud.setItemText(0, _translate("SettingsModbusRTU", "1200", None))
        self.cmbBaud.setItemText(1, _translate("SettingsModbusRTU", "2400", None))
        self.cmbBaud.setItemText(2, _translate("SettingsModbusRTU", "4800", None))
        self.cmbBaud.setItemText(3, _translate("SettingsModbusRTU", "9600", None))
        self.cmbBaud.setItemText(4, _translate("SettingsModbusRTU", "19200", None))
        self.cmbBaud.setItemText(5, _translate("SettingsModbusRTU", "38400", None))
        self.cmbBaud.setItemText(6, _translate("SettingsModbusRTU", "57600", None))
        self.cmbBaud.setItemText(7, _translate("SettingsModbusRTU", "115200", None))
        self.lblBaud.setText(_translate("SettingsModbusRTU", "Baud", None))
        self.cmbParity.setItemText(0, _translate("SettingsModbusRTU", "None", None))
        self.cmbParity.setItemText(1, _translate("SettingsModbusRTU", "Odd", None))
        self.cmbParity.setItemText(2, _translate("SettingsModbusRTU", "Even", None))
        self.lblParity.setText(_translate("SettingsModbusRTU", "Parity", None))
        self.lblDev.setText(_translate("SettingsModbusRTU", "Serial device", None))
        self.cmbDev.setItemText(0, _translate("SettingsModbusRTU", "/dev/ttyS", None))
        self.cmbDev.setItemText(1, _translate("SettingsModbusRTU", "/dev/ttyUSB", None))

import pyModSlaveQt_rc
