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
#   Description: Plays MP3/WAV or other supported files using the VLC lib.
# *************************************************************************************************************

from DB.RAM_DB import RAM_DB
from control.threads.ReproductionStatusThread import ReproductionStatusThread
from control.threads.ThreadController import ThreadController

import libs.vlc as vlc


class AudioFileVLC:
    """
    Plays MP3/WAV or other supported files using the VLC lib.
    """

    def __init__(self, notifyAudioController):
        """
        Constructor of the AudioFileVLC class.

        :param notifyAudioController: Method to notify of the changes to the Audio Controller.
        """

        self.vlcInstance = vlc.Instance()
        self.mediaPlayer = self.vlcInstance.media_player_new()
        self.mediaList = self.vlcInstance.media_list_new()
        self.listMediaPlayer = self.vlcInstance.media_list_player_new()
        self.listMediaPlayer.set_media_player(self.mediaPlayer)
        self.db = RAM_DB()
        self.threadController = ThreadController()
        (self.fileName, self.pathFiles, self.metaDataList) = self.db.getAudioDB()
        self.notifyAudioController = notifyAudioController

        #This boolean avoid to notify of unnecesary changes to the AudioController, works as a flag
        self.avoidNotify = False
        #This boolean avoid to stop the medialistplayer when is already stopped because have reached the end of the list.
        self.reproductionEnded = False

        for i in range(0, len(self.pathFiles)):
            self.mediaList.insert_media(self.vlcInstance.media_new(self.pathFiles[i]), i)

        self.listMediaPlayer.set_media_list(self.mediaList)

        #For the VLC Event handler
        self.vlc_eventsMediaList = self.listMediaPlayer.event_manager()
        self.vlc_eventsMediaPlayer = self.mediaPlayer.event_manager()
        self.vlc_eventsMediaPlayer.event_attach(vlc.EventType.MediaPlayerEndReached, self.endOfSong, 1)
        self.vlc_eventsMediaList.event_attach(vlc.EventType.MediaListPlayerNextItemSet, self.nextItem, 1)



        self.reproductionStatusThread = None


    def playAudio(self):
        """
        Plays an audio file.
        """

        self.avoidNotify = True
        self.listMediaPlayer.play_item_at_index(self.db.getSelection())
        # We only starts the thread that make polling for gets the current reproduction second if the current menu is the PlayAudioMenu
        if(self.db.getCurrentMenu() == "PlayAudioMenu"):
            self.startUpdateStatusThread()

    def startUpdateStatusThread(self):
        """
        Starts a thread that updates the reproduction status by polling to the vlc lib.
        """

        self.reproductionStatusThread = ReproductionStatusThread(self.mediaPlayer, self.notifyAudioController)
        self.threadController.setReproductionStatusThread(self.reproductionStatusThread)
        self.threadController.getReproductionStatusThread().start()

    def pauseAudio(self):
        """
        Pauses the audio.
        """

        self.listMediaPlayer.pause()

    def changeAudioSecond(self, second):
        """
        Changes the current reproduction second to another second.

        :param second: New current second.
        """

        self.mediaPlayer.set_time(second)

    def resumeAudio(self):
        """
        Resumes a paused audio.
        """

        self.listMediaPlayer.play()

    def stopAudio(self):
        """
        Stops the reproduction of an audio.
        """

        if (self.threadController.getReproductionStatusThread() != None):
            self.threadController.getReproductionStatusThread().stop()

        # At the end of the list, VLC Lib makes a stop() to the media player list by default.
        # If we make a stop() two times, it hangs
        if (self.reproductionEnded == False):
            self.listMediaPlayer.stop()
        else:
            self.reproductionEnded = False

    def getPath(self):
        """
        Returns the path of the file that it's being reproduced.

        :return: String with the path.
        """

        return self.path

    def nextItem(self, *args, **kwds):
        """
        Method called by the VLC event manager when the reproduction item has changed.

        :param args: args
        :param kwds: kwds
        """

        if (self.avoidNotify == False):
            self.notifyAudioController("nextTrack")
        else:
            self.avoidNotify = False

    def endOfSong(self, *args, **kwds):
        """
        Method called by the VLC event manager when the reproduction item ends.

        :param args: args
        :param kwds: kwds
        """

        # If the song ended & is the last of the list, must notify to the controller
        if self.db.getSelection() == (len(self.pathFiles)-1):
            self.reproductionEnded = True
            self.notifyAudioController("endOfList")


