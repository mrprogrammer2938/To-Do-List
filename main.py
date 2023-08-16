# pip install PyQt5
# pip install pyqtdarktheme

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from form import Ui_MainWindow
import qdarktheme
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        qdarktheme.setup_theme("dark")
        
        self.setWindowTitle("To Do List")
        self.setFixedSize(853,600)
        
        self.ui.add_btn.clicked.connect(self.add_list)
        self.ui.delete_btn.clicked.connect(self.delete_list)
        self.ui.clear_btn.clicked.connect(self.clear_all)
        
    def add_list(self):
        text = self.ui.line.text()
        self.ui.my_list.addItem(text)
        self.ui.line.clear()
    def delete_list(self):
        item = self.ui.my_list.currentRow()
        self.ui.my_list.takeItem(item)
    def clear_all(self):
        self.ui.my_list.clear()
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("To Do List")
    win = Window()
    win.show()
    sys.exit(app.exec_())
    
main()
