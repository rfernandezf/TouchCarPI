import os


class RAM_DB():

    def __init__(self):
        #Obtengo los archivos de audio MP3
        self.filesInFolder = []
        self.pathFiles = []
        self.selectionIndex = 0

        for (dirpath, dirnames, filenames) in os.walk("Music"):
            for x in filenames:
                if x.endswith(".mp3"):
                    self.filesInFolder.append(x)
                    self.pathFiles.append(os.path.join(dirpath, x))


    def getAudioDB(self):
        return (self.filesInFolder, self.pathFiles)

    def setSelection(self, selectionIndex):
        self.selectionIndex = selectionIndex

    def getSelection(self):
        return self.selectionIndex

    def getIndexByPath(self, pathFile):
        return self.pathFiles.index(pathFile)

    def getIndexByFile(self, fileInFolder):
        return self.filesInFolder.index(fileInFolder)