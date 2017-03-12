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
#   Class name: AudioFile.py
#   Description: This class is a singleton facade for playing any kind of Audio file. It recives an audio file
#   and calls to the appropiate concrete class according to what type of audio file is.
# *************************************************************************************************************

from .AudioFileMP3 import AudioFileMP3
from .AudioStatus import AudioStatus
from DB.RAM_DB import RAM_DB

class AudioFile:

    class __AudioFile:
        def __init__(self):
            self.path = ""
            self.savedSecond = 0
            self.status = AudioStatus.NOFILE
            self.audioFileObject = None
            self.db = RAM_DB()
            (self.fileName, self.pathFiles) = self.db.getAudioDB()


        def playAudio(self, path):
            self.path = path
            if (self.status == AudioStatus.NOFILE):
                self.audioFileObject = self.__selectAudioType(self.path)
                self.audioFileObject.playAudio(self.path)
                self.status = AudioStatus.PLAYING


            elif (self.status == AudioStatus.PLAYING):
                self.audioFileObject.stopAudio()
                self.audioFileObject = self.__selectAudioType(self.path)
                self.audioFileObject.playAudio(self.path)

        def pauseAudio(self):
            self.audioFileObject.pauseAudio()

        def reanudeAudio(self, savedSecond):
            self.audioFileObject.reanudeAudio(savedSecond)

        def stopAudio(self):
            self.status = AudioStatus.NOFILE
            self.audioFileObject.stopAudio()
            self.audioFileObject = None

        def getPath(self):
            return self.path

        def __selectAudioType(self, path):
            if (self.path.endswith(".mp3")):
                audioType = AudioFileMP3()

            return audioType


        def getStatus(self):
            return self.status



        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not AudioFile.instance:
            AudioFile.instance = AudioFile.__AudioFile()

    def __getattr__(self, name):
        return getattr(self.instance, name)

