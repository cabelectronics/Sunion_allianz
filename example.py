	
# file_browser_ui.py
  
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
  
import sys
  
# A simple widget consisting of a QLabel, a QLineEdit and a 
# QPushButton. The class could be implemented in a separate 
# script called, say, file_browser.py
class FileBrowser(QWidget):
  
    OpenFile = 0
    OpenFiles = 1
    OpenDirectory = 2
    SaveFile = 3
    
    def __init__(self, title, mode=OpenFile):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.browser_mode = mode
        self.filter_name = 'All files (*.*)'
        self.dirpath = QDir.currentPath()
        
        self.label = QLabel()
        self.label.setText(title)
        self.label.setFixedWidth(65)
        self.label.setFont(QFont("Arial",weight=QFont.Bold))
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(self.label)
        
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFixedWidth(180)
        
        layout.addWidget(self.lineEdit)
        
        self.button = QPushButton('Search')
        self.button.clicked.connect(self.getFile)
        layout.addWidget(self.button)
        layout.addStretch()
    #--------------------------------------------------------------------
    # For example, 
    #    setMode(FileBrowser.OpenFile)
    #    setMode(FileBrowser.OpenFiles)
    #    setMode(FileBrowser.OpenDirectory)
    #    setMode(FileBrowser.SaveFile)
    def setMode(mode):
        self.mode = mode
    #--------------------------------------------------------------------
    # For example, 
    #    setFileFilter('Images (*.png *.xpm *.jpg)')
    def setFileFilter(text):
        self.filter_name = text        
    #--------------------------------------------------------------------
    def setDefaultDir(path):
        self.dirpath = path
    #--------------------------------------------------------------------
    def getFile(self):
        self.filepaths = []
        
        if self.browser_mode == FileBrowser.OpenFile:
            self.filepaths.append(QFileDialog.getOpenFileName(self, caption='Choose File',
                                                    directory=self.dirpath,
                                                    filter=self.filter_name)[0])
        elif self.browser_mode == FileBrowser.OpenFiles:
            self.filepaths.extend(QFileDialog.getOpenFileNames(self, caption='Choose Files',
                                                    directory=self.dirpath,
                                                    filter=self.filter_name)[0])
        elif self.browser_mode == FileBrowser.OpenDirectory:
            self.filepaths.append(QFileDialog.getExistingDirectory(self, caption='Choose Directory',
                                                    directory=self.dirpath))
        else:
            options = QFileDialog.Options()
            if sys.platform == 'darwin':
                options |= QFileDialog.DontUseNativeDialog
            self.filepaths.append(QFileDialog.getSaveFileName(self, caption='Save/Save As',
                                                    directory=self.dirpath,
                                                    filter=self.filter_name,
                                                    options=options)[0])
        if len(self.filepaths) == 0:
            return
        elif len(self.filepaths) == 1:
            self.lineEdit.setText(self.filepaths[0])
        else:
            self.lineEdit.setText(",".join(self.filepaths))    
    #--------------------------------------------------------------------
    def setLabelWidth(self, width):
        self.label.setFixedWidth(width)    
    #--------------------------------------------------------------------
    def setlineEditWidth(self, width):
        self.lineEdit.setFixedWidth(width)
    #--------------------------------------------------------------------
    def getPaths(self):
        return self.filepaths
#-------------------------------------------------------------------
  
  
class Demo(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        
        # Ensure our window stays in front and give it a title
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle("File Browsing Dialog")
        self.setFixedSize(400, 300)
        
        # Create and assign the main (vertical) layout.
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)    
        
        self.fileBrowserPanel(vlayout)
        vlayout.addStretch()
        self.addButtonPanel(vlayout)
        self.show()
    #--------------------------------------------------------------------
    def fileBrowserPanel(self, parentLayout):
        vlayout = QVBoxLayout()
    	
        self.fileFB = FileBrowser('Open File', FileBrowser.OpenFile)
        self.filesFB = FileBrowser('Open Files', FileBrowser.OpenFiles)
        self.dirFB = FileBrowser('Open Dir', FileBrowser.OpenDirectory)
        self.saveFB = FileBrowser('Save File', FileBrowser.SaveFile)
        
        vlayout.addWidget(self.fileFB)
        vlayout.addWidget(self.filesFB)
        vlayout.addWidget(self.dirFB)
        vlayout.addWidget(self.saveFB)
        
        vlayout.addStretch()
        parentLayout.addLayout(vlayout)
    #--------------------------------------------------------------------
    def addButtonPanel(self, parentLayout):
        hlayout = QHBoxLayout()
        hlayout.addStretch()
        
        self.button = QPushButton("OK")
        self.button.clicked.connect(self.buttonAction)
        hlayout.addWidget(self.button)
        parentLayout.addLayout(hlayout)
    #--------------------------------------------------------------------
    def buttonAction(self):
        print(self.fileFB.getPaths())
        print(self.filesFB.getPaths())
        print(self.dirFB.getPaths())
        print(self.saveFB.getPaths())
        
    #--------------------------------------------------------------------
  
# ========================================================                
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    demo = Demo() # <<-- Create an instance
    demo.show()
    sys.exit(app.exec_())