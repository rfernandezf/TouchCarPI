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

from PyQt5.QtWidgets import *
from model.AudioController import AudioController

from ..widgets.MainMenu.MainMenuAudioWidget.MainMenuAudioWidget import MainMenuAudioWidget
from ..widgets.MainMenu.MainMenuButtonsWidget.MainMenuButtonsWidget import MainMenuButtonsWidget

from ..widgets.buttons.MainMenu.Button_POff_MM import Button_POff_MM
from ..widgets.buttons.MainMenu.Button_Options_MM import Button_Options_MM

class MainMenu(QWidget):
    """
    This class creates a custom widget with the Main Menu elements and layout.
    """

    def __init__(self, controller, parent=None):
        """
        Constructor of the MainMenu class.

        :param controller: GUIController object.
        """

        super(MainMenu, self).__init__(parent)

        audioController = AudioController()
        optionsButton = Button_Options_MM(controller).createButton(269, 100)
        optionsButton.setOppacity(0.3)
        poffButton = Button_POff_MM().createButton(269, 100)

        mainMenuAudioWidget = MainMenuAudioWidget()
        mainMenuButtonsWidget = MainMenuButtonsWidget(controller)

        # Observer
        audioController.register(mainMenuAudioWidget)

        # Setting the layouts
        verticalBoxLayout = QVBoxLayout()
        hMainMenuTopWidgets = QHBoxLayout()
        hButtonsMenuBox = QHBoxLayout()

        verticalBoxLayout.setContentsMargins(0, 0, 0, 0)
        verticalBoxLayout.addStretch()
        verticalBoxLayout.addStretch()

        hMainMenuTopWidgets.addStretch()
        hMainMenuTopWidgets.addWidget(mainMenuAudioWidget)
        verticalBoxLayout.addLayout(hMainMenuTopWidgets)
        verticalBoxLayout.addStretch()

        verticalBoxLayout.addWidget(mainMenuButtonsWidget)
        verticalBoxLayout.addStretch()

        hButtonsMenuBox.addWidget(optionsButton)

        hButtonsMenuBox.addStretch()
        hButtonsMenuBox.addWidget(poffButton)
        verticalBoxLayout.addLayout(hButtonsMenuBox)

        self.setLayout(verticalBoxLayout)