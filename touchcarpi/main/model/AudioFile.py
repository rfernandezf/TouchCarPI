

from .AudioFileMP3 import AudioFileMP3

class AudioFile:

    def __init__(self):
        self.path = ""
        self.savedSecond = 0
        self.status = False
        self.audioFileObject = None

    def playAudio(self, path):
        self.path = path
        if(self.status == False):
            if (self.path.endswith(".mp3")):
                self.audioFileObject = AudioFileMP3()
            self.status = True
        self.audioFileObject.playAudio(self.path)

    def pauseAudio(self):
        self.audioFileObject.pauseAudio()

    def reanudeAudio(self, savedSecond):
        self.audioFileObject.reanudeAudio(savedSecond)

    def stopAudio(self):
        self.status = False
        self.audioFileObject.stopAudio()
        self.audioFileObject = None

    def getPath(self):
        return self.path