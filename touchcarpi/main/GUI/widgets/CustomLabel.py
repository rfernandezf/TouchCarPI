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
#   Class name: CustomLabel.py
#   Description: This class creates a custom text label.
# *************************************************************************************************************

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CustomLabel():
    """
    This class creates a custom text label.
    """

    def createLabel(self, text, align, size = 13, rcolor = 255, gcolor = 255, bcolor = 255):
        """
        Factory method of the label.

        :param text: Text of the label.
        :param align: Align of the label.
        :param size: Size of the font.
        :param rcolor: R color of the text in RGB.
        :param gcolor: G color of the text in RGB.
        :param bcolor: B color of the text in RGB.
        :return: Label object.
        """

        label = QLabel()
        label.setText(text)
        label.setAttribute(Qt.WA_TransparentForMouseEvents)
        label.setAlignment(align)
        font = QFont('Myriada', size)
        font.setBold(True)
        label.setStyleSheet("color: rgb(" + str(rcolor) + ", " + str(gcolor) + ", " + str(bcolor) + ");")
        label.setFont(font)

        return label