import sys

from PyQt5 import QtWidgets,QtCore,QtGui
from Ui_studentmanager import Ui_studentmanagerClass


class studentmanager(QtWidgets.QMainWindow,Ui_studentmanagerClass):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("database.png"))

        self.savebutton.clicked.connect(self.saveresult)
        self.deletebutton.clicked.connect(self.deletetable)
        self.deletebutton.clicked.connect(self.changetable)

        self.showmytable()

    def saveresult(self):
        exit()
    
    def deletetable(self):
        exit()

    def changetable(self):
        exit()
    
    def connectMysql(self):
        exit()
        
    def showmytable(self):
        table = self.showtable
        table.setHorizontalHeaderLabels(["person","id","math","chinese","english"])
        table.setRowCount(10)
        table.setColumnCount(5)
        table.setItem(0,0,QtWidgets.QTableWidgetItem("xxx"))
        table.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = studentmanager()

    main_window.show()
    sys.exit(app.exec_())

