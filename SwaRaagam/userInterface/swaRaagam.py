import sys
# import os as _os
# import json

from SwaRaagam.userInterface.uiModels import QtWidgets
from SwaRaagam.core.ripple import Ripple
from SwaRaagam.userInterface import (
    welcomeScreen as _welcomeScreen,
    addSong as _addSong,
    lyricEditor as _lyricEditor,
    lyricLines as _lyricLines,
    pyqtUtils as _pyqtUtils
)


def setDisabledBtn(widget, btnList=None):
    if btnList is None:
        btnList = [False, True, True, True, True]
    widget.workFlowTray.audioInputStep.setEnabled(btnList[0])
    widget.workFlowTray.lyricInfoStep.setEnabled(btnList[1])
    widget.workFlowTray.lyricEditorStep.setEnabled(btnList[2])
    widget.workFlowTray.lyricMixStep.setEnabled(btnList[3])
    widget.workFlowTray.previewStep.setEnabled(btnList[4])


class SwaRaagamEditor(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SwaRaagamEditor, self).__init__(parent)
        self.btnActive = None
        self.project = None

        self.welcomeScreenWidget()

    def welcomeScreenWidget(self):
        if self.validateProgress():
            widget = _welcomeScreen.WelcomeScreen(self)
            widget.addLyricBtn.clicked.connect(self.stepOneWidget)
            self.setCentralWidget(widget)

    @_pyqtUtils.showWaitCursor
    def stepOneWidget(self):
        self.btnActive = 1
        if not self.project:
            self.project = Ripple()
        widget = _addSong.AddSong(self)
        if self.project.lyrics.getSongFile():
            widget.addSongWidget.selectedSong.setText(self.project.lyrics.getSongFile())
        widget.fileSelector.connect(self.regainFilePath)
        self.setButtonConnections(widget)
        self.setCentralWidget(widget)

    @_pyqtUtils.showWaitCursor
    def setTwoWidget(self):
        self.btnActive = 2
        if not self.project.lyrics.getSongFile():
            _pyqtUtils.warningDialog(self, "Song not added",
                                     "Please add the song to proceed with the lyricad data"
                                     )
            self.stepOneWidget()
        else:
            widget = _lyricEditor.AddLyricInfo(self)
            widget.addLyricInfoWidget.setSongName(self.project.lyrics.getSongName())
            widget.addLyricInfoWidget.setSingerNames(self.project.lyrics.getSingers())
            widget.addLyricInfoWidget.setLyricData(self.project.lyrics.getLyricData())
            if not self.project.lyrics.getSongName():
                widget.addLyricInfoWidget.setSongNameFromPath(self.project.lyrics.getSongFile())
            widget.addLyricInfoWidget.lyricData.connect(self.setLyricsToProject)
            self.setButtonConnections(widget)
            self.setCentralWidget(widget)

    @_pyqtUtils.showWaitCursor
    def setThreeWidget(self):
        self.btnActive = 3
        if not self.project.lyrics.getSongFile():
            _pyqtUtils.warningDialog(self, "Song not added",
                                     "Please add the song to proceed with the lyricad data"
                                     )
            self.stepOneWidget()
        elif not self.project.lyrics.validateJsonFile():
            _pyqtUtils.warningDialog(self,
                                     "Lyrics Not added",
                                     "Please add the lyrics to continue with the distribution of lyrics"
                                     )
            self.setTwoWidget()
        else:
            lyricData = self.project.getRawSongInfo()
            widget = _lyricLines.LyricLines(self)
            self.setButtonConnections(widget)
            self.setCentralWidget(widget)
            for eachLine in lyricData["Lyrics"].keys():
                widget.scrollWidget.addWidget(lyricData["Lyrics"][eachLine][0], lyricData["Lyrics"][eachLine][1])
            self.addSingerChecks(self.project.lyrics.getSingerChecks())
            widget.singersChecked.connect(self.addSingerChecks)

    @_pyqtUtils.showWaitCursor
    def setFourWidget(self):
        self.btnActive = 4
        if not self.project.lyrics.getSongFile():
            _pyqtUtils.warningDialog(self, "Song not added",
                                     "Please add the song to proceed with the lyricad data"
                                     )
            self.stepOneWidget()
        elif not self.project.lyrics.validateJsonFile():
            _pyqtUtils.warningDialog(self,
                                     "Lyrics Not added",
                                     "Please add the lyrics to continue with the distribution of lyrics"
                                     )
            self.setTwoWidget()
        else:
            widget = _lyricLines.LyricLines(self)
            self.setButtonConnections(widget)
            self.setCentralWidget(widget)

    def setFiveWidget(self):
        self.btnActive = 5
        print("Fifth step")

    def setButtonConnections(self, widget):
        widget.workFlowTray.homeBtn.clicked.connect(self.welcomeScreenWidget)
        widget.workFlowTray.audioInputStep.clicked.connect(self.stepOneWidget)
        widget.workFlowTray.lyricInfoStep.clicked.connect(self.setTwoWidget)
        widget.workFlowTray.lyricEditorStep.clicked.connect(self.setThreeWidget)
        widget.workFlowTray.lyricMixStep.clicked.connect(self.setFourWidget)
        widget.workFlowTray.previewStep.clicked.connect(self.setFiveWidget)
        btnList = []
        for eachType in range(5):
            if eachType == self.btnActive - 1:
                btnList.append(False)
            else:
                btnList.append(True)
        setDisabledBtn(widget, btnList)

    def regainFilePath(self, filePath):
        if self.project.lyrics.getSongFile():
            self.project.lyrics.removeSongFile()
        self.project.copyToDir(filePath)
        self.setTwoWidget()

    def setLyricsToProject(self, lyricInfo):
        self.project.lyrics.setSongName(lyricInfo[0])
        self.project.makeJsonFromInfo(lyricInfo[0], lyricInfo[1], lyricInfo[2])
        songName, singers, lyrics, singChecker = self.project.getSongInfo()
        self.project.lyrics.setSongName(songName)
        self.project.lyrics.setSingers(singers)
        self.project.lyrics.setLyricData(lyrics)
        self.project.lyrics.setSingerChecks(singChecker)

        self.setThreeWidget()

    def addSingerChecks(self, singerChecks):
        for index, singerCheck in enumerate(singerChecks):
            self.project.addSingerChecks(index, singerCheck)

    def validateProgress(self):
        if self.project and self.project.getProgress():
            query = _pyqtUtils.queryDialog(self, "Work in Progress",
                                           "Work is still in progress. If you click on yes the data will be "
                                           "removed.\nDo you really want to remove?")

            if query == QtWidgets.QMessageBox.Yes:
                self.project.deleteTempDir()
                self.welcomeScreenWidget()
                self.project = None
            else:
                if self.btnActive == 1:
                    self.stepOneWidget()
                elif self.btnActive == 2:
                    self.setTwoWidget()
                elif self.btnActive == 3:
                    self.setThreeWidget()
                return False
        return True


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    mainWindow = SwaRaagamEditor()
    mainWindow.show()
    sys.exit(app.exec_())
