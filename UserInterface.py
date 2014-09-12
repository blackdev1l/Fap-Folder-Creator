from PyQt4.QtGui import QMainWindow, QApplication, QFileDialog, QDialog, QLabel
from PyQt4.QtCore import SIGNAL,QObject, QStringList, QString
from interface import Ui_MainWindow
import sys
from ffc import check_dir,main


class Gui:

    def __init__(self):
        self.curr = 0
        self.app = QApplication(sys.argv)
        self.fileManager = QFileDialog()
        self.fileManager.setFileMode(self.fileManager.DirectoryOnly)
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.connect()

    def onDownloadButton(self):
        urlText = str(self.ui.urlEdit.text())
        dirText =  str(self.ui.dirEdit.text())

        check_dir(dirText)
        main(self,urlText, dirText, 10)

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

    def getProgress(self,curr,max):
        self.ui.progressBar.setRange(0,max)
        self.ui.maxImageLabel.setText(QString(max))
        self.ui.minImageLabel.setText(QString(curr))
    def onProgress(self):
        return self.curr


    def show(self):
        self.window.show()
        sys.exit(self.app.exec_())
    def connect(self):
        QObject.connect(self.ui.pushButton,SIGNAL("clicked()"),self.onDownloadButton)
        QObject.connect(self.ui.toolButton,SIGNAL("clicked()"),self.onSelectFolder)
        QObject.connect(self.ui.progressBar,SIGNAL("valueChanged()"),self.onProgress)


