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
        self.tableoption = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableoption.sizePolicy().hasHeightForWidth())
        self.tableoption.setSizePolicy(sizePolicy)
        self.tableoption.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.tableoption.setFont(font)
        self.tableoption.setObjectName("tableoption")
        self.gridLayout.addWidget(self.tableoption, 0, 0, 1, 1)
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
        self.staticbutton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staticbutton.sizePolicy().hasHeightForWidth())
        self.staticbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        self.staticbutton.setFont(font)
        self.staticbutton.setObjectName("staticbutton")
        self.verticalLayout.addWidget(self.staticbutton)
        self.findbutton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findbutton.sizePolicy().hasHeightForWidth())
        self.findbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        self.findbutton.setFont(font)
        self.findbutton.setObjectName("findbutton")
        self.verticalLayout.addWidget(self.findbutton)
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
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.infolabel = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.infolabel.setFont(font)
        self.infolabel.setText("")
        self.infolabel.setObjectName("infolabel")
        self.gridLayout.addWidget(self.infolabel, 2, 0, 1, 1)
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
        self.actionmysqlconfig = QtWidgets.QAction(studentmanagerClass)
        self.actionmysqlconfig.setObjectName("actionmysqlconfig")
        self.actionexport = QtWidgets.QAction(studentmanagerClass)
        self.actionexport.setObjectName("actionexport")
        self.actionexit = QtWidgets.QAction(studentmanagerClass)
        self.actionexit.setObjectName("actionexit")
        self.actionrefesh = QtWidgets.QAction(studentmanagerClass)
        self.actionrefesh.setObjectName("actionrefesh")
        self.menu.addAction(self.actionexport)
        self.menu.addAction(self.actionexit)
        self.menu_3.addAction(self.actionrefesh)
        self.menu_3.addAction(self.actionmysqlconfig)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())

        self.retranslateUi(studentmanagerClass)
        QtCore.QMetaObject.connectSlotsByName(studentmanagerClass)

    def retranslateUi(self, studentmanagerClass):
        _translate = QtCore.QCoreApplication.translate
        studentmanagerClass.setWindowTitle(_translate("studentmanagerClass", "学生成绩管理系统"))
        self.statuslabel.setText(_translate("studentmanagerClass", "已连接"))
        self.staticbutton.setToolTip(_translate("studentmanagerClass", "计算统计量"))
        self.staticbutton.setText(_translate("studentmanagerClass", "统计"))
        self.findbutton.setToolTip(_translate("studentmanagerClass", "查找一定范围的数据"))
        self.findbutton.setText(_translate("studentmanagerClass", "查询"))
        self.savebutton.setToolTip(_translate("studentmanagerClass", "将当前更改保存至数据库"))
        self.savebutton.setText(_translate("studentmanagerClass", "保存更改"))
        self.menu.setTitle(_translate("studentmanagerClass", "文件"))
        self.menu_3.setTitle(_translate("studentmanagerClass", "设置"))
        self.actionmysqlconfig.setText(_translate("studentmanagerClass", "设置连接"))
        self.actionmysqlconfig.setToolTip(_translate("studentmanagerClass", "设置MySql数据库的连接"))
        self.actionexport.setText(_translate("studentmanagerClass", "导出"))
        self.actionexport.setToolTip(_translate("studentmanagerClass", "将当前表格导出为csv文件"))
        self.actionexit.setText(_translate("studentmanagerClass", "退出"))
        self.actionrefesh.setText(_translate("studentmanagerClass", "刷新"))

