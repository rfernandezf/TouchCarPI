from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TimeSlider(QWidget):
    def __init__(self, minSize, maxSize, startOn, sliderValueChangedByUser, parent=None):
        super(TimeSlider, self).__init__(parent)

        self.minSize = minSize
        self.maxSize = maxSize
        self.slideValue = startOn
        self.sliderValueChangedByUser = sliderValueChangedByUser
        """
        0 = Normal
        1 = The user is moving the slider
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
        self.maxSize = maxSize
        self.slider.setMaximum(self.maxSize)

    def setValue(self, value):
        if(self.sliderTouched == False):
            self.slideValue = value
            self.slider.setValue(self.slideValue)

    def getValue(self):
        return self.slideValue

    def sliderPressed(self):
        self.sliderTouched = True

    def sliderReleased(self):
        self.slideValue = self.slider.value()
        self.sliderValueChangedByUser()
        self.sliderTouched = False
