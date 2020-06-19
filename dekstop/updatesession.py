# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updatesession.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox, QDialog,QFileDialog,QInputDialog
import pymysql
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

class Ui_updatesession(object):
    session=None
    section=None
    subject=None
    sessname=None
    def __init__(self, Parent=None,code=None,ses_name=None):
        if code=="session":
            self.session=Parent
            
        if(code=="section"):
            self.section=Parent
            self.sessname=ses_name
            print(self.sessname)
        if(code=="subject"):
            self.subject=Parent
            self.sessname=ses_name
            print(self.sessname)
    
        
    def messagebox(self,title,message):
        mess= QMessageBox.information(None,'Congrats' , 'updated successfully', QMessageBox.Ok,QMessageBox.Ok)
    def updatesession(self):
        
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
        st_email1=self.session
        print(st_email1)
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()

        query=("update tbl_session set ses_name= %s where ses_name=%s")
        data= cursor.execute(query,(self.lineEdit.text(),st_email1))
        
        if data:
            self.messagebox("congrats" , "updated successfully")
        conn.commit()

    def updatesection(self):
        
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
        st_email1=self.section
        st_section=self.sessname
     
        print(st_email1)
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()

        query=("update tbl_section set sec_name= %s where ses_ID=(select ses_ID from tbl_session where ses_name=%s) and sec_name=%s")
        data= cursor.execute(query,(self.lineEdit_2.text(),self.comboBox_2.currentText(),st_email1))
        
        if data:
            self.messagebox("congrats" , "updated successfully")
        conn.commit()
    def updatesubject(self):
        
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
        st_email1=self.subject
        st_section=self.sessname
     
        print(st_email1)
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()

        query=("update tbl_subject set sub_name= %s where ses_ID=(select ses_ID from tbl_session where ses_name=%s) and sub_name=%s")
        data= cursor.execute(query,(self.lineEdit_3.text(),self.comboBox_3.currentText(),st_email1))
        
        if data:
            self.messagebox("congrats" , "updated successfully")
        conn.commit()


    def setupUi(self, updatesession):
        updatesession.setObjectName(_fromUtf8("updatesession"))
        updatesession.resize(772, 587)
        self.centralwidget = QtGui.QWidget(updatesession)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-15, -19, 791, 561))
        self.graphicsView.setStyleSheet(_fromUtf8("background-color:\n"
"qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 129, 178, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
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
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 90, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 10, 781, 81))
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setBackgroundBrush(brush)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(420, 350, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 180, 120, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 510, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        ##################
        self.pushButton_8.clicked.connect(self.updatesubject)
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 320, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        ############
        self.pushButton_7.clicked.connect(self.updatesection)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(360, 420, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(280, 340, 441, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(530, 390, 141, 31))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
############
        self.comboBox_3.addItem(self.sessname)
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(530, 240, 141, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        print(self.sessname)
        self.comboBox_2.addItem(self.sessname)
##        self.comboBox_2.addItem(_fromUtf8(""))
##        self.comboBox_2.addItem(_fromUtf8(""))
##        self.comboBox_2.addItem(_fromUtf8(""))
##        self.comboBox_2.addItem(self.sess_name)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 30, 91, 41))
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
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 130, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(360, 230, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
               ###########
        self.pushButton_6.clicked.connect(self.updatesession)

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(360, 460, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(280, 190, 441, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(420, 200, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(360, 380, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(530, 430, 141, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 321, 451))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("E:/final year projects/documents/nimradesigner/QTdesigner/hgyg.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(530, 130, 141, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
              ############
        self.lineEdit.setText(self.session)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 280, 141, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
         ############
        self.lineEdit_2.setText(self.section)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 470, 141, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        ##############
        self.lineEdit_3.setText(self.subject)
        updatesession.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(updatesession)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        updatesession.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(updatesession)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        updatesession.setStatusBar(self.statusbar)

        self.retranslateUi(updatesession)
        QtCore.QMetaObject.connectSlotsByName(updatesession)

    def retranslateUi(self, updatesession):
        updatesession.setWindowTitle(_translate("updatesession", "MainWindow", None))
        self.label_2.setText(_translate("updatesession", "Smart Classroom", None))
        self.label_10.setText(_translate("updatesession", "Update Session", None))
        self.label_9.setText(_translate("updatesession", "Enter Section Name", None))
        self.label_12.setText(_translate("updatesession", "Update Subject", None))
        self.pushButton_8.setText(_translate("updatesession", "Update", None))
        self.pushButton_7.setText(_translate("updatesession", "Update", None))
        self.label_14.setText(_translate("updatesession", "Select Section", None))
##        self.comboBox_3.setItemText(0, _translate("updatesession", "2016", None))
##        self.comboBox_3.setItemText(1, _translate("updatesession", "2017", None))
##        self.comboBox_3.setItemText(2, _translate("updatesession", "2018", None))
##        self.comboBox_3.setItemText(3, _translate("updatesession", "2019", None))
##        self.comboBox_2.setItemText(0, _translate("updatesession", "2016", None))
##        self.comboBox_2.setItemText(1, _translate("updatesession", "2017", None))
##        self.comboBox_2.setItemText(2, _translate("updatesession", "2018", None))
##        self.comboBox_2.setItemText(3, _translate("updatesession", "2019", None))
        self.pushButton_4.setText(_translate("updatesession", "Add Subject", None))
        self.label_3.setText(_translate("updatesession", "Enter Session Name", None))
        self.label_8.setText(_translate("updatesession", "Select Session", None))
        self.pushButton_2.setText(_translate("updatesession", "Management", None))
        self.pushButton_6.setText(_translate("updatesession", "Update", None))
        self.pushButton.setText(_translate("updatesession", "Registration", None))
        self.label_15.setText(_translate("updatesession", "Enter Suject Name", None))
        self.label_11.setText(_translate("updatesession", "Update Section", None))
        self.label_13.setText(_translate("updatesession", "Select Session", None))
        self.comboBox.setItemText(0, _translate("updatesession", "A", None))
        self.comboBox.setItemText(1, _translate("updatesession", "B", None))
        self.comboBox.setItemText(2, _translate("updatesession", "C", None))
        self.comboBox.setItemText(3, _translate("updatesession", "D", None))
        self.pushButton_3.setText(_translate("updatesession", "Processing", None))
        self.label_4.setText(_translate("updatesession", "Smart Classroom", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    updatesession = QtGui.QMainWindow()
    ui = Ui_updatesession()
    ui.setupUi(updatesession)
    updatesession.show()
    sys.exit(app.exec_())

