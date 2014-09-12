# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Documenti\Progetti\Fap-Folder-Creator\interface.ui'
#
# Created: Fri Sep 12 23:07:18 2014
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
        self.label.setGeometry(QtCore.QRect(20, 10, 21, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(420, 40, 25, 19))
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
        self.progressBar.setGeometry(QtCore.QRect(80, 80, 251, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.minImageLabel = QtGui.QLabel(self.centralwidget)
        self.minImageLabel.setGeometry(QtCore.QRect(30, 80, 16, 16))
        self.minImageLabel.setObjectName(_fromUtf8("minImageLabel"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 16, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.maxImageLabel = QtGui.QLabel(self.centralwidget)
        self.maxImageLabel.setGeometry(QtCore.QRect(50, 80, 16, 16))
        self.maxImageLabel.setObjectName(_fromUtf8("maxImageLabel"))
        self.watch_label = QtGui.QLabel(self.centralwidget)
        self.watch_label.setEnabled(False)
        self.watch_label.setGeometry(QtCore.QRect(180, 60, 101, 16))
        self.watch_label.setIndent(0)
        self.watch_label.setObjectName(_fromUtf8("watch_label"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Url:", None))
        self.label_2.setText(_translate("MainWindow", "Directory", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.pushButton.setText(_translate("MainWindow", "Download", None))
        self.minImageLabel.setText(_translate("MainWindow", "0", None))
        self.label_4.setText(_translate("MainWindow", "/", None))
        self.maxImageLabel.setText(_translate("MainWindow", "0", None))
        self.watch_label.setText(_translate("MainWindow", "Watching thread...", None))

