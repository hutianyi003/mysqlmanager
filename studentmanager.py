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

        self.config = dict()
        self.config["mysqlserver"] = {
            "host": "localhost",
            "port": 3306,
            "password": "981012aA$",
            "user": "root",
            "database": "sys"
        }

        self.connectMysql()
        self.showTableOption()
        self.fetchtable()

    def saveresult(self):
        exit()
    
    def deletetable(self):
        exit()

    def changetable(self):
        exit()
    
    def statuschange(self, status):
        self.statuslabel.setText(status)

    def showTableOption(self):
        if self.statuslabel.text() != "已连接":
            return
        cursor = self.conn.cursor()
        cursor.execute("SHOW TABLES")
        result = cursor.fetchall()

        for t in result:
            self.tableoption.insertItem(result.index(t),t[0])

        self.tablename = result[0][0]

    def connectMysql(self):
        config = self.config["mysqlserver"]
        try:
            self.conn = mysql.connector.connect(host=config["host"],port=config["port"],user=config["user"],password=config["password"],database=config["database"])
        except:
            self.statuschange("连接异常")
        else:
            self.statuschange("已连接")
        
    def fetchtable(self):
        cursor = self.conn.cursor()

        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='{}' AND TABLE_NAME='{}'".format(
            self.config["mysqlserver"]["database"], self.tablename))
        result = cursor.fetchall()
        col = len(result)
        col_label = [x[0] for x in result]

        cursor.execute("SELECT COUNT(*) FROM {}.{}".format(self.config["mysqlserver"]["database"],self.tablename))
        result = cursor.fetchall()
        row = result[0][0]

        cursor.execute("SELECT * FROM {}.{}".format(self.config["mysqlserver"]["database"],self.tablename))
        content = cursor.fetchall()

        table = self.showtable
        table.setRowCount(row)
        table.setColumnCount(col)
        table.setHorizontalHeaderLabels(col_label)

        for i in range(row):
            for j in range(col):
                table.setItem(i,j,QtWidgets.QTableWidgetItem(str(content[i][j])))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = studentmanager()

    main_window.show()
    sys.exit(app.exec_())
