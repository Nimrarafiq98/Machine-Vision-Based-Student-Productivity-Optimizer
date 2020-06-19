# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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

class Ui_report(object):
    def changed(self, value):
        self.comboBox_3.clear()
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
        cursor.execute(query1,(l))
        records = cursor.fetchall()
        for row in records:
            section.append(str(row[0]))
        subject=[]
        query3=("select sub_name from tbl_subject where ses_ID=(select ses_ID from tbl_session where ses_name=%s)")
        cursor.execute(query3,(self.comboBox_2.currentText()))
        ll = cursor.fetchall()
        for l in ll:
            subject.append(str(l[0]))
        
        conn.commit()
        self.comboBox.addItems(section)
        self.comboBox_3.addItems(subject)
    def search(self):
        conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
   
        
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
  ##      (select sec_ID from tbl_section where sec_name=self.combosession_2.currentText() and ses_ID=(select ses_ID from tbl_session where ses_name=%s))),(select sub_ID from tbl_subject where sub_name=%s),(select ses_ID from tbl_session where ses_name=%s)
        cursor=conn.cursor()

        query2=("select tbl_registration.reg_firstname,tbl_registration.reg_lastname,tbl_registration.reg_registration, tbl_attendance.att_attendance,tbl_attendance.att_productivity from tbl_registration join tbl_attendance on tbl_registration.reg_ID=tbl_attendance.reg_ID group by tbl_registration.reg_ID")
        cursor.execute(query2)
        result = cursor.fetchall()
        
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
           
            for column_number,data in enumerate(row_data):
                
                if data==1:
                    data="Present"
                self.tableWidget.setItem(row_number,column_number,QtGui.QTableWidgetItem(str(data)))
                                    

##        query3=("select att_attendance,att_productivity from tbl_attendance where sub_ID=(select max(sub_ID) from tbl_subject where sub_name=%s) and sec_ID=(select section_Id from new_section where section_name=%s) and ses_ID=(select ses_ID from tbl_session where ses_name=%s)")
##        cursor.execute(query3,(self.comboBox_3.currentText(),self.comboBox.currentText(),self.comboBox_2.currentText()))
##        result1 = cursor.fetchall()
##        self.tableWidget.setRowCount(0)
##
##                
##        for row_number, row_data in enumerate(result1):
##            self.tableWidget.insertRow(row_number)
## 
##           
##            for column_number,data in enumerate(row_data):
##
##                self.tableWidget.setItem(row_number+3,column_number,QtGui.QTableWidgetItem(str(data)))
##             

            
        conn.commit()
       ## self.tableWidget_2.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        ##self.tableWidget_2.itemDoubleClicked.connect(self.editItemsubject)


        

    def setupUi(self, report):
        report.setObjectName(_fromUtf8("report"))
        report.resize(770, 600)
        self.centralwidget = QtGui.QWidget(report)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-5, 1, 771, 581))
        self.graphicsView.setStyleSheet(_fromUtf8("background-color:\n"
"qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 129, 178, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(210, 140, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(210, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(440, 400, 75, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(120, 360, 511, 161))
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
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
        self.tableWidget.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 100, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Script"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(-10, 0, 771, 81))
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView_3.setBackgroundBrush(brush)
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
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
        self.pushButton_2.setGeometry(QtCore.QRect(540, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 20, 91, 41))
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
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(360, 150, 141, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
 ##################
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
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 190, 141, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(210, 220, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(360, 230, 141, 31))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(210, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(360, 270, 141, 21))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 2), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 310, 91, 41))
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
        #######
        self.pushButton_5.clicked.connect(self.search)
        report.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(report)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        report.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(report)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        report.setStatusBar(self.statusbar)

        self.retranslateUi(report)
        QtCore.QMetaObject.connectSlotsByName(report)

    def retranslateUi(self, report):
        report.setWindowTitle(_translate("report", "MainWindow", None))
        self.label_9.setText(_translate("report", "Select Session", None))
        self.label_11.setText(_translate("report", "Select Section", None))
        self.pushButton_10.setText(_translate("report", "Delete", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("report", "FirstName", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("report", "LastName", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("report", "Registration No.", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("report", "Attendance", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("report", "Status", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("report", "Report", None))
        self.pushButton.setText(_translate("report", "Registration", None))
        self.pushButton_3.setText(_translate("report", "Processing", None))
        self.label_2.setText(_translate("report", "Smart Classroom", None))
        self.pushButton_2.setText(_translate("report", "Management", None))
        self.pushButton_4.setText(_translate("report", "Add Subject", None))
        self.comboBox_2.setItemText(0, _translate("report", "2016", None))
        self.comboBox_2.setItemText(1, _translate("report", "2017", None))
        self.comboBox_2.setItemText(2, _translate("report", "2018", None))
        self.comboBox_2.setItemText(3, _translate("report", "2019", None))
        self.comboBox.setItemText(0, _translate("report", "A", None))
        self.comboBox.setItemText(1, _translate("report", "B", None))
        self.comboBox.setItemText(2, _translate("report", "C", None))
        self.comboBox.setItemText(3, _translate("report", "D", None))
        self.label_12.setText(_translate("report", "Select Subject", None))
        self.comboBox_3.setItemText(0, _translate("report", "Final year Project", None))
        self.label_13.setText(_translate("report", "Select Date", None))
        self.pushButton_5.setText(_translate("report", "OK", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    report = QtGui.QMainWindow()
    ui = Ui_report()
    ui.setupUi(report)
    report.show()
    sys.exit(app.exec_())

