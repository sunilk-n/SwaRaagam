"""-*- coding: utf-8 -*-

###################################################

SwaRaagam - Lyric editor with song

Website path

contact: sunil.nerella39@gmail.com

###################################################


Copyright (C) 2019 Sunil Kumar Nerella

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
        Generated on: 24/11/2019 10:32:06
"""
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_editorHolder(object):
    def setupUi(self, editorHolder):
        editorHolder.setObjectName("editorHolder")
        editorHolder.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(editorHolder)
        self.gridLayout.setObjectName("gridLayout")
        self.singersEdit = QtWidgets.QLineEdit(editorHolder)
        self.singersEdit.setObjectName("singersEdit")
        self.gridLayout.addWidget(self.singersEdit, 1, 0, 1, 1)
        self.songCoverBtn = QtWidgets.QPushButton(editorHolder)
        self.songCoverBtn.setObjectName("songCoverBtn")
        self.gridLayout.addWidget(self.songCoverBtn, 0, 1, 2, 1)
        self.lyricEdit = QtWidgets.QTextEdit(editorHolder)
        self.lyricEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lyricEdit.setLineWidth(1)
        self.lyricEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lyricEdit.setObjectName("lyricEdit")
        self.gridLayout.addWidget(self.lyricEdit, 2, 0, 1, 2)
        self.songNameEdit = QtWidgets.QLineEdit(editorHolder)
        self.songNameEdit.setObjectName("songNameEdit")
        self.gridLayout.addWidget(self.songNameEdit, 0, 0, 1, 1)
        self.nextBtn = QtWidgets.QPushButton(editorHolder)
        self.nextBtn.setObjectName("nextBtn")
        self.gridLayout.addWidget(self.nextBtn, 3, 1, 1, 1)

        self.retranslateUi(editorHolder)
        QtCore.QMetaObject.connectSlotsByName(editorHolder)

    def retranslateUi(self, editorHolder):
        editorHolder.setWindowTitle(QtWidgets.QApplication.translate("editorHolder", "Form", None, -1))
        self.singersEdit.setPlaceholderText(QtWidgets.QApplication.translate("editorHolder", "Singer Names(Use \',\' for multiple names)", None, -1))
        self.songCoverBtn.setText(QtWidgets.QApplication.translate("editorHolder", "PushButton", None, -1))
        self.lyricEdit.setPlaceholderText(QtWidgets.QApplication.translate("editorHolder", "Add lyric lines here...", None, -1))
        self.songNameEdit.setPlaceholderText(QtWidgets.QApplication.translate("editorHolder", "Enter Song name", None, -1))
        self.nextBtn.setText(QtWidgets.QApplication.translate("editorHolder", "PushButton", None, -1))

