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
        self.avoidNotify = True
        self.listMediaPlayer.play_item_at_index(self.db.getSelection())
        self.reproductionStatusThread.start()

    def pauseAudio(self):
        self.listMediaPlayer.pause()

    def changeAudioSecond(self, second):
        self.mediaPlayer.set_time(second)

    def resumeAudio(self):
        self.listMediaPlayer.play()

    def stopAudio(self):
        self.reproductionStatusThread.stop()
        self.listMediaPlayer.stop()

    def getPath(self):
        return self.path


    def getMetaData(self):
        """
        libvlc_meta_Title
        libvlc_meta_Artist
        libvlc_meta_Genre
        libvlc_meta_Copyright
        libvlc_meta_Album
        libvlc_meta_TrackNumber
        libvlc_meta_Description
        libvlc_meta_Rating
        libvlc_meta_Date
        libvlc_meta_Setting
        libvlc_meta_URL
        libvlc_meta_Language
        libvlc_meta_NowPlaying
        libvlc_meta_Publisher
        libvlc_meta_EncodedBy
        libvlc_meta_ArtworkURL
        libvlc_meta_TrackID
        libvlc_meta_TrackTotal
        libvlc_meta_Director
        libvlc_meta_Season
        libvlc_meta_Episode
        libvlc_meta_ShowName
        libvlc_meta_Actors
        libvlc_meta_AlbumArtist
        libvlc_meta_DiscNumber
        libvlc_meta_DiscTotal
        """

        self.media = self.mediaPlayer.get_media()
        self.media.parse()

        metaData = []
        for i in range(0, 9):
            metaData.append(self.media.get_meta(i))
        metaData.append(self.media.get_duration())

        return metaData

    def nextItem(self, *args, **kwds):
        if (self.avoidNotify == False):
            #self.reproductionStatusThread.stop()
            self.notifyAudioController("nextTrack")
        else:
            self.avoidNotify = False


