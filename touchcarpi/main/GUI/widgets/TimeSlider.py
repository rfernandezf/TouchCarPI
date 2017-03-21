from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TimeSlider(QWidget):
    def __init__(self, minSize, maxSize, startOn, parent=None):
        super(TimeSlider, self).__init__(parent)

        self.minSize = minSize
        self.maxSize = maxSize
        self.slideValue = startOn

        layout = QVBoxLayout()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(self.minSize)
        self.slider.setMaximum(self.maxSize)
        self.slider.setValue(self.slideValue)


        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.valuechange)
        self.setLayout(layout)

    def setMaximum(self, maxSize):
        self.maxSize = maxSize
        self.slider.setMaximum(self.maxSize)

    def setValue(self, value):
        self.slideValue = value
        self.slider.setValue(self.slideValue)

    def valuechange(self):
        self.slideValue = self.slider.value()
        print("He cambiado loko")