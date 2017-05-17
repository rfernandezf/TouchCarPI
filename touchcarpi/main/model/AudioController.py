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
#   Description: This class has the responsibility of managing the audio files reproduction in any format.
# *************************************************************************************************************

import threading

from model.AudioFile import AudioFile
from model.AudioStatus import AudioStatus
from DB.RAM_DB import RAM_DB

from libs.SI4703 import SI4703
from control.threads.ButtonCoolDownThread import ButtonCoolDownThread
from control.threads.ChangeFrequencyThread import ChangeFrequencyThread
from control.threads.ThreadController import ThreadController

class AudioController:
    """
    This class has the responsibility of managing the audio files reproduction in any format.
    """

    # Singleton pattern
    class __AudioController:

        def __init__(self):
            """
            Constructor of the AudioController class.
            """

            self.db = RAM_DB()
            (self.fileName, self.pathFiles, self.metaDataList) = self.db.getAudioDB()
            #self.path = self.pathFiles[self.db.getSelection()]
            self.path = None
            self.audioObject = AudioFile(self.notifyController)
            self.currentFMStation = None
            self.SI4703 = SI4703()
            self.playingRadio = False
            self.observers = []
            self.GUICoolDown = False
            self.threadController = ThreadController()

        ###############################################################################
        #OBSERVER PATTERN
        ###############################################################################
        def register(self, observer):
            """
            Register method of the observer pattern.

            :param observer: Object to subscribe.
            """

            if not observer in self.observers:
                self.observers.append(observer)

        def unregister(self, observer):
            """
            Untegister method of the observer pattern.

            :param observer: Object to unsubscribe.
            """

            if observer in self.observers:
                self.observers.remove(observer)

        def unregister_all(self):
            """
            Unsubscribe all the subscribers.
            """

            if self.observers:
                del self.observers[:]

        def update_observers(self, *args, **kwargs):
            """
            Notify to all the observers/subscribers.

            :param args: args
            :param kwargs: kwargs
            """

            for observer in self.observers:
                observer.update(*args, **kwargs)
        ###############################################################################

        def getAudioObject(self):
            """
            Returns the audio object, instance of the AudioFile class.
            :return: Current Audio File instance.
            """

            return self.audioObject

        def loadAudio(self):
            """
            Loads an audio file. (Plays it).
            """

            if (self.playingRadio == True):
                self.stopRadio()

            if (self.audioObject.getStatus() == AudioStatus.NOFILE):
                self.audioObject.playAudio()
            else:
                self.audioObject.stopAudio()
                self.audioObject.playAudio()
            self.update_observers("NewMetaData", arg1=self.path, arg2=self.metaDataList[self.db.getSelection()])

        def startUpdateStatusThread(self):
            """
            Starts a thread that updates the reproduction status by polling to the vlc lib.
            """

            self.audioObject.startUpdateStatusThread()
            self.update_observers("NewMetaData", arg1=self.path, arg2=self.metaDataList[self.db.getSelection()])

        def nextTrack(self):
            """
            Switch to the next track of the list.
            """

            self.audioObject.stopAudio()
            if (self.db.getSelection()+1 < len(self.pathFiles)):
                self.db.setSelection(self.db.getSelection()+1)
            else:
                self.db.setSelection(0)

            self.loadAudio()

        def previousTrack(self):
            """
            Switch to the previous track of the list.
            """

            self.audioObject.stopAudio()
            if (self.db.getSelection()-1 >=  0):
                self.db.setSelection(self.db.getSelection()-1)
            else:
                self.db.setSelection(len(self.pathFiles)-1)
            self.loadAudio()

        def nextTrackEvent(self):
            """
            Manages the automatic change to the next track notifying to the GUI.
            """

            if (self.db.getSelection()+1 < len(self.pathFiles)):
                self.db.setSelection(self.db.getSelection()+1)
            else:
                self.db.setSelection(0)
            self.path = self.pathFiles[self.db.getSelection()]
            self.update_observers("NewMetaData", arg1=self.path, arg2=self.metaDataList[self.db.getSelection()])

        def pause(self):
            """
            Pauses the audio.
            """

            self.audioObject.pauseAudio()
            self.update_observers("AudioPaused", arg1=None, arg2=None)

        def resume(self):
            """
            Resumes a paused audio.
            """

            self.audioObject.resumeAudio()
            self.update_observers("AudioResumed", arg1=None, arg2=None)

        def changeAudioSecond(self, second):
            """
            Changes the current reproduction second to another second.

            :param second: New current second.
            """

            self.audioObject.changeAudioSecond(second)

        def updateReproductionSecondEvent(self, second):
            """
            Send an event to the observers when the current reproduction second changes.
            """

            self.update_observers("UpdateReproductionSecond", arg1=second, arg2=None)

        # TODO De aquí para abajo, todo con la librería
        def initRadio(self):
            if self.playingRadio == False:
                #STOP the reproduction of Audio
                if self.audioObject.getStatus() != AudioStatus.NOFILE:
                    self.audioObject.stopAudio()

                #Init the radio
                if(self.currentFMStation == None):
                    self.currentFMStation = 92.3
                self.update_observers("UpdateCurrentFMFrequency", arg1=self.currentFMStation, arg2=None)
                self.SI4703.initRadio()
                self.SI4703.setVolume(15)
                self.SI4703.setChannel(self.currentFMStation)
                self.playingRadio = True

        def stopRadio(self):
            if self.playingRadio == True:
                self.SI4703.stopRadio()
                self.playingRadio = False

        def setCurrentFMFrequency(self, frequency):
            if (frequency >= 87.5 and frequency <= 108):
                self.currentFMStation = frequency
                self.update_observers("UpdateCurrentFMFrequency", arg1=self.currentFMStation, arg2=None)
                self.SI4703.setChannel(self.currentFMStation)

        def getCurrentFMFrequency(self):
            return self.currentFMStation

        def getCurrentFMStationName(self):
            # TODO We can change this with a call to the library to get the RDS name
            return str(self.currentFMStation)

        def updateRadioObservers(self):
            self.update_observers("UpdateCurrentFMFrequency", arg1=self.currentFMStation, arg2=None)
            self.update_observers("UpdateRadioChannelData", arg1=None, arg2=None)

        def nextFrequency(self):
            if(self.currentFMStation >= 87.5 and self.currentFMStation < 108):
                self.currentFMStation = round(self.currentFMStation + 0.1, 2)
                self.update_observers("UpdateCurrentFMFrequency", arg1=self.currentFMStation, arg2=None)

        def previousFrequency(self):
            if (self.currentFMStation > 87.5 and self.currentFMStation <= 108):
                self.currentFMStation = round(self.currentFMStation - 0.1, 2)
                self.update_observers("UpdateCurrentFMFrequency", arg1=self.currentFMStation, arg2=None)

        def startChangeFrequencyThread(self):
            if(self.threadController.getChangeFrequencyThread() != None):
                self.threadController.getChangeFrequencyThread().stop()
                self.threadController.setChangeFrequencyThread(None)

            self.changeFrequencyThread = ChangeFrequencyThread(0.5, self.currentFMStation, self.setCurrentFMFrequency, self.startGUICoolDown)
            self.threadController.setChangeFrequencyThread(self.changeFrequencyThread)
            self.threadController.getChangeFrequencyThread().start()

        def seekUp(self):
            self.SI4703.seekUp(self.notifyController)

        def seekDown(self):
            self.SI4703.seekDown(self.notifyController)

        def setGUICoolDown(self, state):
            self.GUICoolDown = state

        def getGUICoolDown(self):
            return self.GUICoolDown

        def startGUICoolDown(self, ms = 0.5):
            buttonCoolDownThread = ButtonCoolDownThread(ms, self.setGUICoolDown)
            buttonCoolDownThread.start()


        def getStatus(self):
            """
            Returns the current status of the reproduction. See AudioStatus class.

            :return: Current status.
            """

            return self.audioObject.getStatus()

        def notifyController(self, notify, var = 0):
            """
            Method that other classes uses to notifie to the AudioController of the changes.

            :param notify: Kind of notification.
            :param var: Attached var.
            """

            if (notify == "nextTrack"):
                self.nextTrackEvent()
            elif (notify == "updateReproductionSecond"):
                self.updateReproductionSecondEvent(var)
            elif (notify == "endOfList"):
                self.nextTrack()
            elif (notify == "seekFrequencyChanged"):
                self.currentFMStation = var
                self.update_observers("UpdateCurrentFMFrequency", arg1=self.currentFMStation, arg2=None)


        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not AudioController.instance:
            AudioController.instance = AudioController.__AudioController()

    def __getattr__(self, name):
        return getattr(self.instance, name)