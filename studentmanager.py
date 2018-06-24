import sys
import csv

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtCore, QtGui

from Ui_studentmanager import Ui_studentmanagerClass

import mysql.connector


class studentmanager(QtWidgets.QMainWindow, Ui_studentmanagerClass):
    def __init__(self, parent=None):
        super(studentmanager, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("database.png"))

        self.statuslabel.setAlignment(QtCore.Qt.AlignCenter)

        self.savebutton.clicked.connect(self.saveresult)
        self.findbutton.clicked.connect(self.userQuery)
        #self.deletebutton.clicked.connect(self.deletetable)

        self.actionexport.triggered.connect(self.outcsv)
        self.actionexit.triggered.connect(self.close)
        self.actionmysqlconfig.triggered.connect(self.setserver)
        self.actionrefesh.triggered.connect(self.fetchtable)

        self.tableoption.currentIndexChanged.connect(self.tablechange)

        self.showtable.horizontalHeader().sectionClicked.connect(self.headerclick)
        self.showtable.horizontalHeader().sectionDoubleClicked.connect(self.headerDoubleClick)
        self.showtable.itemClicked.connect(self.cursorClicked)
        self.showtable.itemChanged.connect(self.itemchange)


        self.config = dict()
        self.oldtable = dict()
        self.config["mysqlserver"] = {
            "host": "localhost",
            "port": 3306,
            "password": "temppassword",
            "user": "client",
            "database": "test"
        }
        self.tablename = ''

        self.connectMysql()
        self.showTableOption()

    def userQuery(self):
        dialog = queryDialog(self,self.oldtable["header"])
        dialog.show()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            query = dialog.getquery()
            name = query["name"]
            left = self.itemadaptor(query["min"])
            right = self.itemadaptor(query["max"])
            result = self.excuteSql("SELECT * FROM {{}}.{{}} WHERE {0} >= {1} AND {0} <= {2}".format(name,left,right))
            if result is None or len(result) == 0:
                QtWidgets.QMessageBox.information(self,"提示","无查询结果",QtWidgets.QMessageBox.Ok)
                return
            table = self.showtable
            table.blockSignals(True)
            table.clear()
            row = len(result)
            col = self.oldtable["col"]
            for i in range(row):
                for j in range(col):
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(QtCore.Qt.EditRole, self.itemadaptor(result[i][j]))
                    table.setItem(i, j, item)
            table.blockSignals(False)
            print(result)

        return

    def saveresult(self):
        reply = QMessageBox.information(
            self, "保存", "是否确定将改动保存到数据库？", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            desc = self.oldtable['desc']
            pri = None
            for row in desc:
                if row[3] == b'PRI':
                    pri = str(row[0])
            if pri is None:
                QtWidgets.QMessageBox.critical(self,"错误","该表格没有主键,请联系数据库管理员!",QtWidgets.QMessageBox.Ok)
                return
            label = self.oldtable["header"]
            col = len(label)
            desc = self.oldtable["desc"]

            pri = str(pri)
            pri_order = label.index(pri)

            if self.oldtable["row"] < self.showtable.rowCount()-1:
                header = "("
                for i in range(col):
                    header+=label[i]
                    if i != col - 1:
                        header+=','
                header += ")"
                for i in range(self.oldtable["row"], self.showtable.rowCount()-1):
                    value = "("
                    for j in range(col):
                        item = self.showtable.item(i, j)
                        if item is None:
                            value += "null"
                        else:
                            itemtype = str(desc[j][1])
                            if "char" in itemtype or "CHAR" in itemtype:
                                value+="'{}'".format(item.text())
                            else:
                                value += item.text()
                        if j != col - 1:
                            value+=','
                    value += ")"
                    self.excuteSql("INSERT INTO {}.{} " + header + " VALUES" + value)
            for c in self.oldtable["change"]:
                i = c[0]
                j = c[1]
                item = self.showtable.item(i, j)
                if item is None:
                    continue
                else:
                    itemtype = str(desc[j][1])
                    if "char" in itemtype or "CHAR" in itemtype:
                        info ="'{}'".format(item.text())
                    else:
                        info = item.text()
                    colname = label[j]
                    priinfo = self.showtable.item(i,pri_order).text()
                    
                self.excuteSql("UPDATE {}.{} SET " +colname+"="+info+" WHERE "+pri+"="+priinfo)
                '''
                if self.excuteSql("UPDATE {}.{} SET " +colname+"="+info+" WHERE "+pri+"="+priinfo) is None:
                    self.conn.rollback()
                    QtWidgets.QMessageBox.critical(self,"错误","非法修改({},{})".format(i,j),QtWidgets.QMessageBox.Ok)
                    return
                '''
            self.conn.commit()
            self.fetchtable()

    def deletetable(self):
        reply = QMessageBox.warning(
            self, "警告", "该操作会永久删除当前表格，是否继续？", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.excuteSql("DROP TABLE {}.{}")
        self.showTableOption()
    
    def outcsv(self):
        if self.showtable.columnCount() == 0 or self.showtable.rowCount()== 0:
            QtWidgets.QMessageBox.critical(self,"错误","当前表格无法导出",QtWidgets.QMessageBox.Ok)
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self, "选择保存路径"))
        name = self.tablename+'.csv'
        print(file,name)
        with open(file + '/' + name,'w',newline = '',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.oldtable["header"])
            writer.writerows(self.oldtable["content"])

    def itemchange(self, item):
        font = item.font()
        font.setBold(True)
        item.setFont(font)
        self.oldtable['change'].append((item.row(),item.column()))
        if item.row() == self.showtable.rowCount()-1:
            self.showtable.insertRow(self.showtable.rowCount())
        self.tablechanged = True

    def setserver(self):
        inputdia = inputdialog(
            parent=self, currentconfig=self.config["mysqlserver"])
        inputdia.show()
        if inputdia.exec_() == QtWidgets.QDialog.Accepted:
            self.config["mysqlserver"] = inputdia.getconfig()
            self.connectMysql()
            self.showTableOption()

    def cursorClicked(self, index):
        self.infolabel.setText("({2},{3}) ({0},{1})     ".format(
            self.showtable.rowCount()-1, self.showtable.columnCount(), index.row(), index.column()))

    def excuteSql(self, command):
        if self.statuslabel.text() != "已连接":
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute(command.format(
                self.config["mysqlserver"]["database"], self.tablename))
            result = cursor.fetchall()
        except:
            return None
        else:
            return result

    def headerclick(self, index):
        if self.tablechanged:
            QtWidgets.QMessageBox.information(self,"无法排序","更改过的表格无法进行排序,请先保存更改")
            return
        self.showtable.sortItems(index)

    def headerDoubleClick(self, index):
        if self.tablechanged:
            QtWidgets.QMessageBox.information(self,"无法排序","更改过的表格无法进行排序,请先保存更改")
            return
        self.showtable.sortItems(index,QtCore.Qt.DescendingOrder)

    def statuschange(self, status):
        self.statuslabel.setText(status)

    def tablechange(self):
        self.tablename = self.tableoption.currentText()
        self.fetchtable()

    def showTableOption(self):
        if self.statuslabel.text() != "已连接":
            self.tableoption.clear()
            self.showtable.clear()
            return
        result = self.excuteSql("SHOW TABLES")
        self.tableoption.clear()

        if result is None or len(result) == 0:
            self.tableoption.clear()
            self.showtable.clear()
            return
        self.tableoption.blockSignals(True)
        for t in result:
            self.tableoption.insertItem(result.index(t), t[0])
        self.tableoption.blockSignals(False)

        self.tablename = result[0][0]
        self.fetchtable()

    def connectMysql(self):
        config = self.config["mysqlserver"]
        try:
            self.conn = mysql.connector.connect(
                host=config["host"], port=config["port"], user=config["user"], password=config["password"], database=config["database"])
        except:
            self.statuschange("连接异常")
        else:
            self.statuschange("已连接")

    def itemadaptor(self, c):
        try:
            int(c)
        except:
            try:
                float(c)
            except:
                return c
            else:
                return float(c)
        else:
            return int(c)

    def fetchtable(self):
        if self.tablename == None or self.tablename == '':
            return

        self.oldtable["row"] = 0
        self.oldtable["change"] = []
        self.showtable.clear()

        result = self.excuteSql("SELECT COUNT(*) FROM {}.{}")
        row = result[0][0]

        content = self.excuteSql("SELECT * FROM {}.{}")

        desc = self.excuteSql("DESC {}.{}")
        col = len(desc)
        col_label = [x[0] for x in desc]
        self.oldtable['desc'] = desc

        table = self.showtable
        table.setRowCount(row+1)
        table.setColumnCount(col)
        table.setHorizontalHeaderLabels(col_label)

        self.oldtable["row"] = row
        self.oldtable["col"] = len(col_label)
        self.oldtable["content"] = content
        self.oldtable["header"] = col_label
        self.showtable.blockSignals(True)
        for i in range(row):
            for j in range(col):
                item = QtWidgets.QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, self.itemadaptor(content[i][j]))
                table.setItem(i, j, item)
        self.showtable.blockSignals(False)
        self.tablechanged = False


class inputdialog(QtWidgets.QDialog):
    def __init__(self, parent=None, currentconfig=dict()):
        super(inputdialog, self).__init__(parent, QtCore.Qt.WindowSystemMenuHint |
                                          QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)

        self.setWindowTitle("服务器设置")

        config = currentconfig
        self.userhost = QtWidgets.QLineEdit(config["host"], self)
        self.userport = QtWidgets.QLineEdit(str(config["port"]), self)
        self.userpasswd = QtWidgets.QLineEdit(config["password"], self)
        self.userpasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.useruser = QtWidgets.QLineEdit(config["user"], self)
        self.userdatabase = QtWidgets.QLineEdit(config["database"], self)

        layout = QtWidgets.QFormLayout(self)
        layout.addRow(QtWidgets.QLabel("Server:"))
        layout.addRow("Host:", self.userhost)
        layout.addRow("Port:", self.userport)
        layout.addRow("User:", self.useruser)
        layout.addRow("Password:", self.userpasswd)
        layout.addRow("Database:", self.userdatabase)

        buttonBox = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, QtCore.Qt.Horizontal, self)

        layout.addRow(buttonBox)

        self.layout = layout

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getconfig(self):
        config = dict()
        config["host"] = self.userhost.text()
        config["user"] = self.useruser.text()
        config["password"] = self.userpasswd.text()
        config["port"] = self.userport.text()
        config["database"] = self.userdatabase.text()
        return config

class queryDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, namelist = []):
        super(queryDialog, self).__init__(parent, QtCore.Qt.WindowSystemMenuHint |
                                          QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)

        self.setWindowTitle("查询")

        self.username = QtWidgets.QComboBox(self)
        self.usermin = QtWidgets.QLineEdit('0', self)
        self.usermax = QtWidgets.QLineEdit('0', self)

        self.username.addItems(namelist)
        layout = QtWidgets.QFormLayout(self)
        layout.addRow("列名称:", self.username)
        layout.addRow("最小值:", self.usermin)
        layout.addRow("最大值:", self.usermax)

        buttonBox = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, QtCore.Qt.Horizontal, self)

        layout.addRow(buttonBox)

        self.layout = layout

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getquery(self):
        query = dict()
        query["name"] = self.username.currentText()
        query["min"] = self.usermin.text()
        query["max"] = self.usermax.text()
        return query

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = studentmanager()

    main_window.show()
    sys.exit(app.exec_())
