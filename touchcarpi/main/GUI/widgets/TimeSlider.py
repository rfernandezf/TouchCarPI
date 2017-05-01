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
#   Class name: TimeSlider.py
#   Description: Class that creates a custom slider for view the reproduction seconds.
# *************************************************************************************************************

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TimeSlider(QWidget):
    """
    Class that creates a custom slider for view the reproduction seconds.
    """

    def __init__(self, minSize, maxSize, startOn, sliderValueChangedByUser, parent=None):
        """
        Constructor of the custom slider.

        :param minSize: Min size of the slider.
        :param maxSize: Max size (length) of the slider.
        :param startOn: Value where the slider starts.
        :param sliderValueChangedByUser: Method with the behaviour when the user changes the slider value.
        """

        super(TimeSlider, self).__init__(parent)

        self.minSize = minSize
        self.maxSize = maxSize
        self.slideValue = startOn
        self.sliderValueChangedByUser = sliderValueChangedByUser

        """
        False = Normal
        True = The user is moving the slider, the position of the slider
        shouldn't be updated while the user is moving the slider
        """
        self.sliderTouched = False

        layout = QVBoxLayout()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(self.minSize)
        self.slider.setMaximum(self.maxSize)
        self.slider.setValue(self.slideValue)


        layout.addWidget(self.slider)
        self.slider.sliderPressed.connect(self.sliderPressed)
        self.slider.sliderReleased.connect(self.sliderReleased)
        self.setLayout(layout)

    def setMaximum(self, maxSize):
        """
        Sets the length of the slider.

        :param maxSize: Length of the slider.
        """

        self.maxSize = maxSize
        self.slider.setMaximum(self.maxSize)

    def setValue(self, value):
        """
        Sets the value of the slider.

        :param value: Value of the slider.
        """

        if(self.sliderTouched == False):
            self.slideValue = value
            self.slider.setValue(self.slideValue)

    def getValue(self):
        """
        Returns the current value of the slider.

        :return: Current value of the slider.
        """

        return self.slideValue

    def sliderPressed(self):
        """
        Method called by an event if the slider is pressed.
        """

        self.sliderTouched = True

    def sliderReleased(self):
        """
        Method called by an event if the slider is released.
        """

        self.slideValue = self.slider.value()
        self.sliderValueChangedByUser()
        self.sliderTouched = False
