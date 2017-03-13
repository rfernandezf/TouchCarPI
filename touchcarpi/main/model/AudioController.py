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
#   Class name: AudioController.py
#   Description: This class has the responsibility of
# *************************************************************************************************************


from model.AudioFile import AudioFile
from model.AudioStatus import AudioStatus
from DB.RAM_DB import RAM_DB
from . import vlc


class AudioController:

    class __AudioController:


        def __init__(self):
            self.db = RAM_DB()
            (self.fileName, self.pathFiles) = self.db.getAudioDB()
            self.path = self.pathFiles[self.db.getSelection()]
            self.audioObject = AudioFile()
            self.vlcObject = None
            self.observers = []

        ###############################################################################
        #OBSERVER PATTERN
        ###############################################################################
        def register(self, observer):
            if not observer in self.observers:
                self.observers.append(observer)

        def unregister(self, observer):
            if observer in self.observers:
                self.observers.remove(observer)

        def unregister_all(self):
            if self.observers:
                del self.observers[:]

        def update_observers(self, *args, **kwargs):
            for observer in self.observers:
                observer.update(*args, **kwargs)

        ###############################################################################

        def getAudioObject(self):
            return self.audioObject

        def loadAudio(self):
            self.path = self.pathFiles[self.db.getSelection()]
            print("SEL2: " + str(self.db.getSelection()))
            self.vlcObject = None
            self.vlcObject = vlc.MediaPlayer(self.path)
            self.event_manager = None
            self.event_manager = self.vlcObject.event_manager()
            self.event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.trackEnded)
            self.__selectAudioType(self.path)
            if (self.audioObject.getStatus() == AudioStatus.NOFILE):
                self.audioObject.playAudio(self.path)
            else:
                self.audioObject.stopAudio()
                self.audioObject.playAudio(self.path)
            self.update_observers("NewFile", arg1 = self.path)

        def nextTrack(self):
            self.audioObject.stopAudio()
            print("SEL1: " + str(self.db.getSelection()))
            if (self.db.getSelection()+1 < len(self.pathFiles)):
                self.db.setSelection(self.db.getSelection()+1)
            else:
                self.db.setSelection(0)
            self.loadAudio()

        def previousTrack(self):
            self.audioObject.stopAudio()
            if (self.db.getSelection()-1 >=  0):
                self.db.setSelection(self.db.getSelection()-1)
            else:
                self.db.setSelection(len(self.pathFiles)-1)
            self.loadAudio()

        def pause(self):
            self.audioObject.pauseAudio()
            self.update_observers("AudioPaused", arg1=None)

        def resume(self):
            self.audioObject.resumeAudio(0)
            self.update_observers("AudioResumed", arg1=None)

        def __selectAudioType(self, path):
            if (self.path.endswith(".mp3")):
                self.audioObject.setAudioType("MP3", self.vlcObject)

        def trackEnded(self, args):
            print("END")
            self.event_manager.event_detach(vlc.EventType.MediaPlayerEndReached)
            #self.nextTrack()


        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not AudioController.instance:
            AudioController.instance = AudioController.__AudioController()

    def __getattr__(self, name):
        return getattr(self.instance, name)