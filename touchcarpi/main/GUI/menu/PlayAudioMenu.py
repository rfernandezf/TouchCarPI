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

from model.AudioFile import AudioFile
from ..widgets.CustomLabel import CustomLabel
from ..widgets.buttons.Button_Back_PAM import Button_Back_PAM


class PlayAudioMenu(QWidget):
    def __init__(self, controller, db, parent=None):
        super(PlayAudioMenu, self).__init__(parent)
        self.controller = controller
        self.db = db
        backButton = Button_Back_PAM(self.controller).createButton(344, 96)

        (fileName, pathFiles) = self.db.getAudioDB()
        path = pathFiles[self.db.getSelection()]
        audioObject = AudioFile()
        audioObject.playAudio(path)
        testLabel = CustomLabel().createLabel(path, Qt.AlignCenter)
        vbox = QVBoxLayout()

        vbox.addStretch()
        vbox.addStretch()
        vbox.addStretch()
        hMenuBox = QHBoxLayout()
        hMenuBox.addStretch()
        hMenuBox.addWidget(testLabel)
        hMenuBox.addStretch()
        vbox.addLayout(hMenuBox)

        vbox.addStretch()

        hbox = QHBoxLayout()

        hbox.addWidget(backButton)

        hbox.addStretch()

        vbox.addLayout(hbox)

        self.setLayout(vbox)