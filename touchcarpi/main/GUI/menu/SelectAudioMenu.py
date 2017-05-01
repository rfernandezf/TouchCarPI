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

from abc import ABCMeta, abstractmethod

from DB.RAM_DB import RAM_DB
from PyQt5.QtWidgets import *
from model.AudioController import AudioController
from model.AudioStatus import AudioStatus
from util.UtilityFunctions import getBandName


from ..widgets.buttons.SelectAudioMenu.Button_Resume_SAM import Button_Resume_SAM
from ..widgets.ResumeAudioWidget_SAM import ResumeAudioWidget_SAM
from ..widgets.SelectAudioListWidget import SelectAudioListWidget
from ..widgets.buttons.SelectAudioMenu.Button_Back_SAM import Button_Back_SAM


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
        self.resumeAudioWidget = ResumeAudioWidget_SAM(self.controller)


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

        """
        hMenuBox2 = QHBoxLayout()
        hMenuBox2.addStretch()
        hMenuBox2.addStretch()

        hMenuBox2.addWidget(self.resumeAudioWidget)
        if self.audioController.getStatus() == AudioStatus.NOFILE:
            self.resumeAudioWidget.hide()
        else:
            self.resumeAudioWidget.setTextUp(self.metaDataList[self.db.getSelection()][0])
            self.resumeAudioWidget.setTextDown(getBandName(self.metaDataList[self.db.getSelection()][1]))

        hMenuBox2.addStretch()

        vbox.addLayout(hMenuBox2)
        """

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
            """
            self.resumeAudioWidget.setTextUp(self.metaDataList[self.db.getSelection()][0])
            self.resumeAudioWidget.setTextDown(getBandName(self.metaDataList[self.db.getSelection()][1]))
            """
            self.resumeButton.setText("Reproduciendo: " + getBandName(self.metaDataList[self.db.getSelection()][1]))