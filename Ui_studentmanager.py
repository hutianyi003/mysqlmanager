# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Hu Tianyi\Desktop\studentmanager\studentmanager.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_studentmanagerClass(object):
    def setupUi(self, studentmanagerClass):
        studentmanagerClass.setObjectName("studentmanagerClass")
        studentmanagerClass.resize(685, 478)
        self.centralWidget = QtWidgets.QWidget(studentmanagerClass)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.statuslabel = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel.sizePolicy().hasHeightForWidth())
        self.statuslabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        self.statuslabel.setFont(font)
        self.statuslabel.setObjectName("statuslabel")
        self.gridLayout.addWidget(self.statuslabel, 0, 1, 1, 1)
        self.showtable = QtWidgets.QTableWidget(self.centralWidget)
        self.showtable.setObjectName("showtable")
        self.showtable.setColumnCount(0)
        self.showtable.setRowCount(0)
        self.gridLayout.addWidget(self.showtable, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.refreshbutton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshbutton.sizePolicy().hasHeightForWidth())
        self.refreshbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        self.refreshbutton.setFont(font)
        self.refreshbutton.setObjectName("refreshbutton")
        self.verticalLayout.addWidget(self.refreshbutton)
        self.savebutton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savebutton.sizePolicy().hasHeightForWidth())
        self.savebutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        self.savebutton.setFont(font)
        self.savebutton.setObjectName("savebutton")
        self.verticalLayout.addWidget(self.savebutton)
        self.deletebutton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deletebutton.sizePolicy().hasHeightForWidth())
        self.deletebutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        self.deletebutton.setFont(font)
        self.deletebutton.setObjectName("deletebutton")
        self.verticalLayout.addWidget(self.deletebutton)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        studentmanagerClass.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(studentmanagerClass)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 685, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setToolTipsVisible(True)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setToolTipsVisible(True)
        self.menu_3.setObjectName("menu_3")
        studentmanagerClass.setMenuBar(self.menuBar)
        self.actionnewtable = QtWidgets.QAction(studentmanagerClass)
        self.actionnewtable.setObjectName("actionnewtable")
        self.actionmysqlconfig = QtWidgets.QAction(studentmanagerClass)
        self.actionmysqlconfig.setObjectName("actionmysqlconfig")
        self.actionstatic = QtWidgets.QAction(studentmanagerClass)
        self.actionstatic.setObjectName("actionstatic")
        self.actionexport = QtWidgets.QAction(studentmanagerClass)
        self.actionexport.setObjectName("actionexport")
        self.actionexit = QtWidgets.QAction(studentmanagerClass)
        self.actionexit.setObjectName("actionexit")
        self.actionrefresh = QtWidgets.QAction(studentmanagerClass)
        self.actionrefresh.setObjectName("actionrefresh")
        self.menu.addAction(self.actionnewtable)
        self.menu.addAction(self.actionexport)
        self.menu.addAction(self.actionexit)
        self.menu_3.addAction(self.actionmysqlconfig)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())

        self.retranslateUi(studentmanagerClass)
        QtCore.QMetaObject.connectSlotsByName(studentmanagerClass)

    def retranslateUi(self, studentmanagerClass):
        _translate = QtCore.QCoreApplication.translate
        studentmanagerClass.setWindowTitle(_translate("studentmanagerClass", "学生成绩管理系统"))
        self.statuslabel.setText(_translate("studentmanagerClass", "已连接"))
        self.refreshbutton.setToolTip(_translate("studentmanagerClass", "切换至数据库中的另一表格"))
        self.refreshbutton.setText(_translate("studentmanagerClass", "刷新"))
        self.savebutton.setToolTip(_translate("studentmanagerClass", "将当前更改保存至数据库"))
        self.savebutton.setText(_translate("studentmanagerClass", "保存更改"))
        self.deletebutton.setToolTip(_translate("studentmanagerClass", "在数据库中删除当前表格"))
        self.deletebutton.setText(_translate("studentmanagerClass", "删除表格"))
        self.label.setText(_translate("studentmanagerClass", "总行数： 总列数： 当前位置(1,1)"))
        self.menu.setTitle(_translate("studentmanagerClass", "文件"))
        self.menu_3.setTitle(_translate("studentmanagerClass", "设置"))
        self.actionnewtable.setText(_translate("studentmanagerClass", "新建表格"))
        self.actionnewtable.setToolTip(_translate("studentmanagerClass", "在数据库中新建一张表格"))
        self.actionnewtable.setShortcut(_translate("studentmanagerClass", "Ctrl+N"))
        self.actionmysqlconfig.setText(_translate("studentmanagerClass", "设置连接"))
        self.actionmysqlconfig.setToolTip(_translate("studentmanagerClass", "设置MySql数据库的连接"))
        self.actionstatic.setText(_translate("studentmanagerClass", "统计"))
        self.actionstatic.setToolTip(_translate("studentmanagerClass", "进行统计计算"))
        self.actionexport.setText(_translate("studentmanagerClass", "导出"))
        self.actionexport.setToolTip(_translate("studentmanagerClass", "将当前表格导出为csv文件"))
        self.actionexport.setShortcut(_translate("studentmanagerClass", "Ctrl+E"))
        self.actionexit.setText(_translate("studentmanagerClass", "退出"))
        self.actionrefresh.setText(_translate("studentmanagerClass", "刷新"))

