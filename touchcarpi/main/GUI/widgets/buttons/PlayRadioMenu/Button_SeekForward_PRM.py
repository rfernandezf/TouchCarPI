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
#   Class name: Button_SeekForward_PRM.py
#   Description: Concrete class of the "Seek Forward" button from the Play Radio Menu. This class is a
#   factory method of a PicButton.
# *************************************************************************************************************

from PyQt5.QtGui import *
from ..PicButton import PicButton
from model.AudioController import AudioController

class Button_SeekForward_PRM():

    def __init__(self, controller):
        self.controller = controller
        self.audioController = AudioController()

    def onClick(self, isLongClick = False):
        if (self.audioController.getGUICoolDown() == False):
            self.audioController.startGUICoolDown(1.1)
            self.audioController.seekUp()

    def createButton(self, sizeX, sizeY):
        button = PicButton(QPixmap("themes/default/img/seekforward_prm.png"), QPixmap("themes/default/img/seekforward_prm_pressed.png"), sizeX, sizeY, "", self.onClick)

        return button