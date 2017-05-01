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
#   Class name: MainMenu.py
#   Description: This class creates a custom widget with the Main Menu elements and layout.
# *************************************************************************************************************

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from model.AudioController import AudioController


from ..widgets.CustomLabel import CustomLabel
from ..widgets.buttons.MainMenu.Button_Music_MM import Button_Music_MM
from ..widgets.buttons.MainMenu.Button_Options_MM import Button_Options_MM
from ..widgets.buttons.MainMenu.Button_Radio_MM import Button_Radio_MM
from ..widgets.buttons.MainMenu.Button_POff_MM import Button_POff_MM
from ..widgets.MainMenuAudioWidget.MainMenuAudioWidget import MainMenuAudioWidget


class MainMenu(QWidget):
    def __init__(self, controller, db, parent=None):
        super(MainMenu, self).__init__(parent)

        audioController = AudioController()
        optionsButton = Button_Options_MM(controller).createButton(344, 96)
        poffButton = Button_POff_MM().createButton(344, 96)
        musicMenuLabel = CustomLabel().createLabel("Música      ", Qt.AlignCenter)
        musicMenuButton = Button_Music_MM(controller).createButton(97, 97)
        radioMenuLabel = CustomLabel().createLabel("Radio  ", Qt.AlignCenter)
        radioMenuButton = Button_Radio_MM(controller).createButton(97, 97)
        mainMenuAudioWidget = MainMenuAudioWidget()
        audioController.register(mainMenuAudioWidget)

        vBox1 = QVBoxLayout()
        hBox1 = QHBoxLayout()
        hBox2 = QHBoxLayout()

        vBox1.addStretch()
        vBox1.addStretch()

        hBox1.addStretch()
        hBox1.addWidget(mainMenuAudioWidget)
        vBox1.addLayout(hBox1)
        vBox1.addStretch()

        hBox2.addStretch()
        hBox2.addWidget(musicMenuButton)
        hBox2.addStretch()
        hBox2.addWidget(radioMenuButton)
        hBox2.addStretch()
        vBox1.addLayout(hBox2)

        hLabelMenuBox = QHBoxLayout()
        hLabelMenuBox.addStretch()
        hLabelMenuBox.addWidget(musicMenuLabel)
        hLabelMenuBox.addStretch()
        hLabelMenuBox.addWidget(radioMenuLabel)
        hLabelMenuBox.addStretch()

        vBox1.addLayout(hLabelMenuBox)
        vBox1.addStretch()
        hbox = QHBoxLayout()

        hbox.addWidget(optionsButton)

        hbox.addStretch()
        hbox.addWidget(poffButton)
        vBox1.addLayout(hbox)

        self.setLayout(vBox1)