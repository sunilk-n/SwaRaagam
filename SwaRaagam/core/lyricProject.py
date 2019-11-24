import os
import shutil


class LyricProject(object):
    def __init__(self, songFile=None,
                 lyricData=None, songName=None,
                 singers=None, singerChecks=None,
                 lyricTiming=None, jsonFile=None):
        self._songFile = songFile
        self._lyricData = lyricData
        self._songName = songName
        self._singers = singers
        self._singerChecks = singerChecks
        self._lyricTiming = lyricTiming
        self._jsonFile = jsonFile

    def getSongFile(self):
        return self._songFile

    def setSongFile(self, songPath):
        self._songFile = songPath

    def getJsonFile(self):
        songFile = self.getSongFile()
        if not songFile:
            return
        jsonFile = "%s.json" % (os.path.splitext(songFile)[0])
        self._jsonFile = jsonFile
        return self._jsonFile

    def getLyricData(self):
        return self._lyricData

    def setLyricData(self, lyricData):
        self._lyricData = lyricData

    def getSongName(self):
        return self._songName

    def setSongName(self, songName):
        songFile = os.path.splitext(self.getSongFile())
        dirPath = os.path.dirname(songFile[0])
        newSongFile = os.path.join(dirPath, "{0}{1}".format(songName, songFile[-1]))
        shutil.move(self.getSongFile(), newSongFile)
        self.setSongFile(newSongFile)
        self._songName = songName

    def getSingers(self):
        return self._singers

    def setSingers(self, singers):
        self._singers = singers

    def getLyricTiming(self):
        return self._lyricTiming

    def setLyricTiming(self, timingData):
        self._lyricTiming = timingData

    def getSingerChecks(self):
        return self._singerChecks

    def setSingerChecks(self, singerChecks):
        self._singerChecks = singerChecks

    def getInfoFromSaved(self):
        """ Here comes the code for the edit lyrics
        """
        pass

    def removeSongFile(self):
        os.remove(self.getSongFile())
        self.setSongFile(None)

    def validateJsonFile(self):
        valid = True
        if not self.getSongFile() or not os.path.exists(self.getJsonFile()):
            valid = False
        return valid
