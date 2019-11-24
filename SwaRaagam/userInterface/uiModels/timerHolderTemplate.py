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
        Generated on: 24/11/2019 10:32:09
"""
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_timerHolderLayout(object):
    def setupUi(self, timerHolderLayout):
        timerHolderLayout.setObjectName("timerHolderLayout")
        timerHolderLayout.resize(689, 38)
        self.horizontalLayout = QtWidgets.QHBoxLayout(timerHolderLayout)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startTime = QtWidgets.QDoubleSpinBox(timerHolderLayout)
        self.startTime.setObjectName("startTime")
        self.horizontalLayout.addWidget(self.startTime)
        self.lyricLine = QtWidgets.QLabel(timerHolderLayout)
        self.lyricLine.setAlignment(QtCore.Qt.AlignCenter)
        self.lyricLine.setObjectName("lyricLine")
        self.horizontalLayout.addWidget(self.lyricLine)
        self.endTime = QtWidgets.QDoubleSpinBox(timerHolderLayout)
        self.endTime.setObjectName("endTime")
        self.horizontalLayout.addWidget(self.endTime)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(timerHolderLayout)
        QtCore.QMetaObject.connectSlotsByName(timerHolderLayout)

    def retranslateUi(self, timerHolderLayout):
        timerHolderLayout.setWindowTitle(QtWidgets.QApplication.translate("timerHolderLayout", "Form", None, -1))
        self.lyricLine.setText(QtWidgets.QApplication.translate("timerHolderLayout", "TextLabel", None, -1))

