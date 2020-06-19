# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymysql
from PyQt4.QtGui import QMessageBox, QDialog,QFileDialog,QInputDialog
from updatesession import Ui_updatesession
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

    def messagebox(self,title,message):
        mess= QMessageBox.information(None,'Congrats' , 'Deleted Successfully', QMessageBox.Ok,QMessageBox.Ok)

    def editItem(self,clicked):
        self.code="session"
        selected = self.tableWidget_4.currentRow()
        self.row=self.tableWidget_4.item(selected,0).text()
        print(self.row)
        if clicked.column() == 1:
            self.tableWidget_4.removeRow(selected)
            self.messagebox("congrats" , "Deleted Successfully")
##            print("delete")
            conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
####        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
            cursor=conn.cursor()
            query=("Delete from tbl_session where ses_name=%s")
            cursor.execute(query,(self.row))
 ##           result=cursor.fetchall()
            query=("select ses_name,sec_name from tbl_session join tbl_section where tbl_session.ses_ID=tbl_section.ses_ID")
            cursor.execute(query)
            result=cursor.fetchall()
            self.tableWidget_3.setRowCount(0)
        
            for row_number, row_data in enumerate(result):
                self.tableWidget_3.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tableWidget_3.setItem(row_number,column_number,QtGui.QTableWidgetItem(str(data)))
                    self.tableWidget_3.setItem(row_number,column_number+1,QtGui.QTableWidgetItem("Delete"))
                    self.tableWidget_3.setItem(row_number,column_number+2,QtGui.QTableWidgetItem("Update"))
                    self.tableWidget_3.item(row_number,column_number+2).setBackground(QtGui.QColor(124,124,125))
                    self.tableWidget_3.item(row_number,column_number+1).setBackground(QtGui.QColor(124,124,125))
                    

            self.tableWidget_3.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
           
##  

            query=("select ses_name,sub_name from tbl_session join tbl_subject where tbl_session.ses_ID=tbl_subject.ses_ID")
            cursor.execute(query)
            result=cursor.fetchall()
            self.tableWidget_2.setRowCount(0)
            
            for row_number, row_data in enumerate(result):
                self.tableWidget_2.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.tableWidget_2.setItem(row_number,column_number,QtGui.QTableWidgetItem(str(data)))
                    self.tableWidget_2.setItem(row_number,column_number+1,QtGui.QTableWidgetItem("Delete"))
                    self.tableWidget_2.setItem(row_number,column_number+2,QtGui.QTableWidgetItem("Update"))
                    self.tableWidget_2.item(row_number,column_number+2).setBackground(QtGui.QColor(124,124,125))
                    self.tableWidget_2.item(row_number,column_number+1).setBackground(QtGui.QColor(124,124,125))
            self.tableWidget_3.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
            conn.commit()
        if clicked.column() == 2:
            self.updatesession = QtGui.QMainWindow()
            self.ui = Ui_updatesession(self.row,self.code)
            self.ui.setupUi(self.updatesession)
            self.updatesession.show()



    def editItemsubject(self,clicked):
        self.code="subject"
        selected = self.tableWidget_2.currentRow()
        self.row=self.tableWidget_2.item(selected,1).text()
        self.session=self.tableWidget_2.item(selected,0).text()
        print(self.row)
        if clicked.column() == 2:
            self.tableWidget_2.removeRow(selected)
            self.messagebox("congrats" , "Deleted Successfully")
##            print("delete")
            conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
####        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
            cursor=conn.cursor()
            query=("Delete from tbl_subject where sub_name=%s and ses_ID=(select ses_ID from tbl_session where ses_name=%s)")
            cursor.execute(query,(self.row,self.session))
##            result=cursor.fetchall()
            conn.commit()
##


        if clicked.column() == 3:
            self.updatesession = QtGui.QMainWindow()
            self.ui = Ui_updatesession(self.row,self.code,self.session)
            self.ui.setupUi(self.updatesession)
            self.updatesession.show()


        
    def editItemsection(self,clicked):
        selected = self.tableWidget_3.currentRow()
        self.row=self.tableWidget_3.item(selected,1).text()
        self.ses_name=self.tableWidget_3.item(selected,0).text()
     
        self.code="section"
       
        if clicked.column() == 2:
            self.tableWidget_3.removeRow(selected)
            self.messagebox("congrats" , "Deleted Successfully")
##            print("delete")
            conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
####        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
            cursor=conn.cursor()
            query=("Delete from tbl_section where sec_name=%s and ses_ID=(select ses_ID from tbl_session where ses_name=%s)")
            cursor.execute(query,(self.row,self.code))
##            result=cursor.fetchall()
            conn.commit()
##


        if clicked.column() == 3:
            self.updatesession = QtGui.QMainWindow()
            self.ui = Ui_updatesession(self.row,self.code,self.ses_name)
            self.ui.setupUi(self.updatesession)
            self.updatesession.show()
 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(725, 611)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-5, -9, 731, 641))
        self.graphicsView.setStyleSheet(_fromUtf8("background-color:\n"
"qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 129, 178, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(100, 110, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(0, 10, 721, 81))
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_3.setBackgroundBrush(brush)
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
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
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(610, 190, 75, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
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
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(510, 220, 75, 23))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(610, 250, 75, 23))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(610, 280, 75, 23))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(510, 280, 75, 23))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_14 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(610, 220, 75, 23))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(510, 190, 75, 23))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_17 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(510, 250, 75, 23))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.tableWidget_2 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(220, 390, 321, 161))
        self.tableWidget_2.setRowCount(3)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))

###########################
        
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, item)

        #####################
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
        cursor=conn.cursor()
        query=("select ses_name,sub_name from tbl_session join tbl_subject where tbl_session.ses_ID=tbl_subject.ses_ID")
        cursor.execute(query)
        result=cursor.fetchall()
        self.tableWidget_2.setRowCount(0)
       
        
        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number,column_number,QtGui.QTableWidgetItem(str(data)))
                self.tableWidget_2.setItem(row_number,column_number+1,QtGui.QTableWidgetItem("Delete"))
                self.tableWidget_2.setItem(row_number,column_number+2,QtGui.QTableWidgetItem("Update"))
                self.tableWidget_2.item(row_number,column_number+2).setBackground(QtGui.QColor(124,124,125))
                self.tableWidget_2.item(row_number,column_number+1).setBackground(QtGui.QColor(124,124,125))
                

            
        conn.commit()
        self.tableWidget_2.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidget_2.itemDoubleClicked.connect(self.editItemsubject)


#################
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(610, 190, 75, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_18 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(510, 250, 75, 23))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.pushButton_20 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(610, 220, 75, 23))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.pushButton_21 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(610, 250, 75, 23))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.pushButton_22 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(610, 280, 75, 23))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.pushButton_23 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(510, 280, 75, 23))
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.tableWidget_3 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(380, 160, 321, 161))
        self.tableWidget_3.setRowCount(4)
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, item)
        ###################3
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
        cursor=conn.cursor()
        query=("select ses_name,sec_name from tbl_session join tbl_section where tbl_session.ses_ID=tbl_section.ses_ID")
        cursor.execute(query)
        result=cursor.fetchall()
        self.tableWidget_3.setRowCount(0)
        
        for row_number, row_data in enumerate(result):
            self.tableWidget_3.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget_3.setItem(row_number,column_number,QtGui.QTableWidgetItem(str(data)))
                self.tableWidget_3.setItem(row_number,column_number+1,QtGui.QTableWidgetItem("Delete"))
                self.tableWidget_3.setItem(row_number,column_number+2,QtGui.QTableWidgetItem("Update"))
                self.tableWidget_3.item(row_number,column_number+2).setBackground(QtGui.QColor(124,124,125))
                self.tableWidget_3.item(row_number,column_number+1).setBackground(QtGui.QColor(124,124,125))
                

            
        conn.commit()
        self.tableWidget_3.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidget_3.itemDoubleClicked.connect(self.editItemsection)
###########
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 110, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(270, 350, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.tableWidget_4 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(30, 160, 321, 161))
        self.tableWidget_4.setRowCount(4)
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(3, 0, item)
        

#######################
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
        cursor=conn.cursor()
        query=("select ses_name from tbl_session")
        cursor.execute(query)
        result=cursor.fetchall()
        self.tableWidget_4.setRowCount(0)
        
        for row_number, row_data in enumerate(result):
            self.tableWidget_4.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget_4.setItem(row_number,column_number,QtGui.QTableWidgetItem(str(data)))
                self.tableWidget_4.setItem(row_number,column_number+1,QtGui.QTableWidgetItem("Delete"))
                self.tableWidget_4.setItem(row_number,column_number+2,QtGui.QTableWidgetItem("Update"))
                self.tableWidget_4.item(row_number,column_number+2).setBackground(QtGui.QColor(124,124,125))
                self.tableWidget_4.item(row_number,column_number+1).setBackground(QtGui.QColor(124,124,125))
                

            
        conn.commit()
        self.tableWidget_4.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidget_4.itemDoubleClicked.connect(self.editItem)
##        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_10.setText(_translate("MainWindow", "Manage Sessions", None))
        self.pushButton.setText(_translate("MainWindow", "Registration", None))
        self.pushButton_8.setText(_translate("MainWindow", "Update", None))
        self.pushButton_3.setText(_translate("MainWindow", "Processing", None))
        self.label_2.setText(_translate("MainWindow", "Smart Classroom", None))
        self.pushButton_2.setText(_translate("MainWindow", "Management", None))
        self.pushButton_4.setText(_translate("MainWindow", "Add Subject", None))
        self.pushButton_9.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_13.setText(_translate("MainWindow", "Update", None))
        self.pushButton_12.setText(_translate("MainWindow", "Update", None))
        self.pushButton_11.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_14.setText(_translate("MainWindow", "Update", None))
        self.pushButton_15.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_17.setText(_translate("MainWindow", "Delete", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Session Name", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", " Subject Name", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Delete", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Update", None))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton_10.setText(_translate("MainWindow", "Update", None))
        self.pushButton_18.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_20.setText(_translate("MainWindow", "Update", None))
        self.pushButton_21.setText(_translate("MainWindow", "Update", None))
        self.pushButton_22.setText(_translate("MainWindow", "Update", None))
        self.pushButton_23.setText(_translate("MainWindow", "Delete", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Session Name", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", " Section Name", None))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Delete", None))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Update", None))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_11.setText(_translate("MainWindow", "Manage Sections", None))
        self.label_12.setText(_translate("MainWindow", "Manage Subjects", None))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", " Session Name", None))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Delete", None))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Update", None))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

