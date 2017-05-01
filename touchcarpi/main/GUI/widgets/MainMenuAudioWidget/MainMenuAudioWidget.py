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
#   Description: This class provides a custimized widget for control the music in the Main Menu.
# *************************************************************************************************************

from abc import ABCMeta, abstractmethod
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ..CustomLabel import CustomLabel
from ..buttons.MainMenu.Button_Play_MM import Button_Play_MM
from ..buttons.MainMenu.Button_Pause_MM import Button_Pause_MM
from ..buttons.MainMenu.Button_Previous_MM import Button_Previous_MM
from ..buttons.MainMenu.Button_Next_MM import Button_Next_MM
from model.AudioController import AudioController
from model.AudioStatus import AudioStatus

class MainMenuAudioWidget (QWidget):
    __metaclass__ = ABCMeta
    def __init__ (self, parent = None):
        super(MainMenuAudioWidget, self).__init__(parent)

        self.playButton = Button_Play_MM().createButton(50, 50)
        self.pauseButton = Button_Pause_MM().createButton(50, 50)
        nextButton = Button_Next_MM().createButton(50, 50)
        previousButton = Button_Previous_MM().createButton(50, 50)
        audioController = AudioController()
        self.audioObject = audioController.getAudioObject()

        vBox1 = QVBoxLayout()
        hBox1 = QHBoxLayout()

        vBox1.addStretch()
        #Aquí el texto con la canción que se reproduce
        self.textLabel = CustomLabel().createLabel("Sin medios de reproducción", Qt.AlignCenter)
        vBox1.addWidget(self.textLabel)

        vBox1.addStretch()
        #Aquí el contenido del otro layout con los botones


        hBox1.addStretch()
        if (self.audioObject.getStatus() == AudioStatus.PAUSED):
            self.pauseButton.hide()
        else:
            self.playButton.hide()
        hBox1.addWidget(previousButton)
        hBox1.addStretch()
        hBox1.addWidget(self.playButton)
        hBox1.addWidget(self.pauseButton)
        hBox1.addStretch()
        hBox1.addWidget(nextButton)
        hBox1.addStretch()

        #Añadimos el layout al layout vertical
        vBox1.addLayout(hBox1)

        self.setLayout(vBox1)

    @abstractmethod
    def update(self, *args, **kwargs):
        self.updateView(*args, **kwargs)

    def updateView(self, *args, arg1, arg2):
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