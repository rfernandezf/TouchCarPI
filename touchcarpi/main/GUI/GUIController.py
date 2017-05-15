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
#   Description: This class has the responsibility of do the change between menus & initialize the GUI,
#   loading the Main Menu.
# *************************************************************************************************************

import sys

from PyQt5.QtWidgets import *

from DB.RAM_DB import RAM_DB
from .MainWindow import MainWindow
from .menu.MainMenu import MainMenu
from .menu.PlayAudioMenu import PlayAudioMenu
from .menu.PlayRadioMenu import PlayRadioMenu
from .menu.SelectAudioMenu import SelectAudioMenu
from model.AudioController import AudioController


class GUIController(object):
    """
    This class has the responsibility of do the change between menus & initialize the GUI.
    """

    def initialize(self):
        """
        Initialize the GUI and load the Main Menu.
        """

        app = QApplication(sys.argv)
        mainWindow = MainWindow()
        self.centralWidget = QStackedWidget()
        mainWindow.setCentralWidget(self.centralWidget)

        self.db = RAM_DB()
        self.mainMenuWidget = MainMenu(self)
        self.audioController = AudioController()

        self.centralWidget.addWidget(self.mainMenuWidget)
        self.centralWidget.setCurrentWidget(self.mainMenuWidget)

        sys.exit(app.exec_())

    def changeToMenu(self, menuname):
        """
        Changes to the menu passed by parameter.

        :param menuname: String with the name of the menu.
        """

        if (menuname == "MainMenu"):
            self.db.setCurrentMenu("MainMenu")
            self.centralWidget.setCurrentWidget(self.mainMenuWidget)

        elif (menuname == "SelectAudioMenu"):
            self.db.setCurrentMenu("SelectAudioMenu")
            self.selectAudioMenuWidget = SelectAudioMenu(self)
            self.centralWidget.addWidget(self.selectAudioMenuWidget)
            self.centralWidget.setCurrentWidget(self.selectAudioMenuWidget)

        elif (menuname == "PlayAudioMenu"):
            self.db.setCurrentMenu("PlayAudioMenu")
            self.playAudioMenuWidget = PlayAudioMenu(self)
            #Observer pattern register
            self.audioController.register(self.playAudioMenuWidget)
            self.centralWidget.addWidget(self.playAudioMenuWidget)
            self.centralWidget.setCurrentWidget(self.playAudioMenuWidget)

        elif (menuname == "PlayRadioMenu"):
            self.db.setCurrentMenu("PlayRadioMenu")
            self.playRadioMenuWidget = PlayRadioMenu(self)
            # Observer pattern register
            self.audioController.register(self.playRadioMenuWidget)
            self.centralWidget.addWidget(self.playRadioMenuWidget)
            self.centralWidget.setCurrentWidget(self.playRadioMenuWidget)
