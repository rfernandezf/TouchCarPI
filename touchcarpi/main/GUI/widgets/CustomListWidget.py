#*************************************************************************************************************
#  ________  ________  ___  ___  ________  ___  ___  ________  ________  ________  ________  ___
# |\___   ___\\   __  \|\  \|\  \|\   ____\|\  \|\  \|\   ____\|\   __  \|\   __  \|\   __  \|\  \
# \|___ \  \_\ \  \|\  \ \  \\\  \ \  \___|\ \  \\\  \ \  \___|\ \  \|\  \ \  \|\  \ \  \|\  \ \  \
#      \ \  \ \ \  \\\  \ \  \\\  \ \  \    \ \   __  \ \  \    \ \   __  \ \   _  _\ \   ____\ \  \
#       \ \  \ \ \  \\\  \ \  \\\  \ \  \____\ \  \ \  \ \  \____\ \  \ \  \ \  \\  \\ \  \___|\ \  \
#        \ \__\ \ \_______\ \_______\ \_______\ \__\ \__\ \_______\ \__\ \__\ \__\\ _\\ \__\    \ \__\
#         \|__|  \|_______|\|_______|\|_______|\|__|\|__|\|_______|\|__|\|__|\|__|\|__|\|__|     \|__|
#
# *************************************************************************************************************
#   Author: Rafael Fernández Flores (@Plata17 at GitHub)
#   Class name: CustomListWidget.py
#   Description: This class provides custimized widgets for each element of a list, for customize the
#   element representation of items in a ListWidget.
# *************************************************************************************************************


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CustomListItemWidget (QWidget):
    def __init__ (self, parent = None):
        super(CustomListItemWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()
        self.path = ""
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QHBoxLayout()
        self.iconQLabel      = QLabel()
        self.iconQLabel.setMaximumHeight(70)
        self.iconQLabel.setMaximumWidth(70)

        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)

        font1 = QFont('Myriada', 10)
        font1.setBold(True)
        font2 = QFont('Myriada', 9)
        font2.setBold(True)
        self.textUpQLabel.setFont(font1)
        self.textDownQLabel.setFont(font2)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(10, 0, 0);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(128, 128, 128);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setPath (self, text):
        self.path = text

    def getPath (self):
        return self.path

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        self.iconQLabel.setPixmap(QPixmap(imagePath))