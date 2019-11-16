import sys

from SwaRaagam.userInterface.uiModels import QtWidgets
from SwaRaagam.core.ripple import Ripple
from SwaRaagam.userInterface import (
    welcomeScreen as _welcomeScreen,
    addSong as _addSong,
    lyricEditor as _lyricEditor,
    pyqtUtils as _pyqtUtils
)


class SwaRaagamEditor(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SwaRaagamEditor, self).__init__(parent)

        self.project = None

        self.welcomeScreenWidget()

    def welcomeScreenWidget(self):
        if self.project and self.project.getProgress():
            query = _pyqtUtils.queryDialog(self, "Work in Progress",
                                            "Work is still in progress. If you click on yes the data will be removed.\nDo you really want to remove?")

            if query == QtWidgets.QMessageBox.Yes:
                self.project.deleteTempDir()
                self.welcomeScreenWidget()
                self.project = None
            else:
                self.stepOneWidget()
        else:
            widget = _welcomeScreen.WelcomeScreen(self)
            widget.addLyricBtn.clicked.connect(self.stepOneWidget)
            self.setCentralWidget(widget)

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

    def setTwoWidget(self):
        self.btnActive = 2
        widget = _lyricEditor.AddLyricInfo(self)
        self.setButtonConnections(widget)
        self.setCentralWidget(widget)

    def setThreeWidget(self):
        self.btnActive = 3
        print("This is next step")

    def setFourWidget(self):
        self.btnActive = 4
        print("Fourth step")

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
        self.setDisabledBtn(widget, btnList)

    def setDisabledBtn(self, widget, btnList=[False, True, True, True, True]):
        widget.workFlowTray.audioInputStep.setEnabled(btnList[0])
        widget.workFlowTray.lyricInfoStep.setEnabled(btnList[1])
        widget.workFlowTray.lyricEditorStep.setEnabled(btnList[2])
        widget.workFlowTray.lyricMixStep.setEnabled(btnList[3])
        widget.workFlowTray.previewStep.setEnabled(btnList[4])

    def regainFilePath(self, filePath):
        if self.project.lyrics.getSongFile():
            self.project.lyrics.removeSongFile()

        self.project.copyToDir(filePath)
        self.setTwoWidget()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    mainWindow = SwaRaagamEditor()
    mainWindow.show()
    sys.exit(app.exec_())
