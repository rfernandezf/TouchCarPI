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
#   Class name: SelectAudioMenu.py
#   Description: This class creates a custom widget with the Select Audio Menu elements and layout.
# *************************************************************************************************************
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ..widgets.buttons.Button_Back_SAM import Button_Back_SAM
from ..widgets.CustomListWidget import CustomListItemWidget
from model.AudioController import AudioController


class SelectAudioMenu(QWidget):
    def __init__(self, controller, db, parent=None):
        super(SelectAudioMenu, self).__init__(parent)
        self.controller = controller
        self.db = db
        backButton = Button_Back_SAM(self.controller).createButton(344, 96)

        #Pasar esto a una clase A PARTE
        selectAudioListWidget = QListWidget()
        selectAudioListWidget.itemClicked.connect(self.item_click)
        selectAudioListWidget.setMinimumSize(QSize(600, 300))
        (fileName, pathFiles, self.metaDataList) = self.db.getAudioDB()
        self.itemsDict = {}

        for i in range(0, len(fileName)):

            customListItemWidget = CustomListItemWidget()
            customListItemWidget.setTextUp(self.metaDataList[i][0])
            if self.metaDataList[i][1] == None:
                textDown = "Artista desconocido"
            else:
                textDown = self.metaDataList[i][1]
            customListItemWidget.setTextDown(textDown)
            customListItemWidget.setIcon("themes/default/img/headphones.png")
            customListItemWidget.setPath(pathFiles[i])

            item = QListWidgetItem()
            item.setSizeHint(customListItemWidget.sizeHint())

            selectAudioListWidget.addItem(item)
            selectAudioListWidget.setItemWidget(item, customListItemWidget)
            self.itemsDict[str(item)] = customListItemWidget



        vbox = QVBoxLayout()

        vbox.addStretch()
        vbox.addStretch()
        vbox.addStretch()
        hMenuBox = QHBoxLayout()
        hMenuBox.addStretch()
        hMenuBox.addStretch()
        hMenuBox.addWidget(selectAudioListWidget)
        hMenuBox.addStretch()
        vbox.addLayout(hMenuBox)

        vbox.addStretch()

        hbox = QHBoxLayout()

        hbox.addWidget(backButton)

        hbox.addStretch()

        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def item_click(self, item):
        print(str(self.itemsDict[str(item)].getPath()))
        #Set the track selected for playing it
        self.db.setSelection(self.db.getIndexByPath(self.itemsDict[str(item)].getPath()))
        #Switch to PlayAudioMenu
        self.controller.changeToMenu("PlayAudioMenu")
        #Call to audioController for load the new audio file...
        audioController = AudioController()
        audioController.loadAudio()

