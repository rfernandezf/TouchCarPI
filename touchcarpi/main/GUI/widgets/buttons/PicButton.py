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
#   Class name: PicButton.py
#   Description: Class that creates a customised button using a pair of pics (normal button and pressed button).
#   It also has a custom label, size and onClick event.
# *************************************************************************************************************

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time


class PicButton(QAbstractButton):
    """
    Class that creates a customised button using a pair of pics (normal button and pressed button).
    """

    def __init__(self, pixmap, pixmap_pressed, sizeX, sizeY, text, onClick, oppacity = 1.0, parent=None):
        """
        Constructor of the PicButton class.

        :param pixmap: Pic of the button in stand by.
        :param pixmap_pressed: Pic of the button pressed.
        :param sizeX: X size of the button.
        :param sizeY: Y size of the button.
        :param text: Text label of the button.
        :param onClick: On click behaviour of the button.
        """

        super(PicButton, self).__init__(parent)

        self.sizeX = sizeX
        self.sizeY = sizeY
        self.onClick = onClick
        self.pixmap = pixmap
        self.pixmap_hover = pixmap
        self.pixmap_pressed = pixmap_pressed
        self.pressed.connect(self.checkPressed)
        self.released.connect(self.checkReleased)
        self.clicked.connect(self.checkClick)
        self.setText(text)
        font = QFont('Myriada', 20)
        font.setBold(True)
        self.setStyleSheet("color: rgb(255, 255, 255);")
        self.setFont(font)
        self.buttonTimer = 0
        self.oppacityLevel = oppacity


    def checkPressed(self):
        self.buttonTimer = time.time()
        self.update()

    def checkReleased(self):
        self.buttonTimer = time.time() - self.buttonTimer
        self.update()

    def checkClick(self):
        if(self.buttonTimer > 1):
            isLongClick = True
        else:
            isLongClick = False

        self.onClick(isLongClick)

    def setOppacity(self, oppacity):
        self.oppacityLevel = oppacity

    def getOppacity(self):
        return self.oppacityLevel

    def paintEvent(self, event):
        """
        Paint event from the QT lib for draw the change of pics.

        :param event: Event from the QT lib.
        """

        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed

        painter = QPainter(self)
        painter.setOpacity(self.oppacityLevel)
        painter.drawPixmap(event.rect(), pix)
        painter.drawText(event.rect(), Qt.AlignCenter, self.text())


    def enterEvent(self, event):
        """
        Enter event from the QT lib.

        :param event: Event from the QT lib.
        """

        self.update()


    def leaveEvent(self, event):
        """
        Leave event from the QT lib.

        :param event: Event from the QT lib.
        """

        self.update()


    def sizeHint(self):
        """
        Size hint method override from the QT lib.
        """

        return QSize(self.sizeX, self.sizeY)