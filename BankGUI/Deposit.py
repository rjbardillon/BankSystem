from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QMessageBox, QPushButton, QLineEdit
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from AccountCsv import get_account, write_account


class Ui_deposit_window(object):

    def main_menu(self):
        from MainMenu import UiMainMenu
        self.main_menu = QtWidgets.QMainWindow()
        self.ui = UiMainMenu()
        self.ui.setupUi(self.main_menu)
        self.main_menu.show()

    def setupUi(self, deposit_window):
        deposit_window.setObjectName("deposit_window")
        deposit_window.resize(800, 600)
        deposit_window.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(deposit_window)
        self.centralwidget.setObjectName("centralwidget")
        self.deposit_label = QtWidgets.QLabel(self.centralwidget)
        self.deposit_label.setGeometry(QtCore.QRect(30, 140, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.deposit_label.setFont(font)
        self.deposit_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.deposit_label.setObjectName("deposit_label")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(690, 10, 101, 91))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../images/Bank logo 1.png"))
        self.logo_label.setObjectName("logo_label")
        self.input_deposit = QtWidgets.QLineEdit(self.centralwidget)
        self.input_deposit.setValidator(QRegExpValidator(QRegExp("[0-9]{6}")))
        self.input_deposit.setGeometry(QtCore.QRect(370, 140, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.input_deposit.setFont(font)
        self.input_deposit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(85, 170, 255);")
        self.input_deposit.setObjectName("input_deposit")
        self.enter_button = QPushButton(self.centralwidget, clicked=lambda: self.enter_pressed())
        self.enter_button.setGeometry(QtCore.QRect(450, 250, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(85, 170, 255);")
        self.enter_button.setObjectName("enter_button")
        self.enter_button.clicked.connect(lambda: deposit_window.close())
        self.cancel_button = QPushButton(self.centralwidget, clicked=lambda: self.main_menu())
        self.cancel_button.setGeometry(QtCore.QRect(170, 260, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(170, 0, 0);")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(lambda: deposit_window.hide())
        deposit_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(deposit_window)
        self.statusbar.setObjectName("statusbar")
        deposit_window.setStatusBar(self.statusbar)

        self.retranslateUi(deposit_window)
        QtCore.QMetaObject.connectSlotsByName(deposit_window)

    def retranslateUi(self, deposit_window):
        _translate = QtCore.QCoreApplication.translate
        deposit_window.setWindowTitle(_translate("deposit_window", "Deposit"))
        self.deposit_label.setText(_translate("deposit_window", "Input amount to deposit"))
        self.enter_button.setText(_translate("deposit_window", "ENTER"))
        self.cancel_button.setText(_translate("deposit_window", "CANCEL"))

    def enter_pressed(self):
        s_money_deposited = self.input_deposit.text()
        elements = get_account()
        balance = int(elements[0][2])
        if len(self.input_deposit.text()) == 0:
            self.error()
        else:
            money_deposited = int(s_money_deposited)
            if money_deposited < 1:
                self.error()
            else:
                balance += money_deposited
                elements[0][2] = balance
                write_account(elements)
                self.deposit_success()

    def deposit_success(self):
        balance = get_account()[0][2]
        message = QMessageBox()
        message.setWindowTitle("Successful")
        message.setText(f"Your new balance is {balance}")
        message.setIcon(QMessageBox.Information)
        message.exec_()
        self.main_menu()

    def error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("Your deposit should not be less than ₱1!")
        message.setIcon(QMessageBox.Warning)
        message.exec_()
        self.main_menu()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    deposit_window = QtWidgets.QMainWindow()
    ui = Ui_deposit_window()
    ui.setupUi(deposit_window)
    deposit_window.show()
    sys.exit(app.exec_())
