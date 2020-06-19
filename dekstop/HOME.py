# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HOME.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from registration import Ui_registration
from Addsubject import Ui_addsubject
from Management import Ui_Management
from processing import Ui_processing
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def reg(self):
        self.registration = QtGui.QMainWindow()
        self.ui = Ui_registration()
        self.ui.setupUi(self.registration)
        self.registration.show()
       

    def addsubject(self):
        self.addsubject = QtGui.QMainWindow()
        self.ui = Ui_addsubject()
        self.ui.setupUi(self.addsubject)
        self.addsubject.show()
        
    def manage(self):
        self.Management = QtGui.QMainWindow()
        self.ui = Ui_Management()
        self.ui.setupUi(self.Management)
        self.Management.show()

    def process(self):
        self.MainWindow = QtGui.QMainWindow()
        self.ui = Ui_processing()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(755, 599)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(5, 1, 751, 581))
        self.graphicsView.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:1, y1:0.71, x2:1, y2:0, stop:0 rgba(30, 140, 187, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 0, 741, 81))
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setBackgroundBrush(brush)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        ############
        self.pushButton_2.clicked.connect(self.manage)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        ##############
        self.pushButton_4.clicked.connect(self.addsubject)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 180, 120, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 240, 271, 171))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(430, 230, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        ##########
        self.pushButton_3.clicked.connect(self.process)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #########
        self.pushButton.clicked.connect(self.reg)
 
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 321, 481))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("E:/final year projects/documents/nimradesigner/QTdesigner/hgyg.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Smart Classroom", None))
        self.pushButton_2.setText(_translate("MainWindow", "Management", None))
        self.pushButton_4.setText(_translate("MainWindow", "Add Subject", None))
        self.label_3.setText(_translate("MainWindow", "We provide the automated solution to mark students\' attendance and moniter them during class using face and expression recognition", None))
        self.label_10.setText(_translate("MainWindow", "About Services", None))
        self.pushButton_3.setText(_translate("MainWindow", "Processing", None))
        self.pushButton.setText(_translate("MainWindow", "Registration", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

