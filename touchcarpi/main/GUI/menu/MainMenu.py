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
from model.AudioController import AudioController


from ..widgets.CustomLabel import CustomLabel
from ..widgets.buttons.MainMenu.Button_Music_MM import Button_Music_MM
from ..widgets.buttons.MainMenu.Button_Options_MM import Button_Options_MM
from ..widgets.buttons.MainMenu.Button_Radio_MM import Button_Radio_MM
from ..widgets.buttons.MainMenu.Button_POff_MM import Button_POff_MM
from ..widgets.MainMenuAudioWidget.MainMenuAudioWidget import MainMenuAudioWidget


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
        optionsButton = Button_Options_MM(controller).createButton(344, 96)
        poffButton = Button_POff_MM().createButton(344, 96)
        musicMenuLabel = CustomLabel().createLabel("Música      ", Qt.AlignCenter)
        musicMenuButton = Button_Music_MM(controller).createButton(97, 97)
        radioMenuLabel = CustomLabel().createLabel("Radio  ", Qt.AlignCenter)
        radioMenuButton = Button_Radio_MM(controller).createButton(97, 97)
        mainMenuAudioWidget = MainMenuAudioWidget()
        # Observer
        audioController.register(mainMenuAudioWidget)

        # Setting the layouts
        verticalBoxLayout = QVBoxLayout()
        hMainMenuTopWidgets = QHBoxLayout()
        hAppsMenuBox = QHBoxLayout()
        hLabelMenuBox = QHBoxLayout()
        hButtonsMenuBox = QHBoxLayout()

        verticalBoxLayout.addStretch()
        verticalBoxLayout.addStretch()

        hMainMenuTopWidgets.addStretch()
        hMainMenuTopWidgets.addWidget(mainMenuAudioWidget)
        verticalBoxLayout.addLayout(hMainMenuTopWidgets)
        verticalBoxLayout.addStretch()

        hAppsMenuBox.addStretch()
        hAppsMenuBox.addWidget(musicMenuButton)
        hAppsMenuBox.addStretch()
        hAppsMenuBox.addWidget(radioMenuButton)
        hAppsMenuBox.addStretch()
        verticalBoxLayout.addLayout(hAppsMenuBox)

        hLabelMenuBox.addStretch()
        hLabelMenuBox.addWidget(musicMenuLabel)
        hLabelMenuBox.addStretch()
        hLabelMenuBox.addWidget(radioMenuLabel)
        hLabelMenuBox.addStretch()

        verticalBoxLayout.addLayout(hLabelMenuBox)
        verticalBoxLayout.addStretch()

        hButtonsMenuBox.addWidget(optionsButton)

        hButtonsMenuBox.addStretch()
        hButtonsMenuBox.addWidget(poffButton)
        verticalBoxLayout.addLayout(hButtonsMenuBox)

        self.setLayout(verticalBoxLayout)