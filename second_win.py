from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *


class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.fio = QLabel(txt_hintname)
        self.age = QLabel()
        self.instruction1, self.instruction2, self.instruction3 = QLabel(), QLabel(), QLabel()
        self.time = QLabel()
        self.button1, self.button2, self.button3, self.nextbutton = QPushButton(), QPushButton(), QPushButton(), QPushButton()
        self.fioedit, self.ageedit, self.check1, self.check2, self.check3 = QLineEdit(), QLineEdit(txt_hintage), QLineEdit(), QLineEdit(), QLineEdit()
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line.addWidget(self.time, alignment = Qt.AlignRight)        
        self.l_line.addWidget(self.fio, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.fioedit, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.ageedit, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.instruction1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.check1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.instruction2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.instruction3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.check2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.check3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.nextbutton, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.hide()
        #self.tw = ThirdWin()

app = QApplication([])
sw = SecondWin()
app.exec_()