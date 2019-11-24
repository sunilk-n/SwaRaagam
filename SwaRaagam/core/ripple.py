import tempfile
import shutil
import os
import json

from SwaRaagam.core.lyricProject import LyricProject


class Ripple(object):
    def __init__(self):
        self._tempDir = tempfile.mkdtemp(prefix="swaRaagam")
        self.lyrics = LyricProject()
        self.songSettings = {}

    def getTempDir(self):
        return self._tempDir

    def deleteTempDir(self):
        shutil.rmtree(self.getTempDir())
        self._tempDir = None

    def makeZip(self, zipFile):
        pass

    def getProgress(self):
        progress = False
        if self._tempDir:
            progress = True
        return progress

    def copyToDir(self, filePath):
        shutil.copy2(filePath, self.getTempDir())
        songPath = os.path.join(self.getTempDir(), os.path.basename(filePath))
        self.lyrics.setSongFile(songPath)

    def makeJsonFromInfo(self, name, singers, lyrics):
        songSettings = {"SongName": name, "Singers": [singer.strip() for singer in singers.split(',')], "Lyrics": {}}
        songSettings["Lyrics"]["line0"] = ["Introduction"]
        songSettings = self.addSingerChecks(0, dataSample=songSettings)
        for i, eachLine in enumerate(lyrics.split('\n')):
            songSettings["Lyrics"]["line{}".format(i + 1)] = [eachLine]
            if eachLine == "":
                songSettings["Lyrics"]["line{}".format(i + 1)] = ["(music)"]
            songSettings = self.addSingerChecks(i + 1, dataSample=songSettings)
        songSettings["Lyrics"]["line{}".format(len(lyrics.split('\n')) + 1)] = ["Ending"]
        songSettings = self.addSingerChecks(len(lyrics.split('\n')) + 1, dataSample=songSettings)
        self.writeRawJson(songSettings)

    def addSingerChecks(self, index, singerCheck=(False, False, False), startTime=0, endTime=0, dataSample=None):
        data = dataSample
        if not data:
            data = self.getRawSongInfo()
        try:
            data['Lyrics']['line%s' % index][1] = singerCheck
        except:
            data['Lyrics']['line%s' % index].append(singerCheck)
        try:
            data['Lyrics']['line%s' % index][2] = startTime
        except:
            data['Lyrics']['line%s' % index].append(startTime)
        try:
            data['Lyrics']['line%s' % index][3] = endTime
        except:
            data['Lyrics']['line%s' % index].append(endTime)
        if not dataSample:
            self.writeRawJson(data)
        else:
            return data

    def getSongInfo(self):
        data = self.getRawSongInfo()
        songName = data['SongName']
        singers = ', '.join(data['Singers'])
        lyrics = '\n'.join(
            [data['Lyrics']['line%s' % line][0]
             if data['Lyrics']['line%s' % line][0] != '(music)' else ''
             for line in range(1, len(data['Lyrics']) - 1)]
        )
        singChecks = [data["Lyrics"][checker][1] for checker in data["Lyrics"].keys()]
        return songName, singers, lyrics, singChecks

    def getRawSongInfo(self):
        jsonFile = self.lyrics.getJsonFile()
        with open(jsonFile) as fd:
            data = json.load(fd)
        return data

    def writeRawJson(self, data):
        with open(self.lyrics.getJsonFile(), 'w') as fd:
            json.dump(data, fd, indent=2)
