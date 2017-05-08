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
#   Description: This class creates a custom widget with the Select Audio Menu elements and layout.
# *************************************************************************************************************
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ..widgets.buttons.PlayRadioMenu.Button_Back_PRM import Button_Back_PRM
from ..widgets.buttons.PlayRadioMenu.Button_Upfreq_PRM import Button_Upfreq_PRM
from ..widgets.buttons.PlayRadioMenu.Button_Downfreq_PRM import Button_Downfreq_PRM
from ..widgets.buttons.PlayRadioMenu.Button_SeekBack_PRM import Button_SeekBack_PRM
from ..widgets.buttons.PlayRadioMenu.Button_SeekForward_PRM import Button_SeekForward_PRM
from ..widgets.buttons.PlayRadioMenu.Button_Memory_PRM import Button_Memory_PRM
from ..widgets.CustomLabel import CustomLabel


class PlayRadioMenu(QWidget):
    """
    This class creates a custom widget with the Select Audio Menu elements and layout.
    """

    def __init__(self, controller, parent=None):
        """
        Constructor of the PlayRadioMenu class.

        :param controller: GUIController object.
        """

        super(PlayRadioMenu, self).__init__(parent)

        self.controller = controller
        backButton = Button_Back_PRM(self.controller).createButton(269, 100)
        freqLabel = CustomLabel().createLabel("89.1", Qt.AlignCenter, 30)
        upFreqButton = Button_Upfreq_PRM(self.controller).createButton(60, 60)
        downFreqButton = Button_Downfreq_PRM(self.controller).createButton(60, 60)
        seekBackButton = Button_SeekBack_PRM(self.controller).createButton(60, 60)
        seekForwardButton = Button_SeekForward_PRM(self.controller).createButton(60, 60)
        memoryButtons = []
        for i in range(0, 9):
            memoryButtons.append(Button_Memory_PRM(self.controller, i).createButton(60, 60))

        verticalBoxLayout = QVBoxLayout()
        verticalBoxLayout.setContentsMargins(0, 0, 0, 0)

        verticalBoxLayout.addStretch()
        verticalBoxLayout.addStretch()
        verticalBoxLayout.addWidget(freqLabel)
        verticalBoxLayout.addStretch()

        hMenuBox = QHBoxLayout()
        hMenuBox.addStretch()
        hMenuBox.addWidget(seekBackButton)
        hMenuBox.addStretch()
        hMenuBox.addWidget(downFreqButton)
        hMenuBox.addStretch()
        hMenuBox.addWidget(upFreqButton)
        hMenuBox.addStretch()
        hMenuBox.addWidget(seekForwardButton)
        hMenuBox.addStretch()
        verticalBoxLayout.addLayout(hMenuBox)

        verticalBoxLayout.addStretch()

        hMemoryButtonsBox = QHBoxLayout()
        hMemoryButtonsBox.addStretch()

        for i in range (0, len(memoryButtons)):
            hMemoryButtonsBox.addWidget(memoryButtons[i])
            hMemoryButtonsBox.addStretch()

        hMemoryButtonsBox.addStretch()
        verticalBoxLayout.addLayout(hMemoryButtonsBox)

        verticalBoxLayout.addStretch()

        hbox = QHBoxLayout()

        hbox.addWidget(backButton)
        hbox.addStretch()

        verticalBoxLayout.addLayout(hbox)

        self.setLayout(verticalBoxLayout)