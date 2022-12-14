# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CS2Project2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from random import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color: rgb(203, 250, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TTT_label = QtWidgets.QLabel(self.centralwidget)
        self.TTT_label.setGeometry(QtCore.QRect(200, -10, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.TTT_label.setFont(font)
        self.TTT_label.setObjectName("TTT_label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 130, 466, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gameboard = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gameboard.setContentsMargins(0, 0, 0, 0)
        self.gameboard.setObjectName("gameboard")
        self.B2 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.clicked())
        self.B2.setMinimumSize(QtCore.QSize(150, 150))
        self.B2.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.B2.setFont(font)
        self.B2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.B2.setText("")
        self.B2.setObjectName("B2")
        self.gameboard.addWidget(self.B2, 1, 1, 1, 1)
        self.A3 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.clicked())
        self.A3.setMinimumSize(QtCore.QSize(150, 150))
        self.A3.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.A3.setFont(font)
        self.A3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.A3.setText("")
        self.A3.setObjectName("A3")
        self.gameboard.addWidget(self.A3, 0, 2, 1, 1)
        self.C3 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.clicked())
        self.C3.setMinimumSize(QtCore.QSize(150, 150))
        self.C3.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.C3.setFont(font)
        self.C3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C3.setText("")
        self.C3.setObjectName("C3")
        self.gameboard.addWidget(self.C3, 2, 2, 1, 1)
        self.B1 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.clicked())
        self.B1.setMinimumSize(QtCore.QSize(150, 150))
        self.B1.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.B1.setFont(font)
        self.B1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.B1.setText("")
        self.B1.setObjectName("B1")
        self.gameboard.addWidget(self.B1, 1, 0, 1, 1)
        self.A2 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.clicked())
        self.A2.setMinimumSize(QtCore.QSize(150, 150))
        self.A2.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.A2.setFont(font)
        self.A2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.A2.setText("")
        self.A2.setObjectName("A2")
        self.gameboard.addWidget(self.A2, 0, 1, 1, 1)
        self.A1 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.clicked())
        self.A1.setMinimumSize(QtCore.QSize(150, 150))
        self.A1.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.A1.setFont(font)
        self.A1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.A1.setText("")
        self.A1.setObjectName("A1")
        self.gameboard.addWidget(self.A1, 0, 0, 1, 1)
        self.C2 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.clicked())
        self.C2.setMinimumSize(QtCore.QSize(150, 150))
        self.C2.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.C2.setFont(font)
        self.C2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C2.setText("")
        self.C2.setObjectName("C2")
        self.gameboard.addWidget(self.C2, 2, 1, 1, 1)
        self.B3 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.clicked())
        self.B3.setMinimumSize(QtCore.QSize(150, 150))
        self.B3.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.B3.setFont(font)
        self.B3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.B3.setText("")
        self.B3.setObjectName("B3")
        self.gameboard.addWidget(self.B3, 1, 2, 1, 1)
        self.C1 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked = lambda: self.clicked())
        self.C1.setMinimumSize(QtCore.QSize(150, 150))
        self.C1.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.C1.setFont(font)
        self.C1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C1.setText("")
        self.C1.setObjectName("C1")
        self.gameboard.addWidget(self.C1, 2, 0, 1, 1)
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(50, 660, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.computer_label = QtWidgets.QLabel(self.centralwidget)
        self.computer_label.setGeometry(QtCore.QRect(430, 660, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.computer_label.setFont(font)
        self.computer_label.setObjectName("computer_label")
        self.userscore_label = QtWidgets.QLabel(self.centralwidget)
        self.userscore_label.setGeometry(QtCore.QRect(190, 670, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.userscore_label.setFont(font)
        self.userscore_label.setText("")
        self.userscore_label.setObjectName("userscore_label")
        self.computerscore_label = QtWidgets.QLabel(self.centralwidget)
        self.computerscore_label.setGeometry(QtCore.QRect(630, 660, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.computerscore_label.setFont(font)
        self.computerscore_label.setText("")
        self.computerscore_label.setObjectName("computerscore_label")
        self.game_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.reset())
        self.game_button.setGeometry(QtCore.QRect(290, 610, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.game_button.setFont(font)
        self.game_button.setStyleSheet("background-color: rgb(218, 208, 200);")
        self.game_button.setObjectName("game_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TTT_label.setText(_translate("MainWindow", "Tic-Tac-Toe"))
        self.user_label.setText(_translate("MainWindow", "User Score: "))
        self.computer_label.setText(_translate("MainWindow", "Computer Score: "))
        self.game_button.setText(_translate("MainWindow", "New Game"))





    def clicked(self, b):
        b.setText('X')
        b.setEnabled(False)
        #     option = random.randint(1,9)
        #     if option ==1 and self.A1==True:
        #         b.setText('O')
        #         b.setEnabled(False)
        #     if option ==2 and self.A2==True:
        #         b.setText('O')
        #         b.setEnabled(False)
        #     if option ==3 and self.A3==True:
        #         b.setText('O')
        #         b.setEnabled(False)
        #     if option ==4 and self.B1==True:
        #         b.setText('O')
        #         b.setEnabled(False)
        #     if option ==5 and self.B2==True:
        #         b.setText('O')
        #         b.setEnabled(False)
        #     if option ==6 and self.B3==True:
        #         b.setText('O')
        #         b.setEnabled(False)
        #     if option ==7 and self.C1==True:
        #         b.setText('O')
        #         b.setEnabled(False)
        #     if option ==8 and self.C2==True:
        #         b.setText('O')
        #         b.setEnabled(False)
        #     if option ==9 and self.C3==True:
        #         b.setText('O')
        #         b.setEnabled(False)

    def reset(self):
        button_list = [
        self.A1,
        self.A2,
        self.A3,
        self.B1,
        self.B2,
        self.B3,
        self.C1,
        self.C2,
        self.C3]

        for b in button_list:
            b.setText('')
            b.setEnabled(True)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
