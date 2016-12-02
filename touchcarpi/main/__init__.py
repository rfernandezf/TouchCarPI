import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QGraphicsView


class ImageView(QGraphicsView):
    def __init__(self, parent=None, origPixmap=None):
        """
        QGraphicsView that will show an image scaled to the current widget size
        using events
        """
        super(ImageView, self).__init__(parent)
        self.origPixmap = origPixmap
        QMetaObject.connectSlotsByName(self)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def resizeEvent(self, event):
        """
        Handle the resize event.
        """
        size = event.size()
        item = self.items()[0]

        # using current pixmap after n-resizes would get really blurry image
        # pixmap = item.pixmap()
        pixmap = self.origPixmap
        pixmap = pixmap.scaled(size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.centerOn(1.0, 1.0)
        item.setPixmap(pixmap)


app = QApplication(sys.argv)

pic = QPixmap('pic.jpg')
grview = ImageView(origPixmap=pic)

scene = QGraphicsScene()
scene.addPixmap(pic)

grview.setScene(scene)
grview.showFullScreen()

sys.exit(app.exec_())