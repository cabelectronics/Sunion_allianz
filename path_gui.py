import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout

class MyApp(QFileDialog):
    
    def getDirectory(self):
        response = QFileDialog.getExistingDirectory(
            self,
            caption='Select a folder',
            directory=os.getcwd(),
            
        )
        print(response)
        return response 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')