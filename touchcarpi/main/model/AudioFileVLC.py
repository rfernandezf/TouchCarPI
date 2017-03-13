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
#   Class name: AudioFileVLC.py
#   Description: It plays MP3/WAV files using the VLC lib.
# *************************************************************************************************************

from . import vlc

class AudioFileVLC:

    def __init__(self, vlcObject):
        self.path = ""
        self.audioObject = vlcObject

    def playAudio(self, path):
        self.path = path
        print("file:///" + self.path)

        self.audioObject.play()

    def pauseAudio(self):
        self.audioObject.pause()

    def resumeAudio(self, savedSecond):
        self.audioObject.play()

    def stopAudio(self):
        self.audioObject.stop()

    def getPath(self):
        return self.path
