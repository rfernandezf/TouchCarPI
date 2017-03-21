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

from DB.RAM_DB import RAM_DB
from control.threads.ThreadController import ThreadController
from control.threads.ReproductionStatusThread import ReproductionStatusThread

from . import vlc


class AudioFileVLC:

    def __init__(self, notifyAudioController):
        self.path = ""
        self.vlcInstance = vlc.Instance()
        self.mediaPlayer = self.vlcInstance.media_player_new()
        self.mediaList = self.vlcInstance.media_list_new()
        self.listMediaPlayer = self.vlcInstance.media_list_player_new()
        self.listMediaPlayer.set_media_player(self.mediaPlayer)
        self.db = RAM_DB()
        self.threadController = ThreadController()
        (self.fileName, self.pathFiles) = self.db.getAudioDB()
        self.notifyAudioController = notifyAudioController

        #This boolean avoid to notify of unnecesary changes to the AudioController, works as a flag
        self.avoidNotify = False

        self.reproductionEnded = False

        #For the VLC Event handler
        self.vlc_events = self.listMediaPlayer.event_manager()
        self.vlc_events.event_attach(vlc.EventType.MediaListPlayerNextItemSet, self.nextItem, 1)

        for i in range(0, len(self.pathFiles)):
            self.mediaList.insert_media(self.vlcInstance.media_new(self.pathFiles[i]), i)

        self.listMediaPlayer.set_media_list(self.mediaList)

        self.reproductionStatusThread = ReproductionStatusThread(self.mediaPlayer, self.notifyAudioController)
        self.threadController.setReproductionStatusThread(self.reproductionStatusThread)


    def playAudio(self, path):
        self.path = path
        print("file:///" + self.path)
        self.avoidNotify = True
        self.listMediaPlayer.play_item_at_index(self.db.getSelection())
        self.reproductionStatusThread.start()


    def pauseAudio(self):
        self.listMediaPlayer.pause()

    def resumeAudio(self, savedSecond):
        self.listMediaPlayer.play()

    def stopAudio(self):
        self.reproductionStatusThread.stop()
        self.listMediaPlayer.stop()

    def getPath(self):
        return self.path

    def getReproductionStatusThread(self):
        return self.getReproductionStatusThread

    def nextItem(self, *args, **kwds):
        if (self.avoidNotify == False):
            self.getReproductionStatusThread.stop()
            self.notifyAudioController("nextTrack")
        else:
            self.avoidNotify = False


