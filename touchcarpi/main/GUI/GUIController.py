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
#   Class name: GUIController.py
#   Description: This class has the responsibility of do the change between menus & initialize the GUI
#   loading the main menu.
# *************************************************************************************************************

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from .widgets.Button_Options_MM import Button_Options_MM

def buttonP():
    button = Button_Options_MM()
    button2 = button.createButton("Hello world", 147, 59)

    grid = QGridLayout()
    grid.setSpacing(10)
    grid.addWidget(button2, 0, 1)


    return grid



class GUIController:

    def __init__(self):
        pass

    def initialize(self):
        class ImageView(QGraphicsView):
            def __init__(self, parent=None, origPixmap=None):
                """
                QGraphicsView that will show an image scaled to the current widget size
                using events
                """
                super(ImageView, self).__init__(parent)
                self.origPixmap = origPixmap
                QMetaObject.connectSlotsByName(self)
                self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


                self.setLayout(buttonP())

            def resizeEvent(self, event):
                """
                Handle the resize event.
                """
                size = event.size()
                item = self.items()[0]

                # using current pixmap after n-resizes would get really blurry image
                # pixmap = item.pixmap()
                pixmap = self.origPixmap
                pixmap = pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.centerOn(1.0, 1.0)
                item.setPixmap(pixmap)



        app = QApplication(sys.argv)

        pic = QPixmap('pic2.jpg')
        grview = ImageView(origPixmap=pic)

        scene = QGraphicsScene()
        scene.addPixmap(pic)




        grview.setScene(scene)
        grview.showFullScreen()



        sys.exit(app.exec_())


    def run(self):
        pass

    def changeToMenu(self, menuname):
        pass