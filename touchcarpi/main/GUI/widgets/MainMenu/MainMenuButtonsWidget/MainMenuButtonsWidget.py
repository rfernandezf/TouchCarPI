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
#   Class name: MainMenuButtonsWidget.py
#   Description: This class provides a customized widget for the menu icons in the main menu.
# *************************************************************************************************************

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ....widgets.CustomLabel import CustomLabel
from ....widgets.buttons.MainMenu.Button_Music_MM import Button_Music_MM
from ....widgets.buttons.MainMenu.Button_Radio_MM import Button_Radio_MM

class MainMenuButtonsWidget (QWidget):
    """
    This class provides a customized widget for the menu icons in the main menu.
    """

    def __init__ (self, controller, parent = None):
        """
        Constructor of the MainMenuButtonsWidget class.
        """

        super(MainMenuButtonsWidget, self).__init__(parent)

        menuButtons = []
        labelsMenuButtons = []

        menuButtons.append(Button_Music_MM(controller).createButton(90, 90))
        menuButtons.append(Button_Radio_MM(controller).createButton(90, 90))
        labelsMenuButtons.append(CustomLabel().createLabel("Música", Qt.AlignCenter))
        labelsMenuButtons.append(CustomLabel().createLabel("Radio", Qt.AlignCenter))

        hButtonBarBox = QHBoxLayout()

        hButtonBarBox.addStretch()

        for i in range(0, len(menuButtons)):
            vButtonBox = QVBoxLayout()
            hMemoryButtonBox = QHBoxLayout()

            hMemoryButtonBox.addStretch()
            hMemoryButtonBox.addWidget(menuButtons[i])
            hMemoryButtonBox.addStretch()
            vButtonBox.addLayout(hMemoryButtonBox)

            hMemoryLabelBox = QHBoxLayout()
            hMemoryLabelBox.addStretch()
            hMemoryLabelBox.addWidget(labelsMenuButtons[i])
            hMemoryLabelBox.addStretch()
            vButtonBox.addLayout(hMemoryLabelBox)

            hButtonBarBox.addLayout(vButtonBox)
            hButtonBarBox.addStretch()

        self.setLayout(hButtonBarBox)