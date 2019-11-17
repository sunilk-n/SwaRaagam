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
        Generated on: 17/11/2019 23:25:03
"""
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_lyricScrollWidget(object):
    def setupUi(self, lyricScrollWidget):
        lyricScrollWidget.setObjectName("lyricScrollWidget")
        lyricScrollWidget.resize(480, 293)
        self.verticalLayout = QtWidgets.QVBoxLayout(lyricScrollWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lyricScrollArea = QtWidgets.QScrollArea(lyricScrollWidget)
        self.lyricScrollArea.setWidgetResizable(True)
        self.lyricScrollArea.setObjectName("lyricScrollArea")
        self.lyricScrollAreaWidget = QtWidgets.QWidget()
        self.lyricScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 460, 273))
        self.lyricScrollAreaWidget.setObjectName("lyricScrollAreaWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lyricScrollAreaWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lyricScrollArea.setWidget(self.lyricScrollAreaWidget)
        self.verticalLayout.addWidget(self.lyricScrollArea)

        self.retranslateUi(lyricScrollWidget)
        QtCore.QMetaObject.connectSlotsByName(lyricScrollWidget)

    def retranslateUi(self, lyricScrollWidget):
        lyricScrollWidget.setWindowTitle(QtWidgets.QApplication.translate("lyricScrollWidget", "Form", None, -1))

