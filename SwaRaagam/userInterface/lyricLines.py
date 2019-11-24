from SwaRaagam.userInterface.uiModels import *
from SwaRaagam.userInterface.workFlowTray import WorkFlowTray


class LyricLinesWidget(LyricLineLegacy, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LyricLinesWidget, self).__init__(parent)
        self.setObjectName("LyricLineObject")
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.style = "#lyricLineLayout { Background: rgba(0, 0, 0, 20) }"
        self.setupUi(self)

    def setLyricLine(self, line):
        self.lyricLine.setText(line)
        self.setFixedHeight(50)

    def getLyricLine(self):
        return self.lyricLine.text()

    def getSingerEnabled(self):
        singer1 = self.singerOneBtn.isChecked()
        singer2 = self.singerTwoBtn.isChecked()
        group = self.groupBtn.isChecked()

        return [singer1, singer2, group]

    def enableBG(self):
        self.setStyleSheet(self.style)

    def setSingersChecked(self, singer1, singer2, group):
        if singer1:
            self.singerOneBtn.setChecked(True)
        if singer2:
            self.singerTwoBtn.setChecked(True)
        if group:
            self.groupBtn.setChecked(True)


class ScrolledLyricWidget(LyricScrollLegacy, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ScrolledLyricWidget, self).__init__(parent)
        self.setupUi(self)
        self.lineNumbers = 1

    def addWidget(self, line, singerChecks):
        widget = LyricLinesWidget(self)
        widget.setLyricLine(line)
        widget.lineNumber.setText(str(self.lineNumbers))
        widget.setSingersChecked(singerChecks[0], singerChecks[1], singerChecks[2])
        widget.lineNumber.setHidden(True)
        if self.lineNumbers % 2 == 0:
            widget.enableBG()
        self.innerScrollLayout.addWidget(widget)
        self.lineNumbers += 1


class LyricLines(QtWidgets.QWidget):
    singersChecked = QtCore.Signal(list)

    def __init__(self, parent=None):
        super(LyricLines, self).__init__(parent)

        self.workFlowTray = WorkFlowTray(self)
        self.scrollWidget = ScrolledLyricWidget(self)

        self.initUI()
        self.connectSignals()
        # self.exampleTemplate()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.workFlowTray)
        layout.addWidget(self.scrollWidget)

        self.scrollWidget.nextBtn.setText("Next")

    def connectSignals(self):
        self.scrollWidget.nextBtn.clicked.connect(self.getLyricSingers)

    def getLyricSingers(self):
        totWid = self.scrollWidget.innerScrollLayout.count()
        checkedList = []
        for each in range(totWid):
            widget = self.scrollWidget.innerScrollLayout.itemAt(each).widget()
            checkedList.append(widget.getSingerEnabled())
        self.singersChecked.emit(checkedList)

    def exampleTemplate(self):
        for eachTemplate in range(10):
            self.scrollWidget.addWidget("This is line %s" % eachTemplate)
