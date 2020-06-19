# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'processing.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymysql
from PyQt4.QtGui import QMessageBox, QDialog,QFileDialog,QInputDialog
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
from test import *
from Management import Ui_Management

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

class Ui_processing(object):
    imagepath=None
    def management(self):
        self.Management = QtGui.QMainWindow()
        self.ui = Ui_Management()
        self.ui.setupUi(self.Management)
        self.Management.show()
  
        

    def changed(self, value):
        self.comboBox.clear()
        self.comboBox_3.clear()
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
   
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()

        print("combobox changed", value)
        for count in range(self.comboBox_2.count()):
         print(self.comboBox_2.itemText(count))
        print("Current index",value,"selection changed ",self.comboBox_2.currentText())
        section=[]
        query1=("select sec_name from tbl_section where ses_ID=(select ses_ID from tbl_session where ses_name=%s)")
        cursor.execute(query1,(self.comboBox_2.currentText()))
        records = cursor.fetchall()
        for row in records:
            section.append(str(row[0]))
            
        
        self.comboBox.addItems(section)

        
        query3 = ("select ses_ID from tbl_session where ses_name=%s")
        cursor.execute(query3,(self.comboBox_2.currentText()))
        rr=cursor.fetchall()
        print(rr)
        
        subject=[]
        query2=("select sub_name from tbl_subject where ses_ID=%s")
        cursor.execute(query2,(rr))
        records1 = cursor.fetchall()
        for row in records1:
            subject.append(str(row[0]))
            
        conn.commit()
        self.comboBox_3.addItems(subject)

    def uploadvideo(self):
        name=QFileDialog.getOpenFileName(QFileDialog(),"Open File","Facetest","Images(*.mp4)")
        imagepath = name
##        print(imagepath)
        return imagepath
    def processing(self):
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
   
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()
        query1=("insert into tbl_attendance(sec_ID,ses_ID,sub_ID) values ((select sec_ID from tbl_section where ses_ID=(select ses_ID from tbl_session where ses_name=%s) and sec_name=%s),(select ses_ID from tbl_session where ses_name=%s),(select sub_ID from tbl_subject where sub_name=%s))")
        cursor.execute(query1,(self.comboBox_2.currentText(),self.comboBox.currentText(),self.comboBox_2.currentText(),self.comboBox_3.currentText()))
        conn.commit()
        os.system("test1.py")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(709, 591)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(15, 11, 701, 531))
        self.graphicsView.setStyleSheet(_fromUtf8("background-color:\n"
"qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 129, 178, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.uploadvideo)
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 711, 81))
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setBackgroundBrush(brush)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.management)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 10, 91, 41))
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
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(490, 180, 141, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        ##############
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
        cur=conn.cursor()

        session=[]
        query1=("select ses_name from tbl_session")
        cur.execute(query1)
        records = cur.fetchall()
        for row in records:
            session.append(str(row[0]))
            
        conn.commit()
        self.comboBox_2.addItems(session)


        self.comboBox_2.currentIndexChanged.connect(self.changed)
        
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 420, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.clicked.connect(self.processing)
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
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(490, 230, 141, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 80, 311, 461))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("E:/final year projects/documents/nimradesigner/QTdesigner/hgyg.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(360, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(360, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 270, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(490, 270, 141, 31))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(360, 310, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(490, 320, 141, 31))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 2), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_5.setText(_translate("MainWindow", "Upload Video", None))
        self.label_2.setText(_translate("MainWindow", "Smart Classroom", None))
        self.pushButton_2.setText(_translate("MainWindow", "Management", None))
        self.pushButton_4.setText(_translate("MainWindow", "Add Subject", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "2016", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2017", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "2018", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "2019", None))
        self.pushButton_6.setText(_translate("MainWindow", "Start Processing", None))
        self.label_10.setText(_translate("MainWindow", "Processing", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "A", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "B", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "C", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "D", None))
        self.pushButton_3.setText(_translate("MainWindow", "Processing", None))
        self.pushButton.setText(_translate("MainWindow", "Registration", None))
        self.label_11.setText(_translate("MainWindow", "Select Session", None))
        self.label_8.setText(_translate("MainWindow", "Select Section", None))
        self.label_9.setText(_translate("MainWindow", "Select Subject", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Final Year Project", None))
        self.label_12.setText(_translate("MainWindow", "Select Date", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_processing()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

