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
        self.slider.setStyleSheet("""
        QSlider::groove:horizontal {
        border: 1px solid #bbb;
        background: white;
        height: 15px;
        border-radius: 4px;
        }

        QSlider::sub-page:horizontal {
        background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
            stop: 0 #FF7A33, stop: 1 #FFAF33);
        background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
            stop: 0 #FF7A33, stop: 1 #FFAF33);
        border: 1px solid #777;
        height: 15px;
        border-radius: 4px;
        }

        QSlider::add-page:horizontal {
        background: #fff;
        border: 1px solid #777;
        height: 15px;
        border-radius: 4px;
        }

        QSlider::handle:horizontal {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #FF7A33, stop:1 #FFAF33);
        border: 1px solid #777;
        width: 18px;
        margin-top: -2px;
        margin-bottom: -2px;
        border-radius: 4px;
        }

        QSlider::handle:horizontal:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #FF6133, stop:1 #FF8D33);
        border: 1px solid #444;
        border-radius: 4px;
        }

        QSlider::sub-page:horizontal:disabled {
        background: #bbb;
        border-color: #999;
        }

        QSlider::add-page:horizontal:disabled {
        background: #eee;
        border-color: #999;
        }

        QSlider::handle:horizontal:disabled {
        background: #eee;
        border: 1px solid #aaa;
        border-radius: 4px;
        }
        """)

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
