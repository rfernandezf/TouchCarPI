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
#   Class name: Button_Next_MM.py
#   Description: Concrete class of the "Next" button from the Main Menu Audio Widget. This class is a
#   factory method of a PicButton.
# *************************************************************************************************************

from PyQt5.QtGui import *
from ..PicButton import PicButton
from model.AudioController import AudioController
from model.AudioStatus import AudioStatus

class Button_Next_MM():
    """
    Concrete class of the "Next" button from the Main Menu Audio Widget.
    """

    def __init__(self):
        """
        Constructor of the Button_Next_MM Class.
        """

        self.audioController = AudioController()
        self.audioObject = self.audioController.getAudioObject()

    def onClick(self, isLongClick = False):
        """
        OnClick method. Describes the behaviour of the button when is pressed.
        In this case, it switch to the next song of the list.
        """

        if (self.audioObject.getStatus() != AudioStatus.NOFILE and self.audioController.getPlayingRadio() == False):
            self.audioController.nextTrack()

        if(self.audioObject.getStatus() == AudioStatus.NOFILE and self.audioController.getPlayingRadio() == True):
            if (self.audioController.getGUICoolDown() == False):
                self.audioController.startGUICoolDown(1.1)
                self.audioController.seekUp()

    def createButton(self, sizeX, sizeY):
        """
        This method is a factory of a PicButton object. Creates a button with the described size.

        :param sizeX: X size of the button.
        :param sizeY: Y size of the button.
        :return: Created button object.
        """

        button = PicButton(QPixmap("themes/default/img/next_pam.png"), QPixmap("themes/default/img/next_pam_pressed.png"), sizeX, sizeY, "", self.onClick)

        return button