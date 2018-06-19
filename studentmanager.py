import sys

from PyQt5 import QtWidgets,QtCore,QtGui
from Ui_studentmanager import Ui_studentmanagerClass

import mysql.connector


class studentmanager(QtWidgets.QMainWindow,Ui_studentmanagerClass):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("database.png"))

        self.statuslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.savebutton.clicked.connect(self.saveresult)
        self.deletebutton.clicked.connect(self.deletetable)
        self.deletebutton.clicked.connect(self.changetable)

        self.config = dict()
        self.config["mysqlserver"] = {
            "host": "localhost",
            "port": 3306,
            "password": "981012aA$",
            "user": "root"
        }
        self.fetchtable()
        self.connectMysql()

    def saveresult(self):
        exit()
    
    def deletetable(self):
        exit()

    def changetable(self):
        exit()
    
    def statuschange(self, status):
        self.statuslabel.setText(status)

    def connectMysql(self):
        config = self.config["mysqlserver"]
        try:
            self.conn = mysql.connector.connect(host=config["host"],port=config["port"],user=config["user"],password=config["password"])
        except:
            self.statuschange("连接异常")
        else:
            self.statuschange("已连接")
        
    def fetchtable(self):
        table = self.showtable
        table.setRowCount(10)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["person","id","math","chinese","english"])
        table.setItem(0,0,QtWidgets.QTableWidgetItem("xxx"))
        table.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = studentmanager()

    main_window.show()
    sys.exit(app.exec_())

