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

from PyQt5.QtWidgets import *

from DB.RAM_DB import RAM_DB
from .MainWindow import MainWindow
from .menu.MainMenu import MainMenu
from .menu.PlayAudioMenu import PlayAudioMenu
from .menu.PlayRadioMenu import PlayRadioMenu
from .menu.SelectAudioMenu import SelectAudioMenu
from model.AudioController import AudioController


class GUIController(object):

    def initialize(self):
        app = QApplication(sys.argv)

        mainWindow = MainWindow()
        self.centralWidget = QStackedWidget()
        mainWindow.setCentralWidget(self.centralWidget)
        self.db = RAM_DB()
        self.mainMenuWidget = MainMenu(self, self.db)

        self.audioController = AudioController()

        self.centralWidget.addWidget(self.mainMenuWidget)
        self.centralWidget.setCurrentWidget(self.mainMenuWidget)

        sys.exit(app.exec_())

    def run(self):
        pass

    def getMenu(self):
        return self.actualMenu

    def changeToMenu(self, menuname):
        if (menuname == "MainMenu"):
            self.db.setActualMenu("MainMenu")
            self.centralWidget.setCurrentWidget(self.mainMenuWidget)
        elif (menuname == "SelectAudioMenu"):
            self.db.setActualMenu("SelectAudioMenu")
            self.selectAudioMenuWidget = SelectAudioMenu(self, self.db)
            self.audioController.register(self.selectAudioMenuWidget)
            self.centralWidget.addWidget(self.selectAudioMenuWidget)
            self.centralWidget.setCurrentWidget(self.selectAudioMenuWidget)
        elif (menuname == "PlayAudioMenu"):
            self.db.setActualMenu("PlayAudioMenu")
            self.playAudioMenuWidget = PlayAudioMenu(self, self.db)
            ###################################################################################
            # APPLYING THE OBSERVER PATTERN :)
            ###################################################################################
            self.audioController.register(self.playAudioMenuWidget)
            ###################################################################################
            self.centralWidget.addWidget(self.playAudioMenuWidget)
            self.centralWidget.setCurrentWidget(self.playAudioMenuWidget)
        elif (menuname == "PlayRadioMenu"):
            self.db.setActualMenu("PlayRadioMenu")
            self.playRadioMenuWidget = PlayRadioMenu(self, self.db)
            self.centralWidget.addWidget(self.playRadioMenuWidget)
            self.centralWidget.setCurrentWidget(self.playRadioMenuWidget)
