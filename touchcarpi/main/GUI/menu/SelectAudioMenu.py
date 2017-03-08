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
#   Class name: SelectAudioMenu.py
#   Description: This class creates a custom widget with the Select Audio Menu elements and layout.
# *************************************************************************************************************

from PyQt5.QtWidgets import *

from touchcarpi.main.GUI.widgets.buttons.Button_Music_MM import Button_Music_MM
from touchcarpi.main.GUI.widgets.buttons.Button_Back_SAM import Button_Back_SAM

class SelectAudioMenu(QWidget):
    def __init__(self, controller, parent=None):
        super(SelectAudioMenu, self).__init__(parent)

        backButton = Button_Back_SAM(controller).createButton(344, 96)

        vbox = QVBoxLayout()

        vbox.addStretch()
        vbox.addStretch()
        vbox.addStretch()
        hMenuBox = QHBoxLayout()
        hMenuBox.addStretch()

        hMenuBox.addStretch()
        vbox.addLayout(hMenuBox)

        vbox.addStretch()

        hbox = QHBoxLayout()

        hbox.addWidget(backButton)

        hbox.addStretch()

        vbox.addLayout(hbox)

        self.setLayout(vbox)