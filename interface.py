# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Documenti\Progetti\Fap-Folder-Creator\interface.ui'
#
# Created: Sat Sep 13 16:43:09 2014
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(449, 109)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 11, 21, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 44, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(420, 41, 25, 19))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 80, 75, 20))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.urlEdit = QtGui.QLineEdit(self.centralwidget)
        self.urlEdit.setGeometry(QtCore.QRect(60, 10, 351, 20))
        self.urlEdit.setObjectName(_fromUtf8("urlEdit"))
        self.dirEdit = QtGui.QLineEdit(self.centralwidget)
        self.dirEdit.setGeometry(QtCore.QRect(60, 40, 351, 20))
        self.dirEdit.setObjectName(_fromUtf8("dirEdit"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(104, 80, 251, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(23, 80, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Fap Folder Creator", None))
        self.label.setText(_translate("MainWindow", "Url:", None))
        self.label_2.setText(_translate("MainWindow", "Directory", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.pushButton.setText(_translate("MainWindow", "Download", None))
        self.checkBox.setText(_translate("MainWindow", "Watch", None))

