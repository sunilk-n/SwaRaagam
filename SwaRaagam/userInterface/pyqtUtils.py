from SwaRaagam.userInterface.uiModels import QtWidgets

def queryDialog(parent, title, msg):
    dialog = QtWidgets.QMessageBox
    ret = dialog.question(parent, title, msg, dialog.Yes | dialog.No)
    return ret

def warningDialog(parent, title, msg):
    dialog = QtWidgets.QMessageBox
    dialog.warning(parent, title, msg, dialog.Ok)

def getFileFromDialog(parent, *args):
    filePath, _ = QtWidgets.QFileDialog.getOpenFileName(parent, caption="Load audio file",
                                                        dir="~/Music", filter="*.mp3 *.wav"
                                                        )
