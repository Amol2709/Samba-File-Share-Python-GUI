# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#self.labeldynamic.setText(_translate("Form","<html><head/><body><p><span style=\" color:#ff0000;\">No Such ShareName</span></p></body></html>"))
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QInputDialog,QMessageBox
import DeleteShare as ds
from PyQt5.QtGui import QIcon
import CheckFile as cf

class Ui_Form_del(object):
    def __init__(self,obc):
        self.obc = obc
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 125)
        Form.setStyleSheet("background-color: rgb(204, 153, 255);")
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        #self.labeldynamic.setText(_translate("Form","<html><head/><body><p><span style=\" color:#ff0000;\">No Such ShareName</span></p></body></html>"))
        self.label.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.Enabledel)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        '''
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        '''
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Delete SambaShare"))
        Form.setWindowIcon(QIcon('team2.png'))
        Form.setWindowOpacity(0.95)
        # self.label.setText(_translate("Form","<html><head/><body><p><span style=\" color:#ffffff;\">Share Name</span></p></body></html>"))
        self.label.setText(_translate("Form", "ShareName"))
        #self.label_2.setText(_translate("Form", "Path"))
        #self.pushButton.setText(_translate("Form", "Browse Path"))
        self.pushButton_2.setText(_translate("Form", "Delete"))
        self.pushButton_2.clicked.connect(self.GetShareName)


    def Enabledel(self):
        self.pushButton_2.setEnabled(bool(self.lineEdit.text()))

    def GetShareName(self):
        self.sharename = self.lineEdit.text()
        print("sharename: {}".format(self.sharename))
        #self.pushButton_2.setEnabled(bool(self.lineEdit.text()))
        #self.a = 1
        #import sys
        #self.app = QtWidgets.QApplication(sys.argv)
        #self.Form = QtWidgets.QWidget()
        #ui = Ui_Form_del()
        #ui.setupUi(Form)
        #Form.show()
        #sys.exit(self.app.exec_())
        # ds.delete(self.sharename)
        # self.obc.close()
        if(cf.fileexists()):
            if(not ds.delete(self.sharename)):              
                    QMessageBox.warning(self.obc, "Warning","Share name does not exist.")
            else:
                QMessageBox.information(self.obc, "Status","Share deleted successfully.")
                self.obc.close()
        else:
            QMessageBox.warning(self.obc, "Warning","Share Deletion Failed. Try deleting manually from smb.conf file")





'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_del()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
'''
