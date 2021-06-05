from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
from AccountCsv import get_account, account_index
from ChangePin import Ui_change_pin_window
from Deposit import Ui_deposit_window
from Withdraw import Ui_withdraw_window


class UiMainMenu(object):

    def thank_you_window(self):
        from ThankYou import UiThankYouMenu
        self.thank_you_menu = QtWidgets.QMainWindow()
        self.ui = UiThankYouMenu()
        self.ui.setupUi(self.thank_you_menu)
        self.thank_you_menu.show()

    def deposit_window(self, user_index):
        self.deposit_window = QtWidgets.QMainWindow()
        self.ui = Ui_deposit_window()
        self.ui.setupUi(self.deposit_window, user_index)
        self.deposit_window.show()

    def withdraw_window(self, user_index):
        self.withdraw_window = QtWidgets.QMainWindow()
        self.ui = Ui_withdraw_window()
        self.ui.setupUi(self.withdraw_window, user_index)
        self.withdraw_window.show()

    def show_balance(self, user_index):
        balance = get_account()[user_index][2]
        message = QMessageBox()
        message.setWindowTitle("Balance Inquiry")
        message.setText(f"Your balance is {balance}")
        message.setIcon(QMessageBox.Information)
        message.exec_()

    def change_pin_window(self, user_index):
        self.change_pin_window = QtWidgets.QMainWindow()
        self.ui = Ui_change_pin_window()
        self.ui.setupUi(self.change_pin_window, user_index)
        self.change_pin_window.show()

    def setupUi(self, main_menu, user_index):
        main_menu.setObjectName("main_menu")
        main_menu.resize(800, 600)
        main_menu.setStyleSheet("background-color: rgb(85, 116, 255);\n"
                                "background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(main_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.atm_label = QtWidgets.QLabel(self.centralwidget)
        self.atm_label.setGeometry(QtCore.QRect(20, 30, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.atm_label.setFont(font)
        self.atm_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.atm_label.setObjectName("atm_label")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(20, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "color: rgb(85, 170, 255);")
        self.welcome_label.setObjectName("welcome_label")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(20, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_label.setObjectName("name_label")
        self.name_label.setText(get_account()[user_index][0])
        self.withdraw_button = QPushButton(self.centralwidget, clicked=lambda: self.withdraw_window(user_index))
        self.withdraw_button.setGeometry(QtCore.QRect(530, 180, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.withdraw_button.setFont(font)
        self.withdraw_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(85, 170, 255);")
        self.withdraw_button.setObjectName("withdraw_button")
        self.withdraw_button.clicked.connect(lambda: main_menu.hide())
        self.deposit_button = QPushButton(self.centralwidget, clicked=lambda: self.deposit_window(user_index))
        self.deposit_button.setGeometry(QtCore.QRect(260, 180, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.deposit_button.setFont(font)
        self.deposit_button.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                          "color: rgb(255, 255, 255);")
        self.deposit_button.setObjectName("deposit_button")
        self.deposit_button.clicked.connect(lambda: main_menu.hide())
        self.changepin_button = QPushButton(self.centralwidget, clicked=lambda: self.change_pin_window(user_index))
        self.changepin_button.setGeometry(QtCore.QRect(530, 300, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.changepin_button.setFont(font)
        self.changepin_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(85, 170, 255);")
        self.changepin_button.setObjectName("changepin_button")
        self.changepin_button.clicked.connect(lambda: main_menu.hide())
        self.balinquiry_button = QPushButton(self.centralwidget, clicked=lambda: self.show_balance(user_index))
        self.balinquiry_button.setGeometry(QtCore.QRect(260, 300, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.balinquiry_button.setFont(font)
        self.balinquiry_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(85, 170, 255);")
        self.balinquiry_button.setObjectName("balinquiry_button")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(680, 20, 91, 81))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../images/Bank logo 1.png"))
        self.logo_label.setObjectName("logo_label")
        self.exit_button = QPushButton(self.centralwidget, clicked=lambda: self.thank_you_window())
        self.exit_button.setGeometry(QtCore.QRect(40, 410, 161, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(170, 0, 0);")
        self.exit_button.setObjectName("pushButton")
        self.exit_button.clicked.connect(lambda: main_menu.close())
        main_menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_menu)
        self.statusbar.setObjectName("statusbar")
        main_menu.setStatusBar(self.statusbar)
        self.retranslateUi(main_menu)
        QtCore.QMetaObject.connectSlotsByName(main_menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "Main Menu"))
        self.atm_label.setText(_translate("main_menu", "ATM"))
        self.welcome_label.setText(_translate("main_menu", "Welcome"))
        self.withdraw_button.setText(_translate("main_menu", "WITHDRAW"))
        self.deposit_button.setText(_translate("main_menu", "DEPOSIT"))
        self.changepin_button.setText(_translate("main_menu", "CHANGE PIN"))
        self.balinquiry_button.setText(_translate("main_menu", "BALANCE INQUIRY"))
        self.exit_button.setText(_translate("main_menu", "EXIT"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_menu = QtWidgets.QMainWindow()
    ui = UiMainMenu()
    ui.setupUi(main_menu, 0)
    main_menu.show()
    sys.exit(app.exec_())
