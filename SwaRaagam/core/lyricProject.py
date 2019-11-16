import os

class LyricProject(object):
    def __init__(self, songFile=None,
                 lyricData=None,songName=None,
                 singers=None, lyricTiming=None):
        self._songFile = songFile
        self._lyricData = lyricData
        self._songName = songName
        self._singers = singers
        self._lyricTiming = lyricTiming

    def getSongFile(self):
        return self._songFile

    def setSongFile(self, songPath):
        self._songFile = songPath

    def getLyricData(self):
        return self._lyricData

    def setLyricData(self, lyricData):
        self._lyricData = lyricData

    def getSongName(self):
        return self._songName

    def setSongName(self, songName):
        self._songName = songName

    def getSingers(self):
        return self._singers

    def setSingers(self, singers):
        self._singers = singers

    def getLyricTiming(self):
        return self._lyricTiming

    def setLyricTiming(self, timingData):
        self._lyricTiming = timingData

    def getInfoFromSaved(self):
        """ Here comes the code for the edit lyrics
        """
        pass

    def removeSongFile(self):
        os.remove(self.getSongFile())
        self.setSongFile(None)
