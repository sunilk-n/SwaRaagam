from SwaRaagam.userInterface.uiModels import *
from SwaRaagam.userInterface.workFlowTray import WorkFlowTray


class LyricLinesWidget(LyricLineLegacy, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LyricLinesWidget, self).__init__(parent)
        self.setupUi(self)

    def setLyricLine(self, line):
        self.lyricLine.setText(line)

class ScrolledLyricWidget(LyricScrollLegacy, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ScrolledLyricWidget, self).__init__(parent)
        self.setupUi(self)

    def addWidget(self, line):
        widget = LyricLinesWidget(self)
        widget.setLyricLine(line)
        # self.layout.addWidget(widget)
        self.verticalLayout_2.addWidget(widget)

class LyricLines(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LyricLines, self).__init__(parent)

        self.workFlowTray = WorkFlowTray(self)
        self.scrollWidget = ScrolledLyricWidget(self)

        self.initUI()
        # self.exampleTemplate()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.workFlowTray)
        layout.addWidget(self.scrollWidget)

    def exampleTemplate(self):
        for eachTemplate in range(10):
            self.scrollWidget.addWidget("This is line %s" % eachTemplate)


