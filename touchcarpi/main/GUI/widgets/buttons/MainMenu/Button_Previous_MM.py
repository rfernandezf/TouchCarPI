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
#   Class name: Button_Previous_MM.py
#   Description: Concrete class of the "Previous Track" button from the Main Menu Audio Widget. This class is a
#   factory method of a PicButton.
# *************************************************************************************************************

from PyQt5.QtGui import *
from ....widgets.buttons.PicButton import PicButton
from model.AudioController import AudioController
from model.AudioStatus import AudioStatus

class Button_Previous_MM():
    """
    Concrete class of the "Previous Track" button from the Main Menu Audio Widget.
    """

    def __init__(self):
        """
        Constructor of the Button_Previous_MM Class.
        """

        self.audioController = AudioController()
        self.audioObject = self.audioController.getAudioObject()

    def onClick(self, isLongClick = False):
        """
        OnClick method. Describes the behaviour of the button when is pressed.
        In this case, it switch to the previous song of the list.
        """

        if (self.audioObject.getStatus() != AudioStatus.NOFILE and self.audioController.getPlayingRadio() == False):
            self.audioController.previousTrack()

        if(self.audioObject.getStatus() == AudioStatus.NOFILE and self.audioController.getPlayingRadio() == True):
            if (self.audioController.getGUICoolDown() == False):
                self.audioController.startGUICoolDown(1.1)
                self.audioController.seekDown()

    def createButton(self, sizeX, sizeY):
        """
        This method is a factory of a PicButton object. Creates a button with the described size.

        :param sizeX: X size of the button.
        :param sizeY: Y size of the button.
        :return: Created button object.
        """

        #TODO Cambiar gráfico
        button = PicButton(QPixmap("themes/default/img/previous_pam.png"), QPixmap("themes/default/img/previous_pam_pressed.png"), sizeX, sizeY, "", self.onClick)

        return button