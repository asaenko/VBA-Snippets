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
        self.radioG = QRadioButton()
        self.radioP = QRadioButton()
        self.radioG.setText('Google')
        self.radioP.setText('Proz')
        self.radioG.setChecked(True)
        l.addWidget(self.radioG)
        l.addWidget(self.radioP)
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
        if self.radioG.isChecked():
            f = '-g'
        elif self.radioP.isChecked():
            f = '-p'
        newSearch = multisearch.multiSearch(f, q)
        newSearch.search()
        self.searchBox.clear()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = searchWindow()
    w.show()
    sys.exit(app.exec_())
