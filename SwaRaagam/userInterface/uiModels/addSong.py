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
        Generated on: 16/11/2019 19:53:15
"""
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_songAddWidget(object):
    def setupUi(self, songAddWidget):
        songAddWidget.setObjectName("songAddWidget")
        songAddWidget.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(songAddWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.inputHolder = QtWidgets.QGridLayout()
        self.inputHolder.setObjectName("inputHolder")
        self.selectedSong = QtWidgets.QLabel(songAddWidget)
        self.selectedSong.setAlignment(QtCore.Qt.AlignCenter)
        self.selectedSong.setObjectName("selectedSong")
        self.inputHolder.addWidget(self.selectedSong, 0, 0, 1, 1)
        self.addSongBtn = QtWidgets.QPushButton(songAddWidget)
        self.addSongBtn.setObjectName("addSongBtn")
        self.inputHolder.addWidget(self.addSongBtn, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.inputHolder, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(143, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)

        self.retranslateUi(songAddWidget)
        QtCore.QMetaObject.connectSlotsByName(songAddWidget)

    def retranslateUi(self, songAddWidget):
        songAddWidget.setWindowTitle(QtWidgets.QApplication.translate("songAddWidget", "Form", None, -1))
        self.selectedSong.setText(QtWidgets.QApplication.translate("songAddWidget", "TextLabel", None, -1))
        self.addSongBtn.setText(QtWidgets.QApplication.translate("songAddWidget", "PushButton", None, -1))

