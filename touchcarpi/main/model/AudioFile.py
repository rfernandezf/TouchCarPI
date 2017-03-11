

from .AudioFileMP3 import AudioFileMP3
from.AudioStatus import AudioStatus

class AudioFile:

    class __AudioFile:
        def __init__(self):
            self.path = ""
            self.savedSecond = 0
            self.status = AudioStatus.NOFILE
            self.audioFileObject = None

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

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not AudioFile.instance:
            AudioFile.instance = AudioFile.__AudioFile()

    def __getattr__(self, name):
        return getattr(self.instance, name)

