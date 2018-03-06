import sys
from PyQt5 import QtWidgets
from Ui_login import Ui_MainWindow

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        ui = Ui_MainWindow()
        ui.setupUi(self)

    def btnLoginClicked(self):
        return 
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
    
