# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Addsubject.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymysql
from PyQt4.QtGui import QMessageBox, QDialog,QFileDialog,QInputDialog
from PyQt4.QtCore import *
from PyQt4.QtGui import *
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

class Ui_addsubject(object):
    def processing(self):
         self.MainWindow = QtGui.QMainWindow()
         self.ui = Ui_processing()
         self.ui.setupUi(self.MainWindow)
         self.MainWindow.show()

##    def reg(self):
##        self.registration = QtGui.QMainWindow()
##        self.ui = Ui_registration()
##        self.ui.setupUi(self.registration)
##        self.registration.show()
##
##    def addsubject(self):
##        self.addsubject = QtGui.QMainWindow()
##        self.ui = Ui_addsubject()
##        self.ui.setupUi(self.addsubject)
##        self.addsubject.show()
##        
##    def manage(self):
##        self.Management = QtGui.QMainWindow()
##        self.ui = Ui_Management()
##        self.ui.setupUi(self.Management)
##        self.Management.show()


    def messagebox(self,title,message):
        mess= QMessageBox.information(None,'Congrats' , 'successfully signed up', QMessageBox.Ok,QMessageBox.Ok)
    def add(self):
        st_label = self.lineEdit.text()      
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")

        cur=conn.cursor()
        query=("insert into tbl_session(ses_name) values (%s)")
        data= cur.execute(query,(st_label))
        conn.commit()
        
        session=[]
        
        if(data):
            self.messagebox("congrats" , "u r successfully signed up")
        query1=("select ses_name from tbl_session")
        cur.execute(query1)
        records = cur.fetchall()
        for row in records:
            session.append(str(row[0]))
            
        conn.commit()
        self.comboBox_2.addItems(session)
        self.comboBox_3.addItems(session)


    def OKsubmit(self):
        st_firstname = self.lineEdit_2.text()
        
        session=[]
##text = self.combo.currentText()
##        self.cursor.execute("INSERT INTO test (Blood) values('{}')".format(text))
        
##        st_section = self.comboBox.currentText()
##        st_session = self.comboBox_2.currenText()
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
        cur=conn.cursor()
        query=("insert into tbl_section(sec_name,ses_ID) values (%s,(select ses_ID from tbl_session where ses_name=%s))")
        data= cur.execute(query,(st_firstname, self.comboBox_2.currentText()))
        conn.commit()
        
        
   
        if(data):
            self.messagebox("congrats" , "u r successfully signed up")
        query1=("select sec_name from tbl_section where ses_id=(select ses_id from tbl_session where ses_name=%s)")
        cur.execute(query1,(self.comboBox_3.currentText()))
        records = cur.fetchall()
        for row in records:
            session.append(str(row[0]))
            
        conn.commit()
        self.comboBox.addItems(session)
        
    


    def ad_subject(self):
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
   
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()
        query=("insert into tbl_subject(ses_ID,sub_name) values((select distinct ses_ID from tbl_session where ses_name=%s),%s)")
        data=cursor.execute(query,(self.comboBox_3.currentText(),self.lineEdit_3.text()))
 

        conn.commit()
        if(data):
            self.messagebox("congrats" , "u r successfully signed up")

    def changed(self, value):
        self.comboBox.clear()
        
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
   
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()

        print("combobox changed", value)
        for count in range(self.comboBox_3.count()):
         print(self.comboBox_3.itemText(count))
        print("Current index",value,"selection changed ",self.comboBox_3.currentText())
        query2=("select ses_ID from tbl_session where ses_name=%s")
        cursor.execute(query2,(self.comboBox_3.currentText()))
        l = cursor.fetchall()
        print(l)
        section=[]
        query1=("select sec_name from tbl_section where ses_id=(select ses_id from tbl_session where ses_name=%s)")
        cursor.execute(query1,(self.comboBox_3.currentText()))
        records = cursor.fetchall()
        for row in records:
            section.append(str(row[0]))
            
        conn.commit()
        self.comboBox.addItems(section)

        

    def setupUi(self, addsubject):
        addsubject.setObjectName(_fromUtf8("addsubject"))
        addsubject.resize(726, 600)
        addsubject.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 255)qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255))"))
        self.centralwidget = QtGui.QWidget(addsubject)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-5, -9, 731, 561))
        self.graphicsView.setStyleSheet(_fromUtf8("background-color:\n"
"qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 129, 178, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 721, 81))
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setBackgroundBrush(brush)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        #############
  ##      self.pushButton_2.clicked.coonect(self.manage)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 20, 91, 41))
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
        ###############
      ##  self.pushButton_4.clicked.coonect(self.addsubject)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(120, 190, 120, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(540, 250, 141, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        ##################
        

        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        ################
        self.pushButton_6.clicked.connect(self.add)
        ############
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

        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 140, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(430, 100, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 240, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(540, 440, 141, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
  
        ################
       
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.processing)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ############
     ##   self.pushButton.clicked.coonect(self.reg)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 80, 311, 471))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("E:/final year projects/documents/nimradesigner/QTdesigner/hgyg.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(310, 200, 421, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 210, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(370, 290, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 330, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        ###############
        self.pushButton_7.clicked.connect(self.OKsubmit)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(310, 350, 421, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(430, 360, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(370, 390, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(370, 430, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(540, 400, 141, 31))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
     
        ##########
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
        self.comboBox_3.addItems(session)

        self.comboBox_3.currentIndexChanged.connect(self.changed)

        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(370, 470, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(450, 520, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        ###################
        self.pushButton_8.clicked.connect(self.ad_subject)
        #############
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 140, 141, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(540, 290, 141, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(540, 480, 141, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        addsubject.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(addsubject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        addsubject.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(addsubject)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        addsubject.setStatusBar(self.statusbar)

        self.retranslateUi(addsubject)
        QtCore.QMetaObject.connectSlotsByName(addsubject)

    def retranslateUi(self, addsubject):
        addsubject.setWindowTitle(_translate("addsubject", "MainWindow", None))
        self.label_2.setText(_translate("addsubject", "Smart Classroom", None))
        self.pushButton_2.setText(_translate("addsubject", "Management", None))
        self.pushButton_4.setText(_translate("addsubject", "Add Subject", None))
##        self.comboBox_2.setItemText(0, _translate("addsubject", "2016", None))
##        self.comboBox_2.setItemText(1, _translate("addsubject", "2017", None))
##        self.comboBox_2.setItemText(2, _translate("addsubject", "2018", None))
##        self.comboBox_2.setItemText(3, _translate("addsubject", "2019", None))
        self.pushButton_6.setText(_translate("addsubject", "Add", None))
        self.label_3.setText(_translate("addsubject", "Enter Session Name", None))
        self.label_10.setText(_translate("addsubject", "Add Session", None))
        self.label_8.setText(_translate("addsubject", "Select Session", None))
        self.comboBox.setItemText(0, _translate("addsubject", "A", None))
        self.comboBox.setItemText(1, _translate("addsubject", "B", None))
        self.comboBox.setItemText(2, _translate("addsubject", "C", None))
        self.comboBox.setItemText(3, _translate("addsubject", "D", None))
        self.pushButton_3.setText(_translate("addsubject", "Processing", None))
        self.pushButton.setText(_translate("addsubject", "Registration", None))
        self.label_11.setText(_translate("addsubject", "Add Section", None))
        self.label_9.setText(_translate("addsubject", "Enter Section Name", None))
        self.pushButton_7.setText(_translate("addsubject", "Add", None))
        self.label_12.setText(_translate("addsubject", "Add Subject", None))
        self.label_13.setText(_translate("addsubject", "Select Session", None))
        self.label_14.setText(_translate("addsubject", "Select Section", None))
##        self.comboBox_3.setItemText(0, _translate("addsubject", "2016", None))
##        self.comboBox_3.setItemText(1, _translate("addsubject", "2017", None))
##        self.comboBox_3.setItemText(2, _translate("addsubject", "2018", None))
##        self.comboBox_3.setItemText(3, _translate("addsubject", "2019", None))
        self.label_15.setText(_translate("addsubject", "Enter Suject Name", None))
        self.pushButton_8.setText(_translate("addsubject", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    addsubject = QtGui.QMainWindow()
    ui = Ui_addsubject()
    ui.setupUi(addsubject)
    addsubject.show()
    sys.exit(app.exec_())

