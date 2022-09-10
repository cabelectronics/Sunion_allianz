import os
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

 
def dialog():
    file = QFileDialog.getExistingDirectory()
    
    path_file = open('path.txt', 'w')
    path_file.write(file)
    print(file)
    sys.exit()
 
if __name__ == '__main__': 
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    win = dialog()

    sys.exit(app.exec_())
   