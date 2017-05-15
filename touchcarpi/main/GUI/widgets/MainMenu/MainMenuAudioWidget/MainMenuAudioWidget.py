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
#   Class name: MainMenuAudioWidget.py
#   Description: This class provides a customized widget for control the music in the Main Menu.
# *************************************************************************************************************

from abc import ABCMeta, abstractmethod
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ....widgets.CustomLabel import CustomLabel
from ....widgets.buttons.MainMenu.Button_Play_MM import Button_Play_MM
from ....widgets.buttons.MainMenu.Button_Pause_MM import Button_Pause_MM
from ....widgets.buttons.MainMenu.Button_Previous_MM import Button_Previous_MM
from ....widgets.buttons.MainMenu.Button_Next_MM import Button_Next_MM
from model.AudioController import AudioController
from model.AudioStatus import AudioStatus

class MainMenuAudioWidget (QWidget):
    """
    This class provides a customized widget for control the music in the Main Menu.
    """

    __metaclass__ = ABCMeta

    def __init__ (self, parent = None):
        """
        Constructor of the MainMenuAudioWidget class.
        """

        super(MainMenuAudioWidget, self).__init__(parent)

        self.playButton = Button_Play_MM().createButton(60, 60)
        self.pauseButton = Button_Pause_MM().createButton(60, 60)
        nextButton = Button_Next_MM().createButton(60, 60)
        previousButton = Button_Previous_MM().createButton(60, 60)
        audioController = AudioController()
        self.audioObject = audioController.getAudioObject()

        verticalBoxLayout = QVBoxLayout()
        hRepButtonsBox = QHBoxLayout()

        verticalBoxLayout.addStretch()
        self.textLabel = CustomLabel().createLabel("Sin medios de reproducción", Qt.AlignCenter)
        verticalBoxLayout.addWidget(self.textLabel)
        verticalBoxLayout.addStretch()

        hRepButtonsBox.addStretch()
        if (self.audioObject.getStatus() == AudioStatus.PAUSED):
            self.pauseButton.hide()
        else:
            self.playButton.hide()
        hRepButtonsBox.addWidget(previousButton)
        hRepButtonsBox.addStretch()
        hRepButtonsBox.addWidget(self.playButton)
        hRepButtonsBox.addWidget(self.pauseButton)
        hRepButtonsBox.addStretch()
        hRepButtonsBox.addWidget(nextButton)
        hRepButtonsBox.addStretch()

        verticalBoxLayout.addLayout(hRepButtonsBox)

        self.setLayout(verticalBoxLayout)

    @abstractmethod
    def update(self, *args, **kwargs):
        """
        Update method of the observer pattern.

        :param args: args
        :param kwargs: kwargs
        """

        self.updateView(*args, **kwargs)

    def updateView(self, *args, arg1, arg2):
        """
        Update view method of the observer pattern.

        :param args: Name of the notification.
        :param arg1: Other data.
        :param arg2: Other data.
        """

        if (args[0] == "NewMetaData"):

            if arg2[1] == None:
                titleText = "Artista desconocido" + " - " + arg2[0]
            else:
                titleText = arg2[1] + " - " + arg2[0]

            self.textLabel.setText(titleText)
            self.playButton.hide()
            self.pauseButton.show()

        elif (args[0] == "AudioPaused"):
            self.playButton.show()
            self.pauseButton.hide()

        elif (args[0] == "AudioResumed"):
            self.playButton.hide()
            self.pauseButton.show()