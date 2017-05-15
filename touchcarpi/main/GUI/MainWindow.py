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
#   Class name: MainWindow.py
#   Description: This class creates the MainWindow object, it creates the main window of the app where all
#   the stuff is drawn.
# *************************************************************************************************************

import platform

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    """
    This class creates the MainWindow object.
    """

    def __init__(self, parent=None):
        """
        Constructor of the Main Window class. Also loads the background.
        """

        super(MainWindow, self).__init__(parent)

        #palette = QPalette()
        #palette.setBrush(QPalette.Background, QBrush(QPixmap('themes/default/img/background_mm.gif')))



        self.movie = QMovie("themes/default/img/background_mm.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

        #self.setPalette(palette)

        self.setWindowTitle("TouchCarPi")
        self.showFullScreen()

        # We keep the cursor visible in windows for testing purposes
        if platform.system() == "Linux":
            self.setCursor(QCursor(Qt.BlankCursor))


    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)
