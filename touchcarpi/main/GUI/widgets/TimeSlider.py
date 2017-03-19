from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TimeSlider(QWidget):
    def __init__(self, parent=None):
        super(TimeSlider, self).__init__(parent)

        layout = QVBoxLayout()

        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(0)
        self.sl.setMaximum(100)
        self.sl.setValue(20)


        layout.addWidget(self.sl)
        self.sl.valueChanged.connect(self.valuechange)
        self.setLayout(layout)

    def valuechange(self):
        size = self.sl.value()
        print("He cambiado loko")