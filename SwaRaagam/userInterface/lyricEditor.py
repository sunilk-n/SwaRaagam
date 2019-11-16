from SwaRaagam.userInterface.uiModels import *
from SwaRaagam.userInterface.workFlowTray import WorkFlowTray


class AddLyricInfoWidget(LyricEditorLegacy, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddLyricInfoWidget, self).__init__(parent)
        self.setupUi(self)


class AddLyricInfo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddLyricInfo, self).__init__(parent)

        self.workFlowTray = WorkFlowTray(self)
        self.addLyricInfoWidget = AddLyricInfoWidget(self)

        self.setupUI()

    def setupUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.workFlowTray)
        layout.addWidget(self.addLyricInfoWidget)
