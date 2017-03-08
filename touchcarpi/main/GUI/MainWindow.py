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

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None, origPixmap=None):
        super(MainWindow, self).__init__(parent)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap('themes/default/img/background_mm.jpg')))

        self.setPalette(palette)
        self.setWindowTitle("TouchCarPi")
        self.showFullScreen()
