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
import platform

from .MetaDataVLC import MetaDataVLC
from lxml import etree
from operator import itemgetter


class RAM_DB:
    """
    This class creates some list and structures with info for the application. The DB class is
    a singleton.
    """

    #Singleton pattern
    class __RAM_DB:
        def __init__(self):
            """
            Constructor of the class.
            """

            # List all the files in the desired format (MP3, WAV...)
            self.filesInFolder = []
            # List with the full path to all the files, for get the meta data
            self.pathFiles = []
            # Selected song of the list (the number is the index)
            self.selectionIndex = 0

            if platform.system() == "Windows":
                musicDir = str(os.path.expanduser("~\Music"))
            elif platform.system() == "Linux":
                print(str(os.path.expanduser("~/Music")))
                musicDir = str(os.path.expanduser("~/Music"))
            else:
                musicDir = "Music"

            for (dirpath, dirnames, filenames) in os.walk(musicDir):
                for x in filenames:
                    if x.endswith(".mp3") or x.endswith(".wav"):
                        self.filesInFolder.append(x)
                        self.pathFiles.append(os.path.join(dirpath, x))

            metaDataVLC = MetaDataVLC(self.pathFiles)
            self.metaDataList = metaDataVLC.getMetaData

            self.__sortAudioDBByNames()

            self.currentMenu = "MainMenu"

        def __sortAudioDBByNames(self):
            """
            Sort all the songs alphabetically by the name of the songs
            """

            #Cambiar el metadato que tenga extension .mp3 para no escribir la extensión
            metaDataNames= []

            for i in range(0, len(self.metaDataList)):
                metaDataNames.append(self.metaDataList[i][0])

            print(metaDataNames)
            metaDataNames, self.pathFiles, self.filesInFolder = zip(*sorted(zip(metaDataNames, self.pathFiles, self.filesInFolder)))
            self.metaDataList = sorted(self.metaDataList, key=itemgetter(0))
            print(self.metaDataList)

        def getArtworkNotFoundPath(self):
            """
            Returns a string with the path of the artwork not found image.
            :return: String with the path.
            """

            return "themes/default/img/artworkNotFound.png"


        def getAudioDB(self):
            """
            Returns the AudioDB

            :return: Three lists of strings with all the data:
            """

            return (self.filesInFolder, self.pathFiles, self.metaDataList)

        def setSelection(self, selectionIndex):
            """
            Sets the current song's index.

            :param selectionIndex: Index of the song in the list
            """

            self.selectionIndex = selectionIndex

        def getSelection(self):
            """
            Returns the index of the current song.

            :return: Index of the current song.
            """

            return self.selectionIndex

        def getIndexByPath(self, pathFile):
            """
            Returns the index of the song in the list of songs by the path of the file.

            :param pathFile: Full path of the song.
            :return: Index of the song.
            """

            return self.pathFiles.index(pathFile)

        def getIndexByFile(self, fileInFolder):
            """
            Returns the index of the song in the list of songs by the file name.

            :param fileInFolder: File name of the song.
            :return: Index of the song.
            """

            return self.filesInFolder.index(fileInFolder)

        def getCurrentMenu(self):
            """
            Returns the current menu that the user is viewing.

            :return: String whith the name of the current menu.
            """

            return self.currentMenu

        def setCurrentMenu(self, menu):
            """
            Sets the current menu that the user is viewing.

            :param menu: String with the name of the menu.
            """

            self.currentMenu = menu

        def getRadioChannels(self):
            """
            Returns a list of tuples with the name and frequency of the memorized channels of radio.

            :return: List with a tuple (frequency, name)
            """

            # Pre-allocating the size of the list, we have 9 items, one per memory button
            result = [None]*9

            # Opening the XML
            xmlFile = etree.parse("config/RadioChannels.xml").getroot()


            for channelItem in xmlFile.findall('channel'):
                result[int(channelItem.get("id"))] = ((float(channelItem.get('freq')), channelItem.text))

            return result

        def setRadioChannel(self, id, freq, name):
            """
            Sets the name and frequency into the memory bank of the radio menu.

            :param id: Id of the bank.
            :param freq: Frequency of the new channel.
            :param name: Name of the new channel.
            """

            xmlFile = etree.parse("config/RadioChannels.xml").getroot()

            for channelItem in xmlFile.findall('channel'):
                if(int(channelItem.get("id")) == id):
                    channelItem.set("freq", str(freq))
                    channelItem.text = name

            obj_xml = etree.tostring(xmlFile,
                                     pretty_print=True,
                                     xml_declaration=True)

            try:
                with open("config/RadioChannels.xml", "wb") as xml_writer:
                    xml_writer.write(obj_xml)
            except IOError:
                print("IOError: Error trying to write into the XML file.")



        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not RAM_DB.instance:
            RAM_DB.instance = RAM_DB.__RAM_DB()

    def __getattr__(self, name):
        return getattr(self.instance, name)