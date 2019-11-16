from SwaRaagam.userInterface.uiModels import *


class WorkFlowTray(WorkFlowTrayLegacy, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WorkFlowTray, self).__init__(parent)
        self.setupUi(self)

        self.setBtnLables()

    def setBtnLables(self):
        self.homeBtn.setText("Home")
        self.audioInputStep.setText("Audio Input")
        self.lyricInfoStep.setText("Add Lyric Info")
        self.lyricEditorStep.setText("Lyric Editor")
        self.lyricMixStep.setText("Audio Mix")
        self.previewStep.setText("Preview Lyrics")
