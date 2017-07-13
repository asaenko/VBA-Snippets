#!/usr/bin/env python3

import sys
from PySide.QtGui import *
import multisearch


class searchWindow(QWidget):
    def __init__(self):
        super(searchWindow, self).__init__()
        self.setWindowTitle('Mutlisearch')
        self.addWidgets()

    def addWidgets(self):
        l = QVBoxLayout()
        self.setLayout(l)
        self.searchBox = QLineEdit()
        self.searchBox.returnPressed.connect(self.startSearch)
        l.addWidget(self.searchBox)
        #add drop-down list
        self.searchButton = QPushButton()
        l.addWidget(self.searchButton)
        self.searchButton.setText('&Search')
        self.searchButton.clicked.connect(self.startSearch)
        self.exitButton = QPushButton()
        l.addWidget(self.exitButton)
        self.exitButton.setText('E&xit')
        self.exitButton.clicked.connect(lambda: sys.exit(0))

    def startSearch(self):
        q = self.searchBox.text()
        f = "Google" #for now google search only
        newSearch = multisearch.multiSearch(f, q) # Move this to init to initialize flags
        newSearch.search()
        self.searchBox.clear()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = searchWindow()
    w.show()
    sys.exit(app.exec_())
