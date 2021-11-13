# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nim.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
from PyQt5.QtWidgets import QMessageBox
from manual.settings_image_manual import Ui_Form


class Ui_nim(object):
    def setupUi(self, nim):
        nim.setObjectName("nim")
        nim.resize(579, 423)
        nim.setStyleSheet("background-color: rgb(2, 31, 108);\n"
                          "")
        self.bt_start = QtWidgets.QPushButton(nim)
        self.bt_start.setGeometry(QtCore.QRect(70, 50, 81, 26))
        self.bt_start.setStyleSheet("color: rgb(200, 186, 255);\n"
                                    "background-color: rgb(51, 53, 140);\n"
                                    "\n"
                                    "")
        self.bt_start.setObjectName("bt_start")

        self.bt_reset = QtWidgets.QPushButton(nim)
        self.bt_reset.setGeometry(QtCore.QRect(190, 50, 81, 26))
        self.bt_reset.setStyleSheet("color: rgb(200, 186, 255);\n"
                                    "background-color: rgb(51, 53, 140);")
        self.bt_reset.setObjectName("bt_reset")

        self.bt_end = QtWidgets.QPushButton(nim)
        self.bt_end.setGeometry(QtCore.QRect(310, 50, 81, 26))
        self.bt_end.setStyleSheet("color: rgb(200, 186, 255);\n"
                                  "background-color: rgb(51, 53, 140);")
        self.bt_end.setObjectName("bt_end")

        self.bt_instruction = QtWidgets.QPushButton(nim)
        self.bt_instruction.setGeometry(QtCore.QRect(440, 50, 81, 26))
        self.bt_instruction.setStyleSheet("color: rgb(200, 186, 255);\n"
                                          "background-color: rgb(51, 53, 140);")
        self.bt_instruction.setObjectName("instruction")

        self.label = QtWidgets.QLabel(nim)
        self.label.setGeometry(QtCore.QRect(150, 250, 111, 20))
        self.label.setStyleSheet("color: rgb(200, 186, 255);\n"
                                 "background-color: rgb(2, 31, 108);\n"
                                 "")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(nim)
        self.label_2.setGeometry(QtCore.QRect(340, 250, 100, 20))
        self.label_2.setStyleSheet("color: rgb(200, 186, 255);\n"
                                   "background-color: rgb(2, 31, 108);\n"
                                   "")
        self.label_2.setObjectName("label_2")

        self.chose_bunch = QtWidgets.QLineEdit(nim)
        self.chose_bunch.setGeometry(QtCore.QRect(150, 270, 111, 20))
        self.chose_bunch.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(51, 53, 140);")
        self.chose_bunch.setObjectName("chose_bunch")

        self.input_nummber_bunch = QtWidgets.QLineEdit(nim)
        self.input_nummber_bunch.setGeometry(QtCore.QRect(340, 270, 100, 20))
        self.input_nummber_bunch.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "background-color: rgb(51, 53, 140);")
        self.input_nummber_bunch.setObjectName("input_nummber_bunch")

        self.bt_move = QtWidgets.QPushButton(nim)
        self.bt_move.setGeometry(QtCore.QRect(260, 370, 81, 26))
        self.bt_move.setStyleSheet("color: rgb(200, 186, 255);\n"
                                   "background-color: rgb(51, 53, 140);")
        self.bt_move.setObjectName("bt_move")

        self.label_3 = QtWidgets.QLabel(nim)
        self.label_3.setGeometry(QtCore.QRect(250, 320, 101, 16))
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        self.label_3.setStyleSheet("color: rgb(200, 186, 255);\n"
                                   "background-color: rgb(2, 31, 108);\n"
                                   "")
        self.label_3.setObjectName("label_3")

        self.info_banch_1 = QtWidgets.QLabel(nim)
        self.info_banch_1.setGeometry(QtCore.QRect(120, 200, 60, 16))
        self.info_banch_1.setStyleSheet("color: rgb(200, 186, 255);\n"
                                        "background-color: rgb(2, 31, 108);\n"
                                        "")
        self.info_banch_1.setObjectName("info_banch_1")

        self.info_banch_2 = QtWidgets.QLabel(nim)
        self.info_banch_2.setGeometry(QtCore.QRect(260, 200, 60, 16))
        self.info_banch_2.setStyleSheet("color: rgb(200, 186, 255);\n"
                                        "background-color: rgb(2, 31, 108);\n"
                                        "")
        self.info_banch_2.setObjectName("info_banch_2")

        self.info_banch_3 = QtWidgets.QLabel(nim)
        self.info_banch_3.setGeometry(QtCore.QRect(400, 200, 60, 16))
        self.info_banch_3.setStyleSheet("color: rgb(200, 186, 255);\n"
                                        "background-color: rgb(2, 31, 108);\n"
                                        "")
        self.info_banch_3.setObjectName("info_banch_3")

        self.img_bunch_1 = QtWidgets.QLabel(nim)
        self.img_bunch_1.setGeometry(QtCore.QRect(110, 140, 61, 60))
        self.img_bunch_1.setText("")
        self.img_bunch_1.setPixmap(QtGui.QPixmap("page_bunch.png"))
        self.img_bunch_1.setObjectName("img_bunch_1")

        self.img_bunch_2 = QtWidgets.QLabel(nim)
        self.img_bunch_2.setGeometry(QtCore.QRect(250, 140, 61, 60))
        self.img_bunch_2.setText("")
        self.img_bunch_2.setPixmap(QtGui.QPixmap("page_bunch.png"))
        self.img_bunch_2.setObjectName("img_bunch_2")

        self.img_bunch_3 = QtWidgets.QLabel(nim)
        self.img_bunch_3.setGeometry(QtCore.QRect(390, 140, 61, 60))
        self.img_bunch_3.setText("")
        self.img_bunch_3.setPixmap(QtGui.QPixmap("page_bunch.png"))
        self.img_bunch_3.setObjectName("img_bunch_3")

        self.bt_types_of_errors = QtWidgets.QPushButton(nim)
        self.bt_types_of_errors.setGeometry(QtCore.QRect(460, 370, 101, 31))
        self.bt_types_of_errors.setStyleSheet("color: rgb(200, 186, 255);\n"
                                              "background-color: rgb(51, 53, 140);\n"
                                              "")

        self.retranslateUi(nim)
        QtCore.QMetaObject.connectSlotsByName(nim)

        # функции начала конце и перезапуска
        self.start_game()
        self.end_game()
        self.res_game()
        # self.instruction()

        self.move()

    def retranslateUi(self, nim):
        _translate = QtCore.QCoreApplication.translate
        nim.setWindowTitle(_translate("nim", "Form"))
        self.bt_start.setText(_translate("nim", "Start"))
        self.bt_reset.setText(_translate("nim", "Reset"))
        self.bt_end.setText(_translate("nim", "End"))
        self.bt_instruction.setText(_translate("nim", "instruction"))
        self.label.setText(_translate("nim", "how many stones"))
        self.label_2.setText(_translate("nim", "what bunch"))
        self.bt_move.setText(_translate("nim", "move"))
        self.label_3.setText(_translate("nim", "Ход игрока №1"))
        self.info_banch_1.setText(_translate("nim", "Bunch 1"))
        self.info_banch_2.setText(_translate("nim", "Bunch 2"))
        self.info_banch_3.setText(_translate("nim", "Bunch 3"))
        self.bt_types_of_errors.setText(_translate("nim", "types of errors"))

    # нач функций кнопок start end reset
    def start_game(self):
        self.bt_start.clicked.connect(lambda: self.start())

    def end_game(self):
        self.bt_end.clicked.connect(lambda: self.end())

    def res_game(self):
        self.bt_reset.clicked.connect(lambda: self.restart())

    # def instruction(self):
    #     self.bt_instruction.clicked.connect(lambda: self.instr())

    def start(self):
        a = []
        for i in range(3):
            i = randint(10, 50)
            a.append(i)
        self.info_banch_1.setText(str(a[0]))
        self.info_banch_2.setText(str(a[1]))
        self.info_banch_3.setText(str(a[2]))
        self.input_nummber_bunch.setText('0')
        self.chose_bunch.setText('0')

    def end(self):
        self.info_banch_1.setText('Bunch 1')
        self.info_banch_2.setText("Bunch 2")
        self.info_banch_3.setText("Bunch 3")
        self.input_nummber_bunch.setText('')
        self.chose_bunch.setText('')

    def restart(self):
        self.info_banch_1.setText('0')
        self.info_banch_2.setText("0")
        self.info_banch_3.setText("0")

    # конец функций кнопок start end reset

    def move(self):
        self.bt_move.clicked.connect(lambda: self.motion())

    def clear(self):
        self.chose_bunch.setText('')
        self.input_nummber_bunch.setText('')

    def win(self):
        a = list(self.label_3.text())
        win = QMessageBox()
        win.setWindowTitle('Конец')
        win.setText('ВЫ победили')
        win.setInformativeText(f'Выиграл игрок{self.label_3.text()[-1]}')
        win.setIcon(QMessageBox.Information)
        win.setStandardButtons(QMessageBox.Ok)
        win.buttonClicked.connect(self.end)
        win.exec_()

    def error_bench(self, much_remove, number_bunch):
        if number_bunch == 1:
            chose = self.info_banch_1.text()
        elif number_bunch == 2:
            chose = self.info_banch_2.text()
        elif number_bunch == 3:
            chose = self.info_banch_3.text()
        notification = QMessageBox()
        notification.setWindowTitle('Ошибка')
        notification.setText('Данное действие не возможно')
        notification.setInformativeText('число камней не может быть меньше 0')
        notification.setIcon(QMessageBox.Information)
        notification.setStandardButtons(QMessageBox.Ok)
        notification.setDetailedText(f'при выполнении данного действия уровень камней в кучке '
                                     f'{number_bunch} будет '
                                     f'{int(chose) - much_remove} камней, а такой уровень камней не возможен')
        notification.buttonClicked.connect(self.clear)
        notification.exec_()

    def motion(self):
        try:
            what_bunch = int(self.chose_bunch.text())
            much_remove = int(self.input_nummber_bunch.text())
        except:
            what_bunch = self.chose_bunch.text()
            much_remove = self.input_nummber_bunch.text()

        if self.info_banch_1.text() == 'Bunch 1':
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Данное действие не возможно')
            error.setInformativeText('вы не начали игру нажмите start')
            error.setIcon(QMessageBox.Information)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()


        elif (str(what_bunch) == '0' and str(much_remove) == '0') or \
                (isinstance(what_bunch, str) or isinstance(much_remove, str)):
            if int(self.info_banch_1.text()) == 0 and int(self.info_banch_2.text()) == 0 \
                    and int(self.info_banch_3.text()) == 0:
                self.win()
            else:
                error = QMessageBox()
                error.setWindowTitle('Ошибка')
                error.setText('Данное действие не возможно')
                error.setInformativeText('поля действия не заданы или заполнены не корректно ')
                error.setIcon(QMessageBox.Information)
                error.setStandardButtons(QMessageBox.Ok)
                error.setDetailedText(f'"how many stones" = {self.chose_bunch.text()} \n'
                                      f'"what bunch" =  {self.input_nummber_bunch.text()}')
                error.buttonClicked.connect(self.clear)
                error.exec_()


        elif int(what_bunch) == 1 and int(self.info_banch_1.text()) >= 0:
            bunch_info = int(self.info_banch_1.text())
            if bunch_info - int(much_remove) >= 0:
                self.info_banch_1.setText(str(bunch_info - int(much_remove)))
                a = list(self.label_3.text())
                if a[-1] == '1':
                    self.label_3.setText('Ход игрока №2')
                elif a[-1] == '2':
                    self.label_3.setText('Ход игрока №1')
                self.chose_bunch.setText('')
                self.input_nummber_bunch.setText('')

            elif bunch_info - int(much_remove) < 0:
                number_bunch = 1
                self.error_bench(much_remove, number_bunch)
            elif int(self.info_banch_1.text()) == 0 and int(self.info_banch_2.text()) == 0 \
                    and int(self.info_banch_3.text()) == 0:
                self.win()



        elif int(what_bunch) == 2 and int(self.info_banch_2.text()) >= 0:
            bunch_info = int(self.info_banch_2.text())
            if bunch_info - int(much_remove) >= 0:
                self.info_banch_2.setText(str(bunch_info - int(much_remove)))
                a = list(self.label_3.text())
                if a[-1] == '1':
                    self.label_3.setText('Ход игрока №2')
                elif a[-1] == '2':
                    self.label_3.setText('Ход игрока №1')
                self.chose_bunch.setText('')
                self.input_nummber_bunch.setText('')

            elif bunch_info - int(much_remove) < 0:
                number_bunch = 2
                self.error_bench(much_remove, number_bunch)
            elif int(self.info_banch_1.text()) == 0 and int(self.info_banch_2.text()) == 0 \
                    and int(self.info_banch_3.text()) == 0:
                self.win()




        elif int(what_bunch) == 3 and int(self.info_banch_3.text()) >= 0:
            bunch_info = int(self.info_banch_3.text())
            if bunch_info - int(much_remove) >= 0:
                self.info_banch_3.setText(str(bunch_info - int(much_remove)))
                a = list(self.label_3.text())
                if a[-1] == '1':
                    self.label_3.setText('Ход игрока №2')
                elif a[-1] == '2':
                    self.label_3.setText('Ход игрока №1')
                self.chose_bunch.setText('')
                self.input_nummber_bunch.setText('')
            elif bunch_info - int(much_remove) < 0:
                number_bunch = 3
                self.error_bench(much_remove, number_bunch)
            elif int(self.info_banch_1.text()) == 0 and int(self.info_banch_2.text()) == 0 \
                    and int(self.info_banch_3.text()) == 0:
                self.win()

    # def instr(self):
    #     global st_im_mn
    #     # self.label_3.setText('Ход игрока №3')
    #     st_im_mn = QtWidgets.QWidget()
    #     ui = Ui_Form()
    #     ui.setupUi(st_im_mn)
    #     st_im_mn.show()
    #     nim.hide()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    nim = QtWidgets.QWidget()
    ui = Ui_nim()
    ui.setupUi(nim)
    nim.show()
    sys.exit(app.exec_())
