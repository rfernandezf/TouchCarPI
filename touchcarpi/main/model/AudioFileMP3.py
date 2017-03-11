from . import vlc

class AudioFileMP3:

    def __init__(self):
        self.path = ""


    def playAudio(self, path):
        self.path = path
        print("file:///" + self.path)
        self.audioObject = vlc.MediaPlayer(self.path)
        self.audioObject.play()

    def pauseAudio(self):
        pass

    def reanudeAudio(self, savedSecond):
        pass

    def stopAudio(self):
        self.audioObject.stop()

    def getPath(self):
        return self.path