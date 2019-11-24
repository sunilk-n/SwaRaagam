import decorator
from SwaRaagam.userInterface.uiModels import QtWidgets, QtCore


def queryDialog(parent, title, msg):
    dialog = QtWidgets.QMessageBox
    ret = dialog.question(parent, title, msg, dialog.Yes | dialog.No)
    return ret


def warningDialog(parent, title, msg):
    dialog = QtWidgets.QMessageBox
    dialog.warning(parent, title, msg, dialog.Ok)


def getFileFromDialog(parent):
    filePath, _ = QtWidgets.QFileDialog.getOpenFileName(parent, caption="Load audio file",
                                                        dir="~/Music", filter="*.mp3 *.wav"
                                                        )


@decorator.decorator
def showWaitCursor(func, *args, **kwargs):
    QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
    try:
        return func(*args, **kwargs)
    finally:
        QtWidgets.QApplication.restoreOverrideCursor()
