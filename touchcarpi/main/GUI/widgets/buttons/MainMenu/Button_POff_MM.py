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
#   Class name: Button_POff_MM.py
#   Description: Concrete class of the "Power Off" button from the Main Menu. This class is a
#   factory method of a PicButton.
# *************************************************************************************************************

from PyQt5.QtGui import *
from ..PicButton import PicButton

from model.AudioController import AudioController

class Button_POff_MM():
    """
    Concrete class of the "Power Off" button from the Main Menu.
    """

    def __init__(self):
        """
        Constructor of the Button_POff_MM Class.
        """

        self.audioController = AudioController()

    def onClick(self, isLongClick = False):
        """
        OnClick method. Describes the behaviour of the button when is pressed.
        In this case, it ends the application.
        """
        self.audioController.stopRadio()
        exit(0)

    def createButton(self, sizeX, sizeY):
        """
        This method is a factory of a PicButton object. Creates a button with the described size.

        :param sizeX: X size of the button.
        :param sizeY: Y size of the button.
        :return: Created button object.
        """

        button = PicButton(QPixmap("themes/default/img/MenuButton_R.png"), QPixmap("themes/default/img/MenuButton_R_Pressed.png"), sizeX, sizeY, "Apagar", self.onClick)

        return button