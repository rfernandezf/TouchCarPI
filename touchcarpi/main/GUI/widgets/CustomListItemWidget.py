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
#   Class name: CustomListItemWidget.py
#   Description: This class provides custimized widgets for each element of a list, for customize the
#   element representation of items in a ListWidget.
# *************************************************************************************************************

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from DB.RAM_DB import RAM_DB

class CustomListItemWidget (QWidget):
    """
    This class provides customized widgets for each element of a list.
    """

    def __init__ (self, parent = None):
        """
        Constructor of the CustomListItemWidget class.
        """

        super(CustomListItemWidget, self).__init__(parent)

        self.db = RAM_DB()
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
        """
        Sets the text of the label on the top of the item.

        :param text: Text of the label.
        """

        self.textUpQLabel.setText(text)

    def setPath (self, pathFile):
        """
        Sets the path to the song that is listed in the item.

        :param pathFile: Path to the file.
        """

        self.path = pathFile

    def getPath (self):
        """
        Returns the path to the song that is listed in the item.

        :return: Path to the song.
        """

        return self.path

    def setTextDown (self, text):
        """
        Sets the text of the label on the bottom of the item.

        :param text: Text of the label.
        """

        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        """
        Sets the icon of the item.

        :param imagePath: Full path to the icon.
        """

        pixmapIcon = QPixmap()

        loaded = pixmapIcon.load(imagePath)

        if(loaded == False):
            pixmapIcon.load(self.db.getArtworkNotFoundPath())

        self.iconQLabel.setPixmap(pixmapIcon.scaled(70,70))

        return loaded