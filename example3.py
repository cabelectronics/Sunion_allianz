import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout, QMainWindow

 
def dialog():
    file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                "Directory")
    if check:
        print(file)
 
if __name__ == '__main__': 
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    win = dialog()

    sys.exit(app.exec_())

    