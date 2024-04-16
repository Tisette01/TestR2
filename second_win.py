from PyQt5.QtCore import Qt,QTimer,QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from final_win import FinalWin

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
        self.age = QLabel(txt_age)
        self.instruction1, self.instruction2, self.instruction3 = QLabel(txt_test1), QLabel(txt_test2), QLabel(txt_test3)
        self.time = QLabel(txt_timer)
        self.button1, self.button2, self.button3, self.nextbutton = QPushButton(txt_starttest1), QPushButton(txt_starttest2), QPushButton(txt_starttest3), QPushButton(txt_sendresults)
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
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
        self.button3.clicked.connect(self.timer_final)
        self.nextbutton.clicked.connect(self.next_click)
    
    def next_click(self):    
        self.hide()
        self.tw = FinalWin()
    
    def timer_test(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color:rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)


    def timer2Event(self):
        global time
        time = time.addSecs(1)
        self.text_timer.setText(time.toString('ss'))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color:rgb(0,0,0)')
        if time.toString('ss') == '30':
            self.timer.stop()
    
    def timer_final(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))        
        if int(time.toString('hh:mm:ss'[6:8]))>=45 or int(time.toString('hh:mm:ss'[6:8]))<=15:
            self.text_timer.setStyleSheet('color:rgb(0,255,0)')
        else:
            self.text_timer.setStyleSheet('color:rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
