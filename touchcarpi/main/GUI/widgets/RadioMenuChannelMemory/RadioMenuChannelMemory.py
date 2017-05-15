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
#   Class name: RadioMenuChannelMemory.py
#   Description: This class provides a customized widget for control the memory banks of the radio channels
#   in the radio menu.
# *************************************************************************************************************

from abc import ABCMeta, abstractmethod
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from DB.RAM_DB import RAM_DB
from ..CustomLabel import CustomLabel
from ..buttons.PlayRadioMenu.Button_Memory_PRM import Button_Memory_PRM

class RadioMenuChannelMemory (QWidget):
    """
    This class provides a customized widget for control the memory banks of the radio channels.
    """

    __metaclass__ = ABCMeta

    def __init__ (self, parent = None):
        """
        Constructor of the RadioMenuChannelMemory class.
        """

        super(RadioMenuChannelMemory, self).__init__(parent)

        self.db = RAM_DB()
        radioChannels = self.db.getRadioChannels()

        memoryButtons = []
        self.labelsMemoryButtons = []
        for i in range(0, 9):
            memoryButtons.append(Button_Memory_PRM(i).createButton(60, 60))

        for i in range(0, 9):
            if (radioChannels[i] == None):
                memoryButtonLabel = "Vacío"
            else:
                memoryButtonLabel = radioChannels[i][1]

            self.labelsMemoryButtons.append(CustomLabel().createLabel(memoryButtonLabel, Qt.AlignCenter, 7))


        hButtonBarBox = QHBoxLayout()

        hButtonBarBox.addStretch()

        for i in range(0, len(memoryButtons)):
            vButtonBox = QVBoxLayout()
            hMemoryButtonBox = QHBoxLayout()

            hMemoryButtonBox.addStretch()
            hMemoryButtonBox.addWidget(memoryButtons[i])
            hMemoryButtonBox.addStretch()
            vButtonBox.addLayout(hMemoryButtonBox)

            hMemoryLabelBox = QHBoxLayout()
            hMemoryLabelBox.addStretch()
            hMemoryLabelBox.addWidget(self.labelsMemoryButtons[i])
            hMemoryLabelBox.addStretch()
            vButtonBox.addLayout(hMemoryLabelBox)

            hButtonBarBox.addLayout(vButtonBox)
            hButtonBarBox.addStretch()

        self.setLayout(hButtonBarBox)

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

        if (args[0] == "UpdateRadioChannelData"):
            radioChannels = self.db.getRadioChannels()
            for i in range(0, len(self.labelsMemoryButtons)):
                self.labelsMemoryButtons[i].setText(radioChannels[i][1])