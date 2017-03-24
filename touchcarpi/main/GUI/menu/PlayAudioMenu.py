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
from ..widgets.TimeSlider import TimeSlider
from ..widgets.CustomLabel import CustomLabel
from ..widgets.buttons.Button_Back_PAM import Button_Back_PAM
from ..widgets.buttons.Button_Play_PAM import Button_Play_PAM
from ..widgets.buttons.Button_Pause_PAM import Button_Pause_PAM
from ..widgets.buttons.Button_Next_PAM import Button_Next_PAM
from ..widgets.buttons.Button_Previous_PAM import Button_Previous_PAM
from abc import ABCMeta, abstractmethod


class PlayAudioMenu(QWidget):
    __metaclass__ = ABCMeta

    def __init__(self, controller, db, parent=None):
        super(PlayAudioMenu, self).__init__(parent)
        self.controller = controller
        self.db = db
        backButton = Button_Back_PAM(self.controller).createButton(344, 96)
        self.playButton = Button_Play_PAM(self.controller).createButton(50, 50)
        self.pauseButton = Button_Pause_PAM(self.controller).createButton(50, 50)
        nextButton = Button_Next_PAM(self.controller).createButton(50, 50)
        previousButton = Button_Previous_PAM(self.controller).createButton(50, 50)
        (self.fileName, self.pathFiles, self.metaDataList) = self.db.getAudioDB()
        path = self.pathFiles[self.db.getSelection()]
        audioController = AudioController()
        self.audioObject = audioController.getAudioObject()
        self.testLabel = CustomLabel().createLabel(path, Qt.AlignCenter)
        self.actualTimeLabel = CustomLabel().createLabel("00:00", Qt.AlignCenter)
        self.totalTimeLabel = CustomLabel().createLabel("00:00", Qt.AlignCenter)

        self.timeSlider = TimeSlider(0, 100, 0, self.sliderValueChangedByUser)

        vbox = QVBoxLayout()

        vbox.addStretch()
        vbox.addStretch()
        vbox.addWidget(self.testLabel)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.actualTimeLabel)
        hbox2.addStretch()
        hbox2.addWidget(self.totalTimeLabel)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.timeSlider)
        vbox.addStretch()
        hMenuBox = QHBoxLayout()
        hMenuBox.addStretch()
        if (self.audioObject.getStatus() == AudioStatus.PAUSED):
            self.pauseButton.hide()
        else:
            self.playButton.hide()
        hMenuBox.addWidget(previousButton)
        hMenuBox.addStretch()
        hMenuBox.addWidget(self.playButton)
        hMenuBox.addWidget(self.pauseButton)
        hMenuBox.addStretch()
        hMenuBox.addWidget(nextButton)
        hMenuBox.addStretch()
        vbox.addLayout(hMenuBox)

        vbox.addStretch()

        hbox = QHBoxLayout()

        hbox.addWidget(backButton)

        hbox.addStretch()

        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def sliderValueChangedByUser(self):
        self.audioObject.changeAudioSecond(self.timeSlider.getValue())

    @abstractmethod
    def update(self, *args, **kwargs):
        self.updateView(*args, **kwargs)

    def updateView(self, *args, arg1, arg2):
        if(args[0] == "NewMetaData"):
            minutes = round((arg2[16] // 1000.0) // 60.0)
            seconds = round((arg2[16] // 1000.0) %60.0)

            if minutes < 10:
                strMinutes = "0" + str(minutes)
            else:
                strMinutes = str(minutes)
            if seconds < 10:
                strSeconds = "0" + str(seconds)
            else:
                strSeconds = str(seconds)

            if arg2[1] == None:
                titleText = "Artista desconocido" + " - " + arg2[0]
            else:
                titleText = arg2[1] + " - " + arg2[0]

            self.testLabel.setText(titleText)
            self.totalTimeLabel.setText(strMinutes + ":" + strSeconds)
            self.timeSlider.setMaximum(arg2[16])
            self.playButton.hide()
            self.pauseButton.show()

        elif (args[0] == "AudioPaused"):
            self.playButton.show()
            self.pauseButton.hide()

        elif (args[0] == "AudioResumed"):
            self.playButton.hide()
            self.pauseButton.show()

        elif (args[0] == "UpdateReproductionSecond"):
            minutes = round((arg1 // 1000) // 60)
            seconds = round((arg1 // 1000)) %60

            if minutes < 10:
                strMinutes = "0" + str(minutes)
            else:
                strMinutes = str(minutes)
            if seconds < 10:
                strSeconds = "0" + str(seconds)
            else:
                strSeconds = str(seconds)

            self.actualTimeLabel.setText(strMinutes + ":" + strSeconds)
            self.timeSlider.setValue(arg1)