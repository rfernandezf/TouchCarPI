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
#   Class name: SelectAudioMenu.py
#   Description: This class creates a custom widget with the Select Audio Menu elements and layout.
# *************************************************************************************************************
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ..widgets.buttons.Button_Back_SAM import Button_Back_SAM
from ..widgets.buttons.Button_Resume_SAM import Button_Resume_SAM
from DB.RAM_DB import RAM_DB
from model.AudioStatus import AudioStatus
from model.AudioController import AudioController
from ..widgets.SelectAudioListWidget import SelectAudioListWidget
from util.UtilityFunctions import getBandName

from abc import ABCMeta, abstractmethod


class SelectAudioMenu(QWidget):
    __metaclass__ = ABCMeta

    def __init__(self, controller, db, parent=None):
        super(SelectAudioMenu, self).__init__(parent)
        self.controller = controller
        self.db = RAM_DB()
        (fileName, pathFiles, self.metaDataList) = self.db.getAudioDB()
        self.audioController = AudioController()
        backButton = Button_Back_SAM(self.controller).createButton(344, 96)
        self.resumeButton = Button_Resume_SAM(self.controller).createButton(344, 96)

        selectAudioListWidget = SelectAudioListWidget(self.controller)


        vbox = QVBoxLayout()

        vbox.addStretch()
        vbox.addStretch()
        vbox.addStretch()
        hMenuBox = QHBoxLayout()
        hMenuBox.addStretch()
        hMenuBox.addStretch()
        hMenuBox.addWidget(selectAudioListWidget)
        hMenuBox.addStretch()
        vbox.addLayout(hMenuBox)

        vbox.addStretch()

        hbox = QHBoxLayout()

        hbox.addWidget(backButton)

        hbox.addStretch()

        hbox.addWidget(self.resumeButton)
        if self.audioController.getStatus() == AudioStatus.NOFILE:
            self.resumeButton.hide()
        else:
            self.resumeButton.setText("Reproduciendo: " + getBandName(self.metaDataList[self.db.getSelection()][1]))

        vbox.addLayout(hbox)

        self.setLayout(vbox)

    @abstractmethod
    def update(self, *args, **kwargs):
        self.updateView(*args, **kwargs)

    def updateView(self, *args, arg1, arg2):
        if (args[0] == "NewMetaData"):
            self.resumeButton.setText("Reproduciendo: " + getBandName(self.metaDataList[self.db.getSelection()][1]))