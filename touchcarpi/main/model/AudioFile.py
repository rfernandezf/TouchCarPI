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
#   Description: This class is a singleton facade for playing any kind of Audio file. It receives an audio file
#   and calls to the appropriate concrete class according to what type of audio file is.
# *************************************************************************************************************

from .AudioFileVLC import AudioFileVLC
from .AudioStatus import AudioStatus
from DB.RAM_DB import RAM_DB

class AudioFile:
    """
    This class is a singleton facade for playing any kind of Audio file.
    """

    #Singleton pattern
    class __AudioFile:
        def __init__(self, notifyAudioController):
            """
            Constructor of the AudioFile class.

            :param notifyAudioController: Method to notify of the changes to the Audio Controller.
            """

            self.savedSecond = 0
            self.status = AudioStatus.NOFILE
            self.audioFileObject = None
            self.db = RAM_DB()
            self.notifyAudioController = notifyAudioController
            (self.fileName, self.pathFiles, self.metaDataList) = self.db.getAudioDB()


        def playAudio(self):
            """
            Plays the selected audio file, don't matter what kind of format.
            """

            if (self.status == AudioStatus.NOFILE):
                self.audioFileObject = self.__selectAudioType(self.pathFiles[self.db.getSelection()])
                self.audioFileObject.playAudio()
                self.status = AudioStatus.PLAYING

            elif (self.status == AudioStatus.PLAYING or self.status == AudioStatus.PAUSED):
                self.audioFileObject.stopAudio()
                self.audioFileObject = self.__selectAudioType(self.pathFiles[self.db.getSelection()])
                self.audioFileObject.playAudio()

        def pauseAudio(self):
            """
            Pauses the current audio, managing it with the appropriate lib.
            """

            self.audioFileObject.pauseAudio()
            self.status = AudioStatus.PAUSED

        def resumeAudio(self, savedSecond):
            """
            Resumes the current audio, managing it with the appropriate lib.

            :param savedSecond: Second from where it resumes the reproduction.
            """

            self.audioFileObject.resumeAudio(savedSecond)

        def resumeAudio(self):
            """
            Resumes the current audio, managing it with the appropriate lib.
            """

            self.audioFileObject.resumeAudio()

        def changeAudioSecond(self, second):
            """
            Changes the current reproduction second to another second.

            :param second: New current second.
            """

            self.audioFileObject.changeAudioSecond(second)

        def stopAudio(self):
            """
            Stops the reproduction of the current audio, managing it with the appropriate lib.
            """

            self.status = AudioStatus.NOFILE
            self.audioFileObject.stopAudio()

        def startUpdateStatusThread(self):
            """
            Starts a thread that updates the reproduction status by polling to the vlc lib.
            """

            self.audioFileObject.startUpdateStatusThread()

        def __selectAudioType(self, path):
            """
            Private method that calls to the appropriate object depending on what kind of audio we want to reproduce.
            (Polimorfism)

            :param path: Path to the audio file.
            :return: Audio object using the appropriate lib.
            """

            if (path.endswith(".mp3") or path.endswith(".wav")):
                audioType = AudioFileVLC(self.notifyAudioController)

            return audioType

        def getStatus(self):
            """
            Returns the current status of the reproduction. See AudioStatus class.

            :return: Current status.
            """

            return self.status

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, notifyAudioController):
        if not AudioFile.instance:
            AudioFile.instance = AudioFile.__AudioFile(notifyAudioController)

    def __getattr__(self, name):
        return getattr(self.instance, name)

