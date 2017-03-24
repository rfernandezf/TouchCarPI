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
#   Class name: SelectAudioListWidget.py
#   Description: Class that creates a customiced QListWidget used in the SelectAudioMenu that displays a list
#   of songs and allows you to choose one to be reproduced.
# *************************************************************************************************************


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .CustomListWidget import CustomListItemWidget
from model.AudioController import AudioController
from DB.RAM_DB import RAM_DB
from util.UtilityFunctions import getBandName

class SelectAudioListWidget(QListWidget):

    def __init__(self, controller, parent = None):
        super(SelectAudioListWidget, self).__init__(parent)
        self.db = RAM_DB()
        self.controller = controller

        # Pasar esto a una clase A PARTE
        self.itemClicked.connect(self.item_click)
        self.setMinimumSize(QSize(600, 300))
        (fileName, pathFiles, self.metaDataList) = self.db.getAudioDB()
        self.itemsDict = {}

        for i in range(0, len(fileName)):

            customListItemWidget = CustomListItemWidget()
            customListItemWidget.setTextUp(self.metaDataList[i][0])
            customListItemWidget.setTextDown(getBandName(self.metaDataList[i][1]))
            customListItemWidget.setIcon("themes/default/img/headphones.png")
            customListItemWidget.setPath(pathFiles[i])

            item = QListWidgetItem()
            item.setSizeHint(customListItemWidget.sizeHint())

            self.addItem(item)
            self.setItemWidget(item, customListItemWidget)
            self.itemsDict[str(item)] = customListItemWidget


    def item_click(self, item):
        #Set the track selected for playing it
        self.db.setSelection(self.db.getIndexByPath(self.itemsDict[str(item)].getPath()))
        #Switch to PlayAudioMenu
        self.controller.changeToMenu("PlayAudioMenu")
        #Call to audioController for load the new audio file...
        audioController = AudioController()
        audioController.loadAudio()