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
        Generated on: 24/11/2019 10:32:07
"""
from PySide2 import QtCore, QtGui, QtWidgets


class Ui_lyricLineLayout(object):
    def setupUi(self, lyricLineLayout):
        lyricLineLayout.setObjectName("lyricLineLayout")
        lyricLineLayout.resize(580, 43)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(lyricLineLayout)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineNumber = QtWidgets.QLabel(lyricLineLayout)
        self.lineNumber.setObjectName("lineNumber")
        self.horizontalLayout_2.addWidget(self.lineNumber)
        self.lyricLine = QtWidgets.QLabel(lyricLineLayout)
        self.lyricLine.setAlignment(QtCore.Qt.AlignCenter)
        self.lyricLine.setObjectName("lyricLine")
        self.horizontalLayout_2.addWidget(self.lyricLine)
        self.singerPartLayout = QtWidgets.QHBoxLayout()
        self.singerPartLayout.setObjectName("singerPartLayout")
        self.singerOneBtn = QtWidgets.QPushButton(lyricLineLayout)
        self.singerOneBtn.setCheckable(True)
        self.singerOneBtn.setObjectName("singerOneBtn")
        self.singerPartLayout.addWidget(self.singerOneBtn)
        self.singerTwoBtn = QtWidgets.QPushButton(lyricLineLayout)
        self.singerTwoBtn.setCheckable(True)
        self.singerTwoBtn.setObjectName("singerTwoBtn")
        self.singerPartLayout.addWidget(self.singerTwoBtn)
        self.groupBtn = QtWidgets.QPushButton(lyricLineLayout)
        self.groupBtn.setCheckable(True)
        self.groupBtn.setObjectName("groupBtn")
        self.singerPartLayout.addWidget(self.groupBtn)
        self.horizontalLayout_2.addLayout(self.singerPartLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)

        self.retranslateUi(lyricLineLayout)
        QtCore.QMetaObject.connectSlotsByName(lyricLineLayout)

    def retranslateUi(self, lyricLineLayout):
        lyricLineLayout.setWindowTitle(QtWidgets.QApplication.translate("lyricLineLayout", "Form", None, -1))
        self.lineNumber.setText(QtWidgets.QApplication.translate("lyricLineLayout", "TextLabel", None, -1))
        self.lyricLine.setText(QtWidgets.QApplication.translate("lyricLineLayout", "TextLabel", None, -1))
        self.singerOneBtn.setText(QtWidgets.QApplication.translate("lyricLineLayout", "PushButton", None, -1))
        self.singerTwoBtn.setText(QtWidgets.QApplication.translate("lyricLineLayout", "PushButton", None, -1))
        self.groupBtn.setText(QtWidgets.QApplication.translate("lyricLineLayout", "PushButton", None, -1))
