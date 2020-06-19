# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymysql
from PyQt4.QtGui import QMessageBox, QDialog,QFileDialog,QInputDialog
from Addsubject import Ui_addsubject
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

class Ui_registration(object):
    def processing(self):
         self.MainWindow = QtGui.QMainWindow()
         self.ui = Ui_processing()
         self.ui.setupUi(self.MainWindow)
         self.MainWindow.show()    
    def messagebox(self,title,message):
        mess= QMessageBox.information(None,'Congrats' , 'successfully signed up', QMessageBox.Ok,QMessageBox.Ok)

    






    def uploadimage(self):
        name=QFileDialog.getOpenFileName(QFileDialog(),"Open File","E:\final year projects\Emotion Multiple Faces\Emotion Multiple Faces","Images(*.jpg *.png)")
        imagepath = name
        print(imagepath)
       
        self.label_10.setPixmap(QtGui.QPixmap(imagepath))

    def reg(self):
            
        st_firstname = self.lineEdit.text()
        st_lastname = self.lineEdit_2.text()
        st_registration = self.lineEdit_3.text()
        st_email = self.lineEdit_4.text()
        st_department = self.lineEdit_5.text()
        st_section = str(self.comboBox.currentText())
        st_session = str(self.comboBox_2.currentText())

##text = self.combo.currentText()
##        self.cursor.execute("INSERT INTO test (Blood) values('{}')".format(text))
        
##        st_section = self.comboBox.currentText()
##        st_session = self.comboBox_2.currenText()
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
        cur=conn.cursor()
        query=("insert into tbl_registration(reg_firstname,reg_lastname, reg_email ,reg_registration, reg_department,reg_session,reg_section) values (%s, %s,%s,%s,%s,(select ses_ID from tbl_session where ses_name=%s),(select sec_ID from tbl_section where sec_name=%s order by sec_ID desc limit 1))")
        data= cur.execute(query,(st_firstname, st_lastname,st_email,st_registration,st_department,st_session,st_section))
        conn.commit()
        
        
        
        if(data):
            self.messagebox("congrats" , "u r successfully signed up")
    def addsubje(self):
        self.addsubject = QtGui.QMainWindow()
        self.ui = Ui_addsubject()
        self.ui.setupUi(self.addsubject)
        self.addsubject.show()

    def changed(self, value):
        self.comboBox.clear()
        
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
   
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()

        print("combobox changed", value)
        for count in range(self.comboBox_2.count()):
         print(self.comboBox_2.itemText(count))
        print("Current index",value,"selection changed ",self.comboBox_2.currentText())
        query2=("select ses_ID from tbl_session where ses_name=%s")
        cursor.execute(query2,(self.comboBox_2.currentText()))
        l = cursor.fetchall()
        print(l)
        section=[]
        query1=("select sec_name from tbl_section where ses_id=(select ses_id from tbl_session where ses_name=%s)")
        cursor.execute(query1,(self.comboBox_2.currentText()))
        records = cursor.fetchall()
        for row in records:
            section.append(str(row[0]))
            
        conn.commit()
        self.comboBox.addItems(section)

    def setupUi(self, registration):
        registration.setObjectName(_fromUtf8("registration"))
        registration.resize(754, 618)
        self.centralwidget = QtGui.QWidget(registration)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 530, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        ##############
        self.pushButton_6.clicked.connect(self.reg)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 210, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(380, 330, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(500, 300, 131, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
##############
        
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 0, 741, 71))
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setBackgroundBrush(brush)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(380, 290, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(500, 340, 131, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
###########################
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
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 130, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 250, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 311, 501))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("E:/final year projects/documents/nimradesigner/QTdesigner/hgyg.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(60, 10, 701, 561))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color:rgb(85, 170, 255)"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 370, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
                ##################
        self.pushButton_5.clicked.connect(self.uploadimage)

        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        ##################
        self.pushButton_3.clicked.connect(self.processing)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)\n"
""))
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        ##################
        self.pushButton_4.clicked.connect(self.addsubje)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(640, 400, 101, 141))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(500, 140, 131, 31))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 180, 131, 31))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 220, 131, 31))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 260, 131, 31))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 380, 131, 31))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.graphicsView.raise_()
        self.pushButton_6.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.comboBox.raise_()
        self.graphicsView_2.raise_()
        self.label_9.raise_()
        self.comboBox_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.pushButton_5.raise_()
        self.pushButton_3.raise_()
        self.label_4.raise_()
        self.pushButton_4.raise_()
        self.label_10.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        registration.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(registration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        registration.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(registration)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        registration.setStatusBar(self.statusbar)

        self.retranslateUi(registration)
        QtCore.QMetaObject.connectSlotsByName(registration)

    def retranslateUi(self, registration):
        registration.setWindowTitle(_translate("registration", "MainWindow", None))
        self.pushButton_6.setText(_translate("registration", "Register", None))
        self.label_6.setText(_translate("registration", "Registration No.", None))
        self.label_8.setText(_translate("registration", "Session", None))
        self.comboBox.setItemText(0, _translate("registration", "A", None))
        self.comboBox.setItemText(1, _translate("registration", "B", None))
        self.comboBox.setItemText(2, _translate("registration", "C", None))
        self.comboBox.setItemText(3, _translate("registration", "D", None))
        self.label_9.setText(_translate("registration", "Section", None))
        self.comboBox_2.setItemText(0, _translate("registration", "2016", None))
        self.comboBox_2.setItemText(1, _translate("registration", "2017", None))
        self.comboBox_2.setItemText(2, _translate("registration", "2018", None))
        self.comboBox_2.setItemText(3, _translate("registration", "2019", None))
        self.label_2.setText(_translate("registration", "Smart Classroom", None))
        self.label_3.setText(_translate("registration", "FirstName", None))
        self.label_5.setText(_translate("registration", "Email", None))
        self.pushButton_2.setText(_translate("registration", "Management", None))
        self.pushButton.setText(_translate("registration", "Registration", None))
        self.label_7.setText(_translate("registration", "Department", None))
        self.pushButton_5.setText(_translate("registration", "Upload Image", None))
        self.pushButton_3.setText(_translate("registration", "Processing", None))
        self.label_4.setText(_translate("registration", "LastName", None))
        self.pushButton_4.setText(_translate("registration", "Add Subject", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    registration = QtGui.QMainWindow()
    ui = Ui_registration()
    ui.setupUi(registration)
    registration.show()
    sys.exit(app.exec_())

