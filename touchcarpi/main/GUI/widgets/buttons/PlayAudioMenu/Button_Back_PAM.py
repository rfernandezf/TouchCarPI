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
#   Class name: Button_Back_PAM.py
#   Description: Concrete class of the "Back" button from the Play Audio Menu. This class is a
#   factory method of a PicButton.
# *************************************************************************************************************

from PyQt5.QtGui import *
from ..PicButton import PicButton
from control.threads.ThreadController import ThreadController

class Button_Back_PAM():
    """
    Concrete class of the "Back" button from the Play Audio Menu.
    """

    def __init__(self, controller):
        """
        Constructor of the Button_Back_PAM Class.

        :param controller: GUIController object.
        """

        self.controller = controller
        self.threadController = ThreadController()

    def onClick(self):
        """
        OnClick method. Describes the behaviour of the button when is pressed.
        In this case, it changes to the previous menu and stops the reproduction status thread.
        """

        reproductionStatusThread = self.threadController.getReproductionStatusThread()
        if reproductionStatusThread != None:
            reproductionStatusThread.stop()
        self.controller.changeToMenu("SelectAudioMenu")

    def createButton(self, sizeX, sizeY):
        """
        This method is a factory of a PicButton object. Creates a button with the described size.

        :param sizeX: X size of the button.
        :param sizeY: Y size of the button.
        :return: Created button object.
        """

        button = PicButton(QPixmap("themes/default/img/options_mm.png"), QPixmap("themes/default/img/options_mm_pressed.png"), sizeX, sizeY, "Atrás", self.onClick)

        return button