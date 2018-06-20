import sys

from PyQt5.QtWidgets import QMessageBox
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
        self.tableoption.currentIndexChanged.connect(self.tablechange)
        self.showtable.horizontalHeader().sectionClicked.connect(self.headerclick)
        self.showtable.itemClicked.connect(self.cursorClicked)
        self.showtable.itemChanged.connect(self.tablechange)

        self.config = dict()
        self.oldtable = dict()
        self.config["mysqlserver"] = {
            "host": "localhost",
            "port": 3306,
            "password": "981012aA$",
            "user": "root",
            "database": "world"
        }
        self.oldtable["row"] = 0
        self.oldtable["change"] = []
        self.tablename = ''

        self.connectMysql()
        self.showTableOption()

    def saveresult(self):
        reply = QMessageBox.information(self,"保存","是否确定将改动保存到数据库？",QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.excuteSql("DROP TABLE {}.{}")
    
    def deletetable(self):
        reply = QMessageBox.warning(self,"警告","该操作会永久删除当前表格，是否继续？",QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.excuteSql("DROP TABLE {}.{}")
        self.showTableOption()

    def changetable(self):
        exit()
    
    def setserver(self):
        config = self.config["mysqlserver"]
        layout = QtWidgets.QFormLayout()
        

    def cursorClicked(self, index):
        self.infolabel.setText("({2},{3}) ({0},{1})     ".format(
            self.showtable.rowCount()-1, self.showtable.columnCount(), index.row(), index.column()))

    def excuteSql(self, command):
        if self.statuslabel.text() != "已连接":
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute(command.format(self.config["mysqlserver"]["database"],self.tablename))
            result = cursor.fetchall()
        except:
            return None
        else:
            return result

    def headerclick(self, index):
        self.showtable.sortItems(index,)
        return
    
    def statuschange(self, status):
        self.statuslabel.setText(status)

    def tablechange(self):
        self.tablename = self.tableoption.currentText()
        self.fetchtable()

    def showTableOption(self):
        if self.statuslabel.text() != "已连接":
            return
        result = self.excuteSql("SHOW TABLES")

        if result is None or len(result) == 0:
            self.tableoption.clear()
            self.showtable.clear()
            return 
        for t in result:
            self.tableoption.insertItem(result.index(t),t[0])

        self.tablename = result[0][0]
        self.fetchtable()

    def connectMysql(self):
        config = self.config["mysqlserver"]
        try:
            self.conn = mysql.connector.connect(host=config["host"],port=config["port"],user=config["user"],password=config["password"],database=config["database"])
        except:
            self.statuschange("连接异常")
        else:
            self.statuschange("已连接")
        
    def fetchtable(self):
        if self.tablename == None or self.tablename == '':
            return
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
        table.setRowCount(row+1)
        table.setColumnCount(col)
        table.setHorizontalHeaderLabels(col_label)

        self.oldtable["row"] = row
        for i in range(row):
            for j in range(col):
                c = str(content[i][j])
                item = QtWidgets.QTableWidgetItem()
                try:
                    float(c)
                except:
                    try:
                        int(c)
                    except:
                        item.setData(QtCore.Qt.EditRole,c)
                    else:
                        item.setData(QtCore.Qt.EditRole,int(c))
                else:
                    item.setData(QtCore.Qt.EditRole,float(c))
                table.setItem(i,j,item)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = studentmanager()

    main_window.show()
    sys.exit(app.exec_())
