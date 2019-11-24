import os as _os

from SwaRaagam.userInterface.uiModels import *
from SwaRaagam.userInterface.workFlowTray import WorkFlowTray
from SwaRaagam.userInterface import pyqtUtils


class AddLyricInfoWidget(LyricEditorLegacy, QtWidgets.QWidget):
    lyricData = QtCore.Signal(list)

    def __init__(self, parent=None):
        super(AddLyricInfoWidget, self).__init__(parent)
        self.setupUi(self)
        self.connectSignals()

    def setSongNameFromPath(self, songPath):
        songFile = _os.path.basename(songPath)
        songName = _os.path.splitext(songFile)[0]
        self.setSongName(songName)

    def setSongName(self, songName):
        self.songNameEdit.setText(songName)

    def setSingerNames(self, singerNames):
        self.singersEdit.setText(singerNames)

    def setLyricData(self, lyricData):
        self.lyricEdit.setText(lyricData)

    def connectSignals(self):
        self.nextBtn.clicked.connect(self.collectLyricData)

    def collectLyricData(self):
        songName = self.songNameEdit.text()
        singerNames = self.singersEdit.text()
        lyric = self.lyricEdit.toPlainText()
        if not songName or not singerNames or not lyric:
            pyqtUtils.warningDialog(self, "Fill the lyrics",
                                    "Please fill all the lyric information to save")
        else:
            self.lyricData.emit([songName, singerNames, lyric])


class AddLyricInfo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddLyricInfo, self).__init__(parent)

        self.workFlowTray = WorkFlowTray(self)
        self.addLyricInfoWidget = AddLyricInfoWidget(self)

        self.setupUI()
        self.setButtonLabels()

    def setupUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.workFlowTray)
        layout.addWidget(self.addLyricInfoWidget)

    def setButtonLabels(self):
        self.addLyricInfoWidget.nextBtn.setText("Next")
        self.addLyricInfoWidget.songCoverBtn.setText("Image Browser")
