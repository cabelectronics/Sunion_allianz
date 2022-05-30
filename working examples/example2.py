
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5 import QtCore
import sys
 
 
def dialog():
    file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                               "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
    if check:
        print(file)
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")
  
button = QPushButton(win)
button.setText("Press")
button.clicked.connect(dialog)
button.move(50,50)
 
win.show()
sys.exit(app.exec_())