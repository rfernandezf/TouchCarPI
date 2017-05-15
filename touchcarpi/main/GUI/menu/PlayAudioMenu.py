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

from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DB.RAM_DB import RAM_DB
from model.AudioController import AudioController
from model.AudioStatus import AudioStatus
from util.UtilityFunctions import getArtworkPath

from ..widgets.buttons.PlayAudioMenu.Button_Next_PAM import Button_Next_PAM
from ..widgets.CustomLabel import CustomLabel
from ..widgets.TimeSlider import TimeSlider
from ..widgets.buttons.PlayAudioMenu.Button_Back_PAM import Button_Back_PAM
from ..widgets.buttons.PlayAudioMenu.Button_Pause_PAM import Button_Pause_PAM
from ..widgets.buttons.PlayAudioMenu.Button_Play_PAM import Button_Play_PAM
from ..widgets.buttons.PlayAudioMenu.Button_Previous_PAM import Button_Previous_PAM


class PlayAudioMenu(QWidget):
    """
    This class creates a custom widget with the Play Audio Menu elements and layout.
    """

    __metaclass__ = ABCMeta

    def __init__(self, controller, parent=None):
        """
        Constructor of the PlayAudioMenu class.

        :param controller: GUIController object.
        """

        super(PlayAudioMenu, self).__init__(parent)

        self.controller = controller
        self.db = RAM_DB()

        backButton = Button_Back_PAM(self.controller).createButton(269, 100)
        self.playButton = Button_Play_PAM(self.controller).createButton(60, 60)
        self.pauseButton = Button_Pause_PAM(self.controller).createButton(60, 60)
        nextButton = Button_Next_PAM(self.controller).createButton(60, 60)
        previousButton = Button_Previous_PAM(self.controller).createButton(60, 60)

        (self.fileName, self.pathFiles, self.metaDataList) = self.db.getAudioDB()
        path = self.pathFiles[self.db.getSelection()]

        audioController = AudioController()
        self.audioObject = audioController.getAudioObject()

        self.textLabel = CustomLabel().createLabel(path, Qt.AlignCenter)
        self.actualTimeLabel = CustomLabel().createLabel("00:00", Qt.AlignCenter)
        self.totalTimeLabel = CustomLabel().createLabel("00:00", Qt.AlignCenter)
        self.timeSlider = TimeSlider(0, 100, 0, self.sliderValueChangedByUser)

        verticalBoxLayout = QVBoxLayout()
        hRepTimeBox = QHBoxLayout()
        hRepButtonsBox = QHBoxLayout()
        hImageBox = QHBoxLayout()
        hButtonsMenuBox = QHBoxLayout()

        verticalBoxLayout.setContentsMargins(0, 0, 0, 0)
        verticalBoxLayout.addStretch()

        verticalBoxLayout.addStretch()
        verticalBoxLayout.addWidget(self.textLabel)
        verticalBoxLayout.addStretch()

        hImageBox.addStretch()
        self.imgQLabel = QLabel()
        self.imgQLabel.setMaximumHeight(150)
        self.imgQLabel.setMaximumWidth(150)
        self.imgQLabel.setPixmap(QPixmap(getArtworkPath(self.metaDataList[self.db.getSelection()])).scaled(150, 150))
        hImageBox.addWidget(self.imgQLabel)
        hImageBox.addStretch()
        verticalBoxLayout.addLayout(hImageBox)

        verticalBoxLayout.addStretch()

        hRepTimeBox.addWidget(self.actualTimeLabel)
        hRepTimeBox.addStretch()
        hRepTimeBox.addWidget(self.totalTimeLabel)
        verticalBoxLayout.addLayout(hRepTimeBox)
        verticalBoxLayout.addWidget(self.timeSlider)
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
        verticalBoxLayout.addStretch()

        hButtonsMenuBox.addWidget(backButton)
        hButtonsMenuBox.addStretch()
        verticalBoxLayout.addLayout(hButtonsMenuBox)

        self.setLayout(verticalBoxLayout)

    def sliderValueChangedByUser(self):
        """
        Method when the slider notifies a change in his value made by the user.
        """

        self.audioObject.changeAudioSecond(self.timeSlider.getValue())

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

            self.textLabel.setText(titleText)
            self.totalTimeLabel.setText(strMinutes + ":" + strSeconds)
            self.timeSlider.setMaximum(arg2[16])
            self.imgQLabel.setPixmap(QPixmap(getArtworkPath(self.metaDataList[self.db.getSelection()])).scaled(150, 150))
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