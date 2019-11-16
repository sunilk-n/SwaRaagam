from SwaRaagam.userInterface.uiModels import *


class WelcomeScreen(WelcomeScreenLegacy, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WelcomeScreen, self).__init__(parent)
        self.setupUi(self)
        self.setButtonText()

    def setButtonText(self):
        self.addLyricBtn.setText("Add Lyrics")
        self.editLyricBtn.setText("Edit Lyrics")
        self.deleteLyricBtn.setText("Delete Lyrics")

    def setConnections(self):
        pass
