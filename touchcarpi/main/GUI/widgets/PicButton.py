
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class PicButton(QAbstractButton):

    def __init__(self, pixmap, pixmap_hover, pixmap_pressed, label, sizeX, sizeY, onClick, parent=None):
        super(PicButton, self).__init__(parent)
        self.label = label
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.onClick = onClick
        self.pixmap = pixmap
        self.pixmap_hover = pixmap_hover
        self.pixmap_pressed = pixmap_pressed

        self.pressed.connect(self.update)
        self.released.connect(self.update)



    def paintEvent(self, event):
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed
            print("Pene")

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), pix)


    def enterEvent(self, event):
        self.update()

    def leaveEvent(self, event):
        self.update()

    def sizeHint(self):
        return QSize(self.sizeX, self.sizeY)