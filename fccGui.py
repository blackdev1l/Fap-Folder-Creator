__author__ = 'Cristian'

import sys
from PyQt4.QtGui import QMainWindow, QApplication, QFileDialog, QDialog, QLabel
from PyQt4.QtCore import SIGNAL,QObject, QStringList, QString, QThread
from interface import Ui_MainWindow
import ffc
import contextlib
import json
import urllib2
"""
This Script works with PyQt4 only
"""
class Worker(QThread):
    def getVar(self,dir,url,watch):
        self.dir = dir
        self.url = url
        self.watch = watch
    def run(self):
        urljson = ffc.url_to_json(self.url)

        try:
            with contextlib.closing(urllib2.urlopen(urljson)) as j:
                j_obj = json.load(j)
        except urllib2.HTTPError:
            print("Thread is 404")
            exit(3)

        img_list = ffc.get_images(self.url)
        gui.getMax(len(img_list))
        cont = 0
        print("foundmages : ",len(img_list))
        for item in img_list:
            cont += 1
            print(cont,len(img_list))
            self.emit(SIGNAL("update(int)"),cont)
            filename = item.split('/')[-1]
            ffc.download(item,filename,self.dir)
        if(self.watch):
            ffc.watch_thread(10,self.url,self.dir)



class Gui:

    def __init__(self):
        self.curr = 0
        self.app = QApplication(sys.argv)
        self.fileManager = QFileDialog()
        self.fileManager.setFileMode(self.fileManager.DirectoryOnly)
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.thread = Worker()
        self.connect()

    def onDownloadButton(self):
        url = str(self.ui.urlEdit.text())
        dir =  str(self.ui.dirEdit.text())
        if(self.ui.checkBox.isChecked()):
            watch = True
        else:
            watch = False
        self.thread.getVar(dir,url,watch)
        self.thread.start()


    def onSelectFolder(self):

        Fdialog = QFileDialog()
        Fdialog.setFileMode(QFileDialog.DirectoryOnly)
        if Fdialog.exec_():
            folderPath = QStringList(Fdialog.selectedFiles())
            self.ui.dirEdit.setText(folderPath.takeFirst())

    def onError(self, type):
        dialog = QDialog(self.window)
        text  = QLabel(dialog)
        if(type is "url"):
            text.setText("URL is invalid")
        else:
            text.setText("DIR is invalid")
        dialog.exec_()

    def getMax(self,max):
        self.ui.progressBar.setRange(0,max)


    def update(self,n):
        self.ui.progressBar.setValue(n)

    def connect(self):
        QObject.connect(self.ui.pushButton,SIGNAL("clicked()"),self.onDownloadButton)
        QObject.connect(self.ui.toolButton,SIGNAL("clicked()"),self.onSelectFolder)
        QObject.connect(self.thread,SIGNAL("update(int)"),self.update)


if __name__ == '__main__':

    gui = Gui()
    gui.window.show()
    gui.app.exec_()
    gui.app.exit(0)



