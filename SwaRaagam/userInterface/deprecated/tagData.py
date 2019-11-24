from PySide2 import (
    QtWidgets as QtGui,
    QtCore
)
import sys
from functools import partial

class TagBar(QtGui.QWidget):
    def __init__(self):
        super(TagBar, self).__init__()
        self.setWindowTitle('Tag Bar')
        self.tags = []
        self.h_layout = QtGui.QHBoxLayout()
        self.h_layout.setSpacing(4)
        self.setLayout(self.h_layout)
        self.line_edit = QtGui.QLineEdit()
        self.line_edit.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.setContentsMargins(2,2,2,2)
        self.h_layout.setContentsMargins(2,2,2,2)
        self.refresh()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.line_edit.returnPressed.connect(self.create_tags)

    def create_tags(self):
        new_tags = self.line_edit.text().split(', ')
        print(new_tags)
        self.line_edit.setText('')
        self.tags.extend(new_tags)
        self.tags = list(set(self.tags))
        self.tags.sort(key=lambda x: x.lower())
        self.refresh()

    def refresh(self):
        for i in reversed(range(self.h_layout.count())):
            self.h_layout.itemAt(i).widget().setParent(None)
        for tag in self.tags:
            self.add_tag_to_bar(tag)
        self.h_layout.addWidget(self.line_edit)
        self.line_edit.setFocus()

    def add_tag_to_bar(self, text):
        tag = QtGui.QFrame()
        tag.setStyleSheet('border:1px solid rgb(192, 192, 192); border-radius: 4px;')
        tag.setContentsMargins(2, 2, 2, 2)
        tag.setFixedHeight(28)
        hbox = QtGui.QHBoxLayout()
        hbox.setContentsMargins(4, 4, 4, 4)
        hbox.setSpacing(10)
        tag.setLayout(hbox)
        label = QtGui.QLabel(text)
        label.setStyleSheet('border:0px')
        label.setFixedHeight(16)
        hbox.addWidget(label)
        x_button = QtGui.QPushButton('x')
        x_button.setFixedSize(20, 20)
        x_button.setStyleSheet('border:0px; font-weight:bold')
        x_button.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        x_button.clicked.connect(partial(self.delete_tag, text))
        hbox.addWidget(x_button)
        tag.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        self.h_layout.addWidget(tag)

    def delete_tag(self, tag_name):
        self.tags.remove(tag_name)
        self.refresh()

if __name__ == '__main__':
    qt_app = QtGui.QApplication(sys.argv)
    tag_bar = TagBar()
    qt_app.exec_()