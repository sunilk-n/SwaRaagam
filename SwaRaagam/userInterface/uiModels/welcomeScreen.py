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
        Generated on: 17/11/2019 23:25:04
"""
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_welcomeWidget(object):
    def setupUi(self, welcomeWidget):
        welcomeWidget.setObjectName("welcomeWidget")
        welcomeWidget.resize(400, 300)
        self.mainLayout = QtWidgets.QGridLayout(welcomeWidget)
        self.mainLayout.setObjectName("mainLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 105, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.buttonLayout = QtWidgets.QGridLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.editLyricBtn = QtWidgets.QPushButton(welcomeWidget)
        self.editLyricBtn.setObjectName("editLyricBtn")
        self.buttonLayout.addWidget(self.editLyricBtn, 1, 0, 1, 1)
        self.deleteLyricBtn = QtWidgets.QPushButton(welcomeWidget)
        self.deleteLyricBtn.setObjectName("deleteLyricBtn")
        self.buttonLayout.addWidget(self.deleteLyricBtn, 1, 1, 1, 1)
        self.addLyricBtn = QtWidgets.QPushButton(welcomeWidget)
        self.addLyricBtn.setObjectName("addLyricBtn")
        self.buttonLayout.addWidget(self.addLyricBtn, 0, 0, 1, 2)
        self.mainLayout.addLayout(self.buttonLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 105, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacerItem3, 2, 1, 1, 1)

        self.retranslateUi(welcomeWidget)
        QtCore.QMetaObject.connectSlotsByName(welcomeWidget)

    def retranslateUi(self, welcomeWidget):
        welcomeWidget.setWindowTitle(QtWidgets.QApplication.translate("welcomeWidget", "Form", None, -1))
        self.editLyricBtn.setText(QtWidgets.QApplication.translate("welcomeWidget", "PushButton", None, -1))
        self.deleteLyricBtn.setText(QtWidgets.QApplication.translate("welcomeWidget", "PushButton", None, -1))
        self.addLyricBtn.setText(QtWidgets.QApplication.translate("welcomeWidget", "PushButton", None, -1))

