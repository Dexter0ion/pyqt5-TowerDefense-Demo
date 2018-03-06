#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_login import Ui_MainWindow
import qdarkstyle


class UiMain(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.btnLoginClicked)
    def btnLoginClicked(self):
        print(self.__dict__)    
        print('login button clicked')
        name = self.ui.leName.text()
        password = self.ui.lePassword.text()
        print(name, password)

        


        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = UiMain()
    ui.show()
    sys.exit(app.exec_())
