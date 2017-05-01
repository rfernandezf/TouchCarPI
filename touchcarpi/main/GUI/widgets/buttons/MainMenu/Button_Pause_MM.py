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
#   Class name: Button_Pause_MM.py
#   Description: Concrete class of the "Pause" button from the Main Menu Audio Widget. This class is a
#   factory method of a PicButton.
# *************************************************************************************************************

from PyQt5.QtGui import *
from ..PicButton import PicButton
from model.AudioController import AudioController
from model.AudioStatus import AudioStatus

class Button_Pause_MM():

    def __init__(self):
        self.audioController = AudioController()
        self.audioObject = self.audioController.getAudioObject()

    def onClick(self):
        # TODO Añadir funcionalidad radio
        if (self.audioObject.getStatus() != AudioStatus.NOFILE):
            self.audioController.pause()

    def createButton(self, sizeX, sizeY):
        #TODO Cambiar gráficos
        button = PicButton(QPixmap("themes/default/img/pause_pam.png"), QPixmap("themes/default/img/pause_pam_pressed.png"), sizeX, sizeY, "", self.onClick)

        return button