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
        Generated on: 24/11/2019 10:32:08
"""
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_lyricScrollWidget(object):
    def setupUi(self, lyricScrollWidget):
        lyricScrollWidget.setObjectName("lyricScrollWidget")
        lyricScrollWidget.resize(485, 118)
        self.gridLayout = QtWidgets.QGridLayout(lyricScrollWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lyricScrollArea = QtWidgets.QScrollArea(lyricScrollWidget)
        self.lyricScrollArea.setWidgetResizable(True)
        self.lyricScrollArea.setObjectName("lyricScrollArea")
        self.lyricScrollAreaWidget = QtWidgets.QWidget()
        self.lyricScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 465, 69))
        self.lyricScrollAreaWidget.setObjectName("lyricScrollAreaWidget")
        self.innerScrollLayout = QtWidgets.QVBoxLayout(self.lyricScrollAreaWidget)
        self.innerScrollLayout.setObjectName("innerScrollLayout")
        self.lyricScrollArea.setWidget(self.lyricScrollAreaWidget)
        self.gridLayout.addWidget(self.lyricScrollArea, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(386, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.nextBtn = QtWidgets.QPushButton(lyricScrollWidget)
        self.nextBtn.setObjectName("nextBtn")
        self.gridLayout.addWidget(self.nextBtn, 1, 1, 1, 1)

        self.retranslateUi(lyricScrollWidget)
        QtCore.QMetaObject.connectSlotsByName(lyricScrollWidget)

    def retranslateUi(self, lyricScrollWidget):
        lyricScrollWidget.setWindowTitle(QtWidgets.QApplication.translate("lyricScrollWidget", "Form", None, -1))
        self.nextBtn.setText(QtWidgets.QApplication.translate("lyricScrollWidget", "PushButton", None, -1))

