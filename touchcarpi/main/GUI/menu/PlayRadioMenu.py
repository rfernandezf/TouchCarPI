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
#   Class name: PlayRadioMenu.py
#   Description: This class creates a custom widget with the Play Radio Menu elements and layout.
# *************************************************************************************************************

from abc import ABCMeta, abstractmethod

from DB.RAM_DB import RAM_DB
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from model.AudioController import AudioController

from ..widgets.RadioMenu.RadioMenuChannelMemory.RadioMenuChannelMemory import RadioMenuChannelMemory
from ..widgets.CustomLabel import CustomLabel
from ..widgets.buttons.PlayRadioMenu.Button_Back_PRM import Button_Back_PRM
from ..widgets.buttons.PlayRadioMenu.Button_Downfreq_PRM import Button_Downfreq_PRM
from ..widgets.buttons.PlayRadioMenu.Button_SeekBack_PRM import Button_SeekBack_PRM
from ..widgets.buttons.PlayRadioMenu.Button_SeekForward_PRM import Button_SeekForward_PRM
from ..widgets.buttons.PlayRadioMenu.Button_Upfreq_PRM import Button_Upfreq_PRM


class PlayRadioMenu(QWidget):
    """
    This class creates a custom widget with the Play Radio Menu elements and layout.
    """

    __metaclass__ = ABCMeta

    def __init__(self, controller, parent=None):
        """
        Constructor of the PlayRadioMenu class.

        :param controller: GUIController object.
        """

        super(PlayRadioMenu, self).__init__(parent)

        self.controller = controller
        audioController = AudioController()
        self.db = RAM_DB()
        radioMenuChannelMemoryWidget = RadioMenuChannelMemory()
        # Observer
        audioController.register(radioMenuChannelMemoryWidget)

        self.backButton = Button_Back_PRM(self.controller).createButton(269, 100)
        self.upFreqButton = Button_Upfreq_PRM(self.controller).createButton(60, 60)
        self.downFreqButton = Button_Downfreq_PRM(self.controller).createButton(60, 60)
        self.seekBackButton = Button_SeekBack_PRM(self.controller).createButton(60, 60)
        self.seekForwardButton = Button_SeekForward_PRM(self.controller).createButton(60, 60)

        if(audioController.getPlayingRadio() == False or audioController.getGUICoolDown() == True):
            self.upFreqButton.setOppacity(0.3)
            self.downFreqButton.setOppacity(0.3)
            self.seekBackButton.setOppacity(0.3)
            self.seekForwardButton.setOppacity(0.3)

        audioController.initRadio()

        self.freqLabel = CustomLabel().createLabel(str(audioController.getCurrentFMFrequency()) + " FM", Qt.AlignCenter, 30)

        verticalBoxLayout = QVBoxLayout()
        verticalBoxLayout.setContentsMargins(0, 0, 0, 0)

        verticalBoxLayout.addStretch()
        verticalBoxLayout.addStretch()
        verticalBoxLayout.addWidget(self.freqLabel)
        verticalBoxLayout.addStretch()

        hMenuBox = QHBoxLayout()
        hMenuBox.addStretch()
        hMenuBox.addWidget(self.seekBackButton)
        hMenuBox.addStretch()
        hMenuBox.addWidget(self.downFreqButton)
        hMenuBox.addStretch()
        hMenuBox.addWidget(self.upFreqButton)
        hMenuBox.addStretch()
        hMenuBox.addWidget(self.seekForwardButton)
        hMenuBox.addStretch()
        verticalBoxLayout.addLayout(hMenuBox)

        verticalBoxLayout.addStretch()

        verticalBoxLayout.addWidget(radioMenuChannelMemoryWidget)

        verticalBoxLayout.addStretch()

        hbox = QHBoxLayout()

        hbox.addWidget(self.backButton)
        hbox.addStretch()

        verticalBoxLayout.addLayout(hbox)

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

        if (args[0] == "UpdateCurrentFMFrequency"):
            self.freqLabel.setText(str(arg1) + " FM")

        elif (args[0] == "CoolDownStarted"):
            self.upFreqButton.setOppacity(0.3)
            self.downFreqButton.setOppacity(0.3)
            self.seekBackButton.setOppacity(0.3)
            self.seekForwardButton.setOppacity(0.3)

        elif (args[0] == "CoolDownEnded"):
            self.upFreqButton.setOppacity(1)
            self.downFreqButton.setOppacity(1)
            self.seekBackButton.setOppacity(1)
            self.seekForwardButton.setOppacity(1)