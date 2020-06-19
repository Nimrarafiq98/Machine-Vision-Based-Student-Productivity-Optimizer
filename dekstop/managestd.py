# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managestd.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymysql
from updatestd import Ui_updatestd
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

class Ui_MainWindow1(object):
    
    def messagebox(self,title,message):
        mess= QMessageBox.information(None,'Congrats' , 'Deleted Successfully', QMessageBox.Ok,QMessageBox.Ok)

    def editItem(self,clicked):
        selected = self.tableWidget.currentRow()
        self.row=self.tableWidget.item(0,2).text()
        
##        sell   =self.tableWidget_4.selectedRows(selected)
        
       ## name = self.tableWidget_4.index(selected, 0)
        
        if clicked.column() == 3:
            conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
            cur=conn.cursor()

            self.tableWidget.removeRow(selected)
            query=("delete from tbl_registration where reg_registration=%s")
            data= cur.execute(query,(self.row))
            conn.commit()
            if (data):
                self.messagebox("congrats" , "Deleted Successfully")



        if clicked.column() == 4:
            self.updatestd = QtGui.QMainWindow()
            
            self.ui = Ui_updatestd(self.row)
            
            self.ui.setupUi(self.updatestd)
            self.updatestd.show()
    def changed(self, value):
        self.comboBox.clear()
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
   
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()

        
        for count in range(self.comboBox_2.count()):
         print(self.comboBox_2.itemText(count))
       
        query2=("select ses_ID from tbl_session where ses_name=%s")
        cursor.execute(query2,(self.comboBox_2.currentText()))
        l = cursor.fetchall()
        
        section=[]
        query1=("select sec_name from tbl_section where ses_ID=%s")
        cursor.execute(query1,(l))
        records = cursor.fetchall()
        for row in records:
            section.append(str(row[0]))
            
        conn.commit()
        self.comboBox.addItems(section)

    def search(self):
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
   
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()

        query2=("select reg_firstname,reg_lastname,reg_registration from tbl_registration where reg_session=(select ses_ID from tbl_session where ses_name=%s) and reg_section=(select sec_ID from tbl_section where ses_ID=(select ses_ID from tbl_session where ses_name=%s) and sec_name=%s)")
        cursor.execute(query2,(self.comboBox_2.currentText(),self.comboBox_2.currentText(),self.comboBox.currentText()))
        result = cursor.fetchall()
 
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
 
           
            for column_number,data in enumerate(row_data):

                self.tableWidget.setItem(row_number,column_number,QtGui.QTableWidgetItem(str(data)))
                self.tableWidget.setItem(row_number,column_number+1,QtGui.QTableWidgetItem("Delete"))
                self.tableWidget.setItem(row_number,column_number+2,QtGui.QTableWidgetItem("Update"))
                self.tableWidget.item(row_number,column_number+2).setBackground(QtGui.QColor(124,124,125))
                self.tableWidget.item(row_number,column_number+1).setBackground(QtGui.QColor(124,124,125))
                

            
        conn.commit()
       ## self.tableWidget_2.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        ##self.tableWidget_2.itemDoubleClicked.connect(self.editItemsubject)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(5, 11, 771, 561))
        self.graphicsView.setStyleSheet(_fromUtf8("background-color:\n"
"qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 129, 178, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 10, 761, 71))
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_2.setBackgroundBrush(brush)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 30, 91, 41))
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
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(260, 100, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 310, 521, 221))
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        ###############
        self.tableWidget.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidget.itemDoubleClicked.connect(self.editItem)

        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 160, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 170, 141, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
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

        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 220, 141, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
##        self.comboBox.addItem(_fromUtf8(""))
##        self.comboBox.addItem(_fromUtf8(""))
##        self.comboBox.addItem(_fromUtf8(""))
##        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 260, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.search)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label_10.setText(_translate("MainWindow", "Manage Students", None))
        self.pushButton_3.setText(_translate("MainWindow", "Processing", None))
        self.pushButton.setText(_translate("MainWindow", "Registration", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "FirstName", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LastName", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Registration No.", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Delete", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Update", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("MainWindow", "Select Session", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "2016", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2017", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "2018", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "2019", None))
        self.label_11.setText(_translate("MainWindow", "Select Section", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "A", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "B", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "C", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "D", None))
        self.pushButton_5.setText(_translate("MainWindow", "Search", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

