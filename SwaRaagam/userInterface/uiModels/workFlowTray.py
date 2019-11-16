"""-*- coding: utf-8 -*-

###################################################

SwaRaagam - Lyric editor with song

Website path

contact: sunil.nerella39@gmail.com

###################################################


Copyright (C) 2019-2020 Sunil Kumar Nerella

Licensed under GNU GPL-3.0-or-later

This file is part of SwaRaagam.

SwaRaagam is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

SwaRaagam is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with SwaRaagam.  If not, see <https://www.gnu.org/licenses/>.

        
        Created By: Sunil Kumar Nerella            
        Generated on: 16/11/2019 19:53:18
"""
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_workFlowTray(object):
    def setupUi(self, workFlowTray):
        workFlowTray.setObjectName("workFlowTray")
        workFlowTray.resize(579, 41)
        self.workflowHolder = QtWidgets.QHBoxLayout(workFlowTray)
        self.workflowHolder.setObjectName("workflowHolder")
        self.homeBtn = QtWidgets.QPushButton(workFlowTray)
        self.homeBtn.setObjectName("homeBtn")
        self.workflowHolder.addWidget(self.homeBtn)
        self.audioInputStep = QtWidgets.QPushButton(workFlowTray)
        self.audioInputStep.setObjectName("audioInputStep")
        self.workflowHolder.addWidget(self.audioInputStep)
        self.lyricInfoStep = QtWidgets.QPushButton(workFlowTray)
        self.lyricInfoStep.setObjectName("lyricInfoStep")
        self.workflowHolder.addWidget(self.lyricInfoStep)
        self.lyricEditorStep = QtWidgets.QPushButton(workFlowTray)
        self.lyricEditorStep.setObjectName("lyricEditorStep")
        self.workflowHolder.addWidget(self.lyricEditorStep)
        self.lyricMixStep = QtWidgets.QPushButton(workFlowTray)
        self.lyricMixStep.setObjectName("lyricMixStep")
        self.workflowHolder.addWidget(self.lyricMixStep)
        self.previewStep = QtWidgets.QPushButton(workFlowTray)
        self.previewStep.setObjectName("previewStep")
        self.workflowHolder.addWidget(self.previewStep)

        self.retranslateUi(workFlowTray)
        QtCore.QMetaObject.connectSlotsByName(workFlowTray)

    def retranslateUi(self, workFlowTray):
        workFlowTray.setWindowTitle(QtWidgets.QApplication.translate("workFlowTray", "Form", None, -1))
        self.homeBtn.setText(QtWidgets.QApplication.translate("workFlowTray", "PushButton", None, -1))
        self.audioInputStep.setText(QtWidgets.QApplication.translate("workFlowTray", "PushButton", None, -1))
        self.lyricInfoStep.setText(QtWidgets.QApplication.translate("workFlowTray", "PushButton", None, -1))
        self.lyricEditorStep.setText(QtWidgets.QApplication.translate("workFlowTray", "PushButton", None, -1))
        self.lyricMixStep.setText(QtWidgets.QApplication.translate("workFlowTray", "PushButton", None, -1))
        self.previewStep.setText(QtWidgets.QApplication.translate("workFlowTray", "PushButton", None, -1))

