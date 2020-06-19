# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updatestd.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymysql
from PyQt4.QtGui import QMessageBox, QDialog,QFileDialog,QInputDialog

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

class Ui_updatestd(object):
    data=None
    info=[]
    firstname=None
    lastname=None
    email=None
    department=None
    def __init__(self, parent = None):
        self.data=parent
        print(parent)
        print("ff")
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
        cursor=conn.cursor()
##            query2=self.tableWidget_4
        query=("select reg_firstname,reg_lastname,reg_email,reg_department from tbl_registration where reg_registration=%s")
        
        cursor.execute(query,(str(parent)))
        result=cursor.fetchall()
        
       
        self.firstname=result[0][0]
        self.lastname=result[0][1]
        self.email=result[0][2]
        self.department=result[0][3]
        conn.commit()
    def messagebox(self,title,message):
        mess= QMessageBox.information(None,'Congrats' , 'updated successfully', QMessageBox.Ok,QMessageBox.Ok)

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
        query1=("select sec_name from tbl_section where ses_ID=%s")
        cursor.execute(query1,(value+1))
        records = cursor.fetchall()
        for row in records:
            section.append(str(row[0]))
            
        conn.commit()
        self.comboBox.addItems(section)
    def updated(self):
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
        st_email1=self.lineEdit_4.text()
        print(st_email1)
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()

        query=("update tbl_registration set reg_firstname= %s,reg_lastname=%s,reg_email=%s,reg_session=(select ses_ID from tbl_session where ses_name=%s),reg_section=(select section_id from new_section where section_name=%s), reg_department=%s,reg_registration=%s where reg_email=%s ")
        data= cursor.execute(query,(self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_4.text(),self.comboBox_2.currentText(),self.comboBox.currentText(),self.lineEdit_5.text(),self.lineEdit_3.text(),st_email1))
        
        if data:
            self.messagebox("congrats" , "updated successfully")
        conn.commit()

    def setupUi(self, updatestd):
        updatestd.setObjectName(_fromUtf8("updatestd"))
        updatestd.resize(765, 575)
        updatestd.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(updatestd)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-25, -19, 791, 571))
        self.graphicsView.setStyleSheet(_fromUtf8("background-color:\n"
"qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 129, 178, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 20, 771, 81))
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setBackgroundBrush(brush)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 40, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 40, 91, 41))
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
        self.frame.setGeometry(QtCore.QRect(120, 190, 120, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(500, 380, 141, 31))
        ###############
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
        self.pushButton_6.setGeometry(QtCore.QRect(380, 460, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        #############
        self.pushButton_6.clicked.connect(self.updated)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(400, 120, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(390, 330, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 290, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 410, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(390, 370, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(500, 340, 141, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 100, 341, 451))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("E:/final year projects/documents/nimradesigner/QTdesigner/hgyg.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 210, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(500, 180, 141, 31))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        ##################
        self.lineEdit.setText(self.firstname)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 220, 141, 31))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        #############
        self.lineEdit_2.setText(self.lastname)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 260, 141, 31))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        #########
         #########
        self.lineEdit_3.setText(self.data)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 300, 141, 31))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        #################
        self.lineEdit_4.setText(self.email)
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 420, 141, 31))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        ##############3
        self.lineEdit_5.setText(self.department)
        updatestd.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(updatestd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        updatestd.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(updatestd)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        updatestd.setStatusBar(self.statusbar)

        self.retranslateUi(updatestd)
        QtCore.QMetaObject.connectSlotsByName(updatestd)

    def retranslateUi(self, updatestd):
        updatestd.setWindowTitle(_translate("updatestd", "MainWindow", None))
        self.label_6.setText(_translate("updatestd", "Registration No.", None))
        self.label_2.setText(_translate("updatestd", "Smart Classroom", None))
        self.pushButton_2.setText(_translate("updatestd", "Management", None))
        self.pushButton_4.setText(_translate("updatestd", "Add Subject", None))
        self.comboBox_2.setItemText(0, _translate("updatestd", "2016", None))
        self.comboBox_2.setItemText(1, _translate("updatestd", "2017", None))
        self.comboBox_2.setItemText(2, _translate("updatestd", "2018", None))
        self.comboBox_2.setItemText(3, _translate("updatestd", "2019", None))
        self.pushButton_6.setText(_translate("updatestd", "Update", None))
        self.label_3.setText(_translate("updatestd", "FirstName", None))
        self.label_10.setText(_translate("updatestd", "Update Student", None))
        self.label_9.setText(_translate("updatestd", "Section", None))
        self.label_5.setText(_translate("updatestd", "Email", None))
        self.label_7.setText(_translate("updatestd", "Department", None))
        self.label_8.setText(_translate("updatestd", "Session", None))
        self.comboBox.setItemText(0, _translate("updatestd", "A", None))
        self.comboBox.setItemText(1, _translate("updatestd", "B", None))
        self.comboBox.setItemText(2, _translate("updatestd", "C", None))
        self.comboBox.setItemText(3, _translate("updatestd", "D", None))
        self.pushButton_3.setText(_translate("updatestd", "Processing", None))
        self.pushButton.setText(_translate("updatestd", "Registration", None))
        self.label_4.setText(_translate("updatestd", "LastName", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    updatestd = QtGui.QMainWindow()
    ui = Ui_updatestd()
    ui.setupUi(updatestd)
    updatestd.show()
    sys.exit(app.exec_())

