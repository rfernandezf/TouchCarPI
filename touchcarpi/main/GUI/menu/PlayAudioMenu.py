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
#   Class name: PlayAudioMenu.py
#   Description: This class creates a custom widget with the Play Audio Menu elements and layout.
# *************************************************************************************************************

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from model.AudioController import AudioController
from model.AudioStatus import AudioStatus
from ..widgets.CustomLabel import CustomLabel
from ..widgets.buttons.Button_Back_PAM import Button_Back_PAM
from ..widgets.buttons.Button_Play_PAM import Button_Play_PAM
from ..widgets.buttons.Button_Pause_PAM import Button_Pause_PAM
from ..widgets.buttons.Button_Next_PAM import Button_Next_PAM
from abc import ABCMeta, abstractmethod


class PlayAudioMenu(QWidget):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        self.updateView(*args)

    def __init__(self, controller, db, parent=None):
        super(PlayAudioMenu, self).__init__(parent)
        self.controller = controller
        self.db = db
        backButton = Button_Back_PAM(self.controller).createButton(344, 96)
        playButton = Button_Play_PAM(self.controller).createButton(50, 50)
        pauseButton = Button_Pause_PAM(self.controller).createButton(50, 50)
        nextButton = Button_Next_PAM(self.controller).createButton(50, 50)
        (self.fileName, self.pathFiles) = self.db.getAudioDB()
        path = self.pathFiles[self.db.getSelection()]
        audioController = AudioController()
        audioObject = audioController.getAudioObject()
        self.testLabel = CustomLabel().createLabel(path, Qt.AlignCenter)
        vbox = QVBoxLayout()

        vbox.addStretch()
        vbox.addStretch()
        vbox.addStretch()
        hMenuBox = QHBoxLayout()
        hMenuBox.addStretch()
        if (audioObject.getStatus() == AudioStatus.PAUSED):
            hMenuBox.addWidget(playButton)
        else:
            hMenuBox.addWidget(pauseButton)
        hMenuBox.addWidget(nextButton)
        hMenuBox.addWidget(self.testLabel)
        hMenuBox.addStretch()
        vbox.addLayout(hMenuBox)

        vbox.addStretch()

        hbox = QHBoxLayout()

        hbox.addWidget(backButton)

        hbox.addStretch()

        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def updateView(self, *args):
        self.testLabel.setText(args[0])