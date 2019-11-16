from SwaRaagam.userInterface.uiModels import *
from SwaRaagam.userInterface.workFlowTray import WorkFlowTray


class AddSongWidget(AddSongLegacy, QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(AddSongWidget, self).__init__(parent)
        self.setupUi(self)

        self.setAllLables()

    def setAllLables(self):
        self.selectedSong.setText("No song selected")
        self.addSongBtn.setText("Click to browse")


class AddSong(QtWidgets.QWidget):
    fileSelector = QtCore.Signal(str)
    def __init__(self, parent=None):
        super(AddSong, self).__init__(parent)

        self.addSongWidget = AddSongWidget(self)
        self.workFlowTray = WorkFlowTray(self)

        self.setupUI()
        self.connections()

    def setupUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.workFlowTray)
        layout.addWidget(self.addSongWidget)

    def connections(self):
        self.addSongWidget.addSongBtn.clicked.connect(self.getFileFromDialog)

    def getFileFromDialog(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption="Load audio file",
                                                        dir="~/Music/", filter="*.mp3 *.wav"
                                                        )
        self.addSongWidget.selectedSong.setText(filePath)
        self.fileSelector.emit(filePath)
