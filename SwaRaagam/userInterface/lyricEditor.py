import os as _os

from SwaRaagam.userInterface.uiModels import *
from SwaRaagam.userInterface.workFlowTray import WorkFlowTray


class AddLyricInfoWidget(LyricEditorLegacy, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddLyricInfoWidget, self).__init__(parent)
        self.setupUi(self)

    def setSongNameFromPath(self, songPath):
        songFile = _os.path.basename(songPath)
        songName = _os.path.splitext(songFile)[0]
        self.songNameEdit.setText(songName)


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
