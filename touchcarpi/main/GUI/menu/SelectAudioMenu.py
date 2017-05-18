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

from PyQt5.QtWidgets import *

from model.AudioController import AudioController
from model.AudioStatus import AudioStatus
from DB.RAM_DB import RAM_DB
from ..widgets.buttons.SelectAudioMenu.Button_Resume_SAM import Button_Resume_SAM
from ..widgets.SelectAudioListWidget import SelectAudioListWidget
from ..widgets.buttons.SelectAudioMenu.Button_Back_SAM import Button_Back_SAM


class SelectAudioMenu(QWidget):
    """
    This class creates a custom widget with the Select Audio Menu elements and layout.
    """

    def __init__(self, controller, parent=None):
        """
        Constructor of the SelectAudioMenu class.

        :param controller: GUIController object.
        """

        super(SelectAudioMenu, self).__init__(parent)

        self.controller = controller
        self.db = RAM_DB()
        (fileName, pathFiles, self.metaDataList) = self.db.getAudioDB()
        self.audioController = AudioController()

        backButton = Button_Back_SAM(self.controller).createButton(269, 100)
        self.resumeButton = Button_Resume_SAM(self.controller).createButton(269, 100)
        selectAudioListWidget = SelectAudioListWidget(self.controller)

        verticalBoxLayout = QVBoxLayout()
        hSelectAudioListBox = QHBoxLayout()
        hButtonsMenuBox = QHBoxLayout()

        verticalBoxLayout.setContentsMargins(0, 0, 0, 0)
        verticalBoxLayout.addStretch()

        hSelectAudioListBox.addStretch()
        hSelectAudioListBox.addWidget(selectAudioListWidget)
        hSelectAudioListBox.addStretch()

        verticalBoxLayout.addLayout(hSelectAudioListBox)

        verticalBoxLayout.addStretch()

        hButtonsMenuBox.addWidget(backButton)
        hButtonsMenuBox.addStretch()
        hButtonsMenuBox.addWidget(self.resumeButton)

        if self.audioController.getStatus() == AudioStatus.NOFILE:
            self.resumeButton.hide()

        verticalBoxLayout.addLayout(hButtonsMenuBox)

        self.setLayout(verticalBoxLayout)
