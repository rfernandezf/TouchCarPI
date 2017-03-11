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
#   Class name: MainMenu.py
#   Description: This class creates a custom widget with the Main Menu elements and layout.
# *************************************************************************************************************

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ..widgets.buttons.Button_POff_MM import Button_POff_MM
from ..widgets.buttons.Button_Music_MM import Button_Music_MM
from ..widgets.buttons.Button_Options_MM import Button_Options_MM
from ..widgets.CustomLabel import CustomLabel

class MainMenu(QWidget):
    def __init__(self, controller, db, parent=None):
        super(MainMenu, self).__init__(parent)

        optionsButton = Button_Options_MM(controller).createButton(344, 96)
        poffButton = Button_POff_MM().createButton(344, 96)
        musicMenuLabel = CustomLabel().createLabel("Música", Qt.AlignCenter)
        musicMenuButton = Button_Music_MM(controller).createButton(97, 97)

        vbox = QVBoxLayout()

        vbox.addStretch()
        vbox.addStretch()
        vbox.addStretch()
        hMenuBox = QHBoxLayout()
        hMenuBox.addStretch()
        hMenuBox.addWidget(musicMenuButton)
        hMenuBox.addStretch()
        vbox.addLayout(hMenuBox)
        vbox.addWidget(musicMenuLabel)
        vbox.addStretch()

        hbox = QHBoxLayout()

        hbox.addWidget(optionsButton)

        hbox.addStretch()
        hbox.addWidget(poffButton)
        vbox.addLayout(hbox)

        self.setLayout(vbox)