import tempfile
import shutil
import os

from SwaRaagam.core.lyricProject import LyricProject


class Ripple(object):
    def __init__(self):
        self._tempDir = tempfile.mkdtemp(prefix="swaRaagam")
        self.lyrics = LyricProject()

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
