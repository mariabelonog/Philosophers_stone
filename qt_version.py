from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
import sys
from runn import runn
from final import final

from ph import Ui_mainWindow

class Main(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.runnn)

    def runnn(self):
        self.listWidget.clear()
        a = self.lineEdit.text().strip()
        b = self.lineEdit_2.text().strip()
        c = self.lineEdit_3.text().strip()
        res = runn(a, b, c)
        for i in res:
            if i[0] != ',':
                self.listWidget.addItem(i)
        res2 = final([a, b, c])
        for i in res2:
            if i[0] != ',':
                self.listWidget.addItem(i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())