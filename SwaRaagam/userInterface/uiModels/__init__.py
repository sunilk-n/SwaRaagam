from SwaRaagam.userInterface.uiModels.addSong import Ui_songAddWidget as AddSongLegacy
from SwaRaagam.userInterface.uiModels.lyricEditor import Ui_editorHolder as LyricEditorLegacy
from SwaRaagam.userInterface.uiModels.welcomeScreen import Ui_welcomeWidget as WelcomeScreenLegacy
from SwaRaagam.userInterface.uiModels.workFlowTray import Ui_workFlowTray as WorkFlowTrayLegacy
from SwaRaagam.userInterface.uiModels.lyricLineTemplate import Ui_lyricLineLayout as LyricLineLegacy
from SwaRaagam.userInterface.uiModels.lyricScrollWidget import Ui_lyricScrollWidget as LyricScrollLegacy
from PySide2 import QtWidgets, QtCore, QtGui


__all__ = [
    # Defined Qt modules
    "AddSongLegacy", "LyricEditorLegacy",
    "WelcomeScreenLegacy", "WorkFlowTrayLegacy",
    "LyricLineLegacy", "LyricScrollLegacy",
    # Inbuilt Qt modules
    "QtWidgets", "QtGui", "QtCore"
]