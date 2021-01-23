# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create5.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QInputDialog,QMessageBox
import CreateShare as cs
from PyQt5.QtGui import QIcon
import CheckFile as cf
import CheckShare as csh

class Ui_Form(object):
    def __init__(self,obc):
        self.obc =obc


    def setupUi(self, Form):
        self.L=[None]*6
        self.User = ['None']*4
        self.count =0
        Form.setObjectName("Form")
        Form.resize(574, 704)
        Form.setStyleSheet("background-color: rgb(204, 153, 255);")
        # 170, 230, 120
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 660, 93, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"font: 75 11pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(self.SendBackend)


        self.labeldynamic = QtWidgets.QLabel(Form)
        self.labeldynamic.setGeometry(QtCore.QRect(180, 70, 250, 21))
        self.labeldynamic.setScaledContents(False)
        self.labeldynamic.setObjectName("labeldynamic")


        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 160, 441, 81))
        self.widget.setObjectName("widget")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.label_9.setStyleSheet("font: 12pt \"Nirmala UI\";")
        self.label_9.setObjectName("label_9")
        self.radioButton_13 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_13.setGeometry(QtCore.QRect(130, 40, 95, 20))
        #self.radioButton_13.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_13.clicked.connect(self.on_text_changed)
        self.radioButton_14 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_14.setGeometry(QtCore.QRect(270, 40, 95, 20))
        #self.radioButton_14.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_14.clicked.connect(self.on_text_changed)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(20, 260, 451, 80))
        self.widget_2.setObjectName("widget_2")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(20, 30, 111, 31))
        self.label_10.setObjectName("label_10")
        self.radioButton_15 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_15.setGeometry(QtCore.QRect(140, 40, 95, 20))
        #self.radioButton_15.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_15.clicked.connect(self.on_text_changed)
        self.radioButton_16 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_16.setGeometry(QtCore.QRect(270, 40, 95, 20))
        #self.radioButton_16.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_16.setObjectName("radioButton_16")
        self.radioButton_16.clicked.connect(self.on_text_changed)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(20, 360, 411, 80))
        self.widget_3.setObjectName("widget_3")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 121, 31))
        self.label_11.setObjectName("label_11")
        self.radioButton_17 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_17.setGeometry(QtCore.QRect(140, 30, 95, 20))
        #self.radioButton_17.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_17.setObjectName("radioButton_17")
        self.radioButton_17.clicked.connect(self.on_text_changed)
        self.radioButton_18 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_18.setGeometry(QtCore.QRect(260, 30, 95, 20))
        #self.radioButton_18.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_18.setObjectName("radioButton_18")
        self.radioButton_18.clicked.connect(self.on_text_changed)
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(30, 450, 411, 80))
        self.widget_4.setObjectName("widget_4")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.label_12.setObjectName("label_12")
        self.radioButton_19 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_19.setGeometry(QtCore.QRect(140, 30, 95, 20))
        #self.radioButton_19.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_19.setObjectName("radioButton_19")
        self.radioButton_19.clicked.connect(self.on_text_changed)
        self.radioButton_20 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_20.setGeometry(QtCore.QRect(270, 30, 95, 20))
        #self.radioButton_20.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_20.setObjectName("radioButton_20")
        self.radioButton_20.clicked.connect(self.on_text_changed)
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setGeometry(QtCore.QRect(200, 530, 120, 111))
        self.widget_5.setObjectName("widget_5")
        self.widget1 = QtWidgets.QWidget(self.widget_5)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 83, 100))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget1)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 540, 121, 51))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 291, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit.textChanged.connect(self.on_text_changed)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 131, 21))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        #self.labeldynamic = QtWidgets.QLabel(Form)
        #self.labeldynamic.setGeometry(QtCore.QRect(180, 70, 130, 21))
        #self.labeldynamic.setScaledContents(False)
        #self.labeldynamic.setObjectName("labeldynamic")



        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 62, 24))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.label_m = QtWidgets.QLabel(Form)
        self.label_m.setGeometry(QtCore.QRect(190, 110, 241, 23))

        self.label_m.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")

        self.label_m.setObjectName("label_m")
        # self.label_m.textChanged.connect(self.on_text_changed)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setCheckable(True)
        self.pushButton.setGeometry(QtCore.QRect(400, 105, 180, 28))
        self.pushButton.setStyleSheet("background-color: rgb(85, 0, 0);\n"
"font: 11pt \"Times New Roman\";\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_text_changed)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Create SambaShare"))
        Form.setWindowIcon(QIcon('team2.png'))
        Form.setWindowOpacity(0.95)
        self.pushButton_2.setText(_translate("Form", "Submit"))

        #self.pushButton_2.connect(self.warning_msg)
        
        #self.pushButton_2.clicked.connect(self.GetShareName)
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Public:</span></p></body></html>"))
        self.radioButton_13.setText(_translate("Form", "Yes"))
        self.radioButton_13.clicked.connect(self.check)
        #self.radioButton_13.textChanged.connect(self.on_text_changed)
        self.radioButton_14.setText(_translate("Form", "No"))
        self.radioButton_14.clicked.connect(self.check)
        #self.radioButton_14.textChanged.connect(self.on_text_changed)
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Writeable: </span></p></body></html>"))
        self.radioButton_15.setText(_translate("Form", "Yes"))
        self.radioButton_15.clicked.connect(self.check)
        self.radioButton_16.setText(_translate("Form", "No"))
        self.radioButton_16.clicked.connect(self.check)
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Browsable:</span></p></body></html>"))
        self.radioButton_17.setText(_translate("Form", "Yes"))
        self.radioButton_17.clicked.connect(self.check)
        self.radioButton_18.setText(_translate("Form", "No"))
        self.radioButton_18.clicked.connect(self.check)
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ReadOnly:</span></p></body></html>"))
        self.radioButton_19.setText(_translate("Form", "yes"))
        self.radioButton_19.clicked.connect(self.check)
        self.radioButton_20.setText(_translate("Form", "No"))
        self.radioButton_20.clicked.connect(self.check)
        self.checkBox.setText(_translate("Form", "Amol"))
        self.checkBox.stateChanged.connect(self.GetCheckItem)
        self.checkBox_2.setText(_translate("Form", "Parth"))
        self.checkBox_2.stateChanged.connect(self.GetCheckItem)
        self.checkBox_4.setText(_translate("Form", "Josh"))
        self.checkBox_4.stateChanged.connect(self.GetCheckItem)
        self.checkBox_3.setText(_translate("Form", "Manoj"))
        self.checkBox_3.stateChanged.connect(self.GetCheckItem)
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">UserList</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Share Name: </span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Path   :</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Browse Path"))
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.label_m.setText(_translate("Form", "Empty Path"))


        self.labeldynamic.setText(_translate("Form","<html><head/><body><p><span style=\" color:#0000ff;\">Enter Share name</span></p></body></html>"))

        #self.labeldynamic.setText(_translate("Form","<html><head/><body><p><span style=\" color:#ff0000;\">No Such ShareName</span></p></body></html>"))

    def on_text_changed(self):

        _translate = QtCore.QCoreApplication.translate

        if(cf.fileexists()):
            self.sharename2 = self.lineEdit.text()
            if(csh.exists(self.sharename2)):
                self.labeldynamic.setText(_translate("Form","<html><head/><body><p><span style=\" color:#ff0000;\">ShareName not available</span></p></body></html>"))
            else:
                self.labeldynamic.setText(_translate("Form","<html><head/><body><p><span style=\" color:#0000ff;\">ShareName available</span></p></body></html>"))
        else:
            self.labeldynamic.setText(_translate("Form","<html><head/><body><p><span style=\" color:#ff0000;\">smb.conf file missing.</span></p></body></html>"))
            QMessageBox.warning(self.obc, "Warning","smb.conf file missing.")
            self.obc.close()

        self.pushButton_2.setEnabled(bool(self.lineEdit.text())\
         and (self.radioButton_13.isChecked() or self.radioButton_14.isChecked()) \
         and (self.radioButton_15.isChecked() or self.radioButton_16.isChecked()) \
         and (self.radioButton_17.isChecked() or self.radioButton_18.isChecked()) \
         and (self.radioButton_19.isChecked() or self.radioButton_20.isChecked())\
         and (self.pushButton.isChecked()) and (not self.label_m.text() == ""))

    #def warning_msg(self):
        



    def pushButton_handler(self):
        print("Button Pressed")
        self.open_dialog_box()
    def open_dialog_box(self):
        #filename = QFileDialog.getOpenFileName()
        self.filename=QFileDialog.getExistingDirectory()
        print("Path: {}".format(self.filename))
        self.label_m.setText(self.filename)
       # print(type(filename))
    def check(self):
        #if self.radioButton_15.isChecked():
         #   self.L
        if self.radioButton_13.isChecked():
            print('Yes')
            self.L[2]=bool(1)
            self.flag = 1
            self.widget1.setEnabled(False)
        if self.radioButton_14.isChecked():
            print('NO')
            self.flag = 0
            self.L[2]=(bool(0))
            self.widget1.setEnabled(True)
        if self.radioButton_15.isChecked():
            print('Yes')
            #self.flag = 0
            self.L[3]=(bool(1))
            #self.widget1.setEnabled(True)
        if self.radioButton_16.isChecked():
            print('NO')
            self.flag = 0
            self.L[3]=(bool(0))
            #self.widget1.setEnabled(True)
        if self.radioButton_17.isChecked():
            print('Yes')
            #self.flag = 0
            self.L[4]=(bool(1))
            #self.widget1.setEnabled(True)
        if self.radioButton_18.isChecked():
            print('NO')
            self.flag = 0
            self.L[4]=(bool(0))
        if self.radioButton_19.isChecked():
            print('Yes')
            #self.flag = 0
            self.L[5]=(bool(1))
            #self.widget1.setEnabled(True)
        if self.radioButton_20.isChecked():
            print('NO')
            self.flag = 0
            self.L[5]=(bool(0))

    def GetCheckItem(self):
        if self.checkBox.isChecked():
            print('Amol')
           # self.User[0] = 'Amol'
        
        if self.checkBox_2.isChecked():
            print('Parth')
            #self.User[1] = 'Parth'
        if self.checkBox_4.isChecked():
            print('Josh')
            #self.User[2] = 'Josh'
        if self.checkBox_3.isChecked():
            print('Manoj')
            #self.User[3] = 'Manoj'
    def GetCheckItem2(self):
        if self.checkBox.isChecked():
            #print('Amol')
            self.User[0] = 'Amol'
        
        if self.checkBox_2.isChecked():
            #print('Parth')
            self.User[1] = 'Parth'
        if self.checkBox_4.isChecked():
            #print('Josh')
            self.User[2] = 'Josh'
        if self.checkBox_3.isChecked():
            #print('Manoj')
            self.User[3] = 'Manoj'


    def GetShareName(self):
        self.sharename = self.lineEdit.text()
        print("sharename: {}".format(self.sharename))


    def SendBackend(self):
        _translate = QtCore.QCoreApplication.translate
        #self.L=[]
        self.GetShareName()
        self.L[0]=self.sharename
        self.L[1]=self.filename
        self.GetCheckItem2()

        print(self.L)

        if 'None' in self.User:
            #print('Am')
            #print(self.User)

            #self.U = list(set(self.User))
            #self.U.remove('None')
            #print(self.U)
            




            self.U = list(set(self.User))
            self.U.remove('None')
            print(self.U)
            if(cf.fileexists()):
                if(not cs.create(self.L[0],self.L[1],self.L[2],self.L[3],self.L[4],self.L[5],self.U)):
                    #self.labeldynamic.setText(_translate("Form","<html><head/><body><p><span style=\" color:#ff0000;\">ShareName already exists</span></p></body></html>"))
                    
                    QMessageBox.warning(self.obc, "Warning","Share Name Exist")
                else:
                    QMessageBox.information(self.obc, "Status","Share created successfully.")
                    self.obc.close()
            else:
                QMessageBox.warning(self.obc, "Warning","Share Creation Failed. Try creating manually from smb.conf file")
        else:
            self.U = list(set(self.User))
            print(self.U)
            if(cf.fileexists()):
                if(not cs.create(self.L[0],self.L[1],self.L[2],self.L[3],self.L[4],self.L[5],self.U)):
                    #self.labeldynamic.setText(_translate("Form","<html><head/><body><p><span style=\" color:#ff0000;\">ShareName already exists</span></p></body></html>"))
                    
                    QMessageBox.warning(self.obc, "Warning","Share Name Exist")
                else:
                    QMessageBox.information(self.obc, "Status","Share created successfully.")
                    self.obc.close()
            else:
                QMessageBox.warning(self.obc, "Warning","Share Creation Failed. Try creating manually from smb.conf file")

    





'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
'''