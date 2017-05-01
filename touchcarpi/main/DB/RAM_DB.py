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
#   Class name: RAM_DB.py
#   Description: This class creates some list and structures with info for the application. The DB class is
#   a singleton.
# *************************************************************************************************************

import os

from .MetaDataVLC import MetaDataVLC


class RAM_DB:

    class __RAM_DB:
        def __init__(self):
            # List all the files in the desired format (MP3, WAV...)
            self.filesInFolder = []
            self.pathFiles = []
            self.selectionIndex = 0

            for (dirpath, dirnames, filenames) in os.walk("Music"):
                for x in filenames:
                    if x.endswith(".mp3"):
                        self.filesInFolder.append(x)
                        self.pathFiles.append(os.path.join(dirpath, x))

            metaDataVLC = MetaDataVLC(self.pathFiles)
            self.metaDataList = metaDataVLC.getMetaData()

            self.currentMenu = "MainMenu"


        def getAudioDB(self):
            return (self.filesInFolder, self.pathFiles, self.metaDataList)

        def setSelection(self, selectionIndex):
            self.selectionIndex = selectionIndex

        def getSelection(self):
            return self.selectionIndex

        def getIndexByPath(self, pathFile):
            return self.pathFiles.index(pathFile)

        def getIndexByFile(self, fileInFolder):
            return self.filesInFolder.index(fileInFolder)

        def getCurrentMenu(self):
            return self.currentMenu

        def setCurrentMenu(self, menu):
            self.currentMenu = menu

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not RAM_DB.instance:
            RAM_DB.instance = RAM_DB.__RAM_DB()

    def __getattr__(self, name):
        return getattr(self.instance, name)