# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Management.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from managestd import Ui_MainWindow1
from manage import Ui_MainWindow
from report import Ui_report
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

class Ui_Management(object):
    def managestd(self):
        self.MainWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def managesession(self):
        self.MainWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def report(self):
        self.report = QtGui.QMainWindow()
        self.ui = Ui_report()
        self.ui.setupUi(self.report)
        self.report.show()

    def setupUi(self, Management):
        Management.setObjectName(_fromUtf8("Management"))
        Management.resize(709, 593)
        self.centralwidget = QtGui.QWidget(Management)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, -9, 711, 591))
        self.graphicsView.setStyleSheet(_fromUtf8("background-color:\n"
"qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 129, 178, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 10, 711, 81))
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
        self.pushButton_2.setGeometry(QtCore.QRect(480, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 30, 91, 41))
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
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 180, 120, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 160, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.clicked.connect(self.managestd)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 110, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 90, 311, 471))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("E:/final year projects/documents/nimradesigner/QTdesigner/hgyg.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(370, 220, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        #################
        self.pushButton_7.clicked.connect(self.managesession)
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 280, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        ################
        self.pushButton_8.clicked.connect(self.managesession)
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(370, 340, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        ################
        self.pushButton_9.clicked.connect(self.managesession)
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(370, 390, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        ################
        self.pushButton_10.clicked.connect(self.report)
        Management.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Management)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Management.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Management)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Management.setStatusBar(self.statusbar)

        self.retranslateUi(Management)
        QtCore.QMetaObject.connectSlotsByName(Management)

    def retranslateUi(self, Management):
        Management.setWindowTitle(_translate("Management", "MainWindow", None))
        self.label_2.setText(_translate("Management", "Smart Classroom", None))
        self.pushButton_2.setText(_translate("Management", "Management", None))
        self.pushButton_4.setText(_translate("Management", "Add Subject", None))
        self.pushButton_6.setText(_translate("Management", "Manage Students", None))
        self.label_10.setText(_translate("Management", "Management", None))
        self.pushButton_3.setText(_translate("Management", "Processing", None))
        self.pushButton.setText(_translate("Management", "Registration", None))
        self.pushButton_7.setText(_translate("Management", "Manage Sessions", None))
        self.pushButton_8.setText(_translate("Management", "Manage Sections", None))
        self.pushButton_9.setText(_translate("Management", "Manage Subjects", None))
        self.pushButton_10.setText(_translate("Management", "Report", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Management = QtGui.QMainWindow()
    ui = Ui_Management()
    ui.setupUi(Management)
    Management.show()
    sys.exit(app.exec_())

