# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\think\Documents\PyQt5\projectPyDefence\login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 500)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.leName = QtWidgets.QLineEdit(self.centralWidget)
        self.leName.setEnabled(True)
        self.leName.setGeometry(QtCore.QRect(10, 210, 250, 30))
        self.leName.setObjectName("leName")
        self.lePassword = QtWidgets.QLineEdit(self.centralWidget)
        self.lePassword.setEnabled(True)
        self.lePassword.setGeometry(QtCore.QRect(10, 270, 250, 30))
        self.lePassword.setObjectName("lePassword")
        self.lblName = QtWidgets.QLabel(self.centralWidget)
        self.lblName.setGeometry(QtCore.QRect(10, 190, 91, 16))
        self.lblName.setObjectName("lblName")
        self.lblPassword = QtWidgets.QLabel(self.centralWidget)
        self.lblPassword.setGeometry(QtCore.QRect(10, 250, 91, 16))
        self.lblPassword.setObjectName("lblPassword")
        self.btnLogin = QtWidgets.QPushButton(self.centralWidget)
        self.btnLogin.setGeometry(QtCore.QRect(160, 310, 100, 30))
        self.btnLogin.setObjectName("btnLogin")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
       
        




        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblName.setText(_translate("MainWindow", "Login Name"))
        self.lblPassword.setText(_translate("MainWindow", "Password"))
        self.btnLogin.setText(_translate("MainWindow", "LOGIN"))

    
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = .QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
