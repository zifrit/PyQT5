# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tesT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 220)
        self.pull_down_menu_formats = QtWidgets.QComboBox(Form)
        self.pull_down_menu_formats.setGeometry(QtCore.QRect(110, 60, 291, 22))
        self.pull_down_menu_formats.setObjectName("pull_down_menu_formats")
        self.pull_down_menu_formats.addItem("")
        self.pull_down_menu_formats.addItem("")
        self.pull_down_menu_formats.addItem("")
        self.initializing_tables_bt = QtWidgets.QPushButton(Form)
        self.initializing_tables_bt.setGeometry(QtCore.QRect(150, 180, 81, 26))
        self.initializing_tables_bt.setObjectName("initializing_tables_bt")
        self.lb_info_about_format = QtWidgets.QLabel(Form)
        self.lb_info_about_format.setGeometry(QtCore.QRect(110, 30, 281, 16))
        self.lb_info_about_format.setObjectName("lb_info_about_format")
        self.checkBox_fio = QtWidgets.QCheckBox(Form)
        self.checkBox_fio.setGeometry(QtCore.QRect(10, 140, 85, 21))
        self.checkBox_fio.setObjectName("checkBox_fio")
        self.checkBox_kurss = QtWidgets.QCheckBox(Form)
        self.checkBox_kurss.setGeometry(QtCore.QRect(70, 140, 85, 21))
        self.checkBox_kurss.setObjectName("checkBox_kurss")
        self.checkBox_type_of_scholarship = QtWidgets.QCheckBox(Form)
        self.checkBox_type_of_scholarship.setGeometry(QtCore.QRect(210, 140, 121, 21))
        self.checkBox_type_of_scholarship.setObjectName("checkBox_type_of_scholarship")
        self.checkBox_profil = QtWidgets.QCheckBox(Form)
        self.checkBox_profil.setGeometry(QtCore.QRect(130, 140, 85, 21))
        self.checkBox_profil.setObjectName("checkBox_profil")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(330, 140, 151, 21))
        self.checkBox_5.setObjectName("checkBox_5")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(280, 180, 81, 26))
        self.exit.setObjectName("exit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.click()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pull_down_menu_formats.setItemText(0, _translate("Form", "none"))
        self.pull_down_menu_formats.setItemText(1, _translate("Form", "блокнот"))
        self.pull_down_menu_formats.setItemText(2, _translate("Form", "excel"))
        self.initializing_tables_bt.setText(_translate("Form", "click"))
        self.lb_info_about_format.setText(_translate("Form", "формат получения данных"))
        self.checkBox_fio.setText(_translate("Form", "ФИО"))
        self.checkBox_kurss.setText(_translate("Form", "Курсс"))
        self.checkBox_type_of_scholarship.setText(_translate("Form", "Вид стипендии"))
        self.checkBox_profil.setText(_translate("Form", "Профиль"))
        self.checkBox_5.setText(_translate("Form", "Дата начала и конца"))
        self.exit.setText(_translate("Form", "exit"))


    def click(self):
        self.pull_down_menu_formats.activated[str].connect(self.onActivated)

    def onActivated(self, text):
        self.initializing_tables_bt.setText(text)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())