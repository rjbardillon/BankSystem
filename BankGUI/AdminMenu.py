import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMessageBox
from AddAccount import UiAddAccountWindow
from DeleteAccount import UiDeleteAccountWindow
from AccountCsv import create_file


class UIAdminMenu(object):

    def thank_you_window(self):
        from BankGUI.ThankYou import UiThankYouMenu
        self.thank_you_menu = QtWidgets.QMainWindow()
        self.ui = UiThankYouMenu()
        self.ui.setupUi(self.thank_you_menu)
        self.thank_you_menu.show()

    def add_account(self):
        self.add_account_window = QtWidgets.QMainWindow()
        self.ui = UiAddAccountWindow()
        self.ui.setupUi(self.add_account_window)
        self.add_account_window.show()

    def delete_account(self):
        create_file()
        if os.path.getsize('Accounts.txt') == 0:
            self.no_account_error()
            self.add_account()
        else:
            self.delete_account_window = QtWidgets.QMainWindow()
            self.ui = UiDeleteAccountWindow()
            self.ui.setupUi(self.delete_account_window)
            self.delete_account_window.show()

    def no_account_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("No Account as of the moment. Click Ok to add account.")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def setupUi(self, Admin_Menu):
        Admin_Menu.setObjectName("main_menu")
        Admin_Menu.resize(800, 600)
        Admin_Menu.setStyleSheet("background-color: rgb(85, 116, 255);\n"
                                "background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(Admin_Menu)
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
        self.name_label.setGeometry(QtCore.QRect(20, 190, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_label.setObjectName("name_label")
        self.delete_account_button = QPushButton(self.centralwidget, clicked=lambda: self.delete_account())
        self.delete_account_button.setGeometry(QtCore.QRect(520, 270, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.delete_account_button.setFont(font)
        self.delete_account_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "background-color: rgb(85, 170, 255);")
        self.delete_account_button.setObjectName("delete_account_button")
        self.delete_account_button.clicked.connect(lambda: Admin_Menu.hide())
        self.add_account_button = QPushButton(self.centralwidget, clicked=lambda: self.add_account())
        self.add_account_button.setGeometry(QtCore.QRect(250, 270, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.add_account_button.setFont(font)
        self.add_account_button.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                              "color: rgb(255, 255, 255);")
        self.add_account_button.setObjectName("add_account_button")
        self.add_account_button.clicked.connect(lambda: Admin_Menu.hide())
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
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(lambda: Admin_Menu.close())
        Admin_Menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Admin_Menu)
        self.statusbar.setObjectName("statusbar")
        Admin_Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Admin_Menu)
        QtCore.QMetaObject.connectSlotsByName(Admin_Menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "Main Menu"))
        self.atm_label.setText(_translate("main_menu", "ATM"))
        self.welcome_label.setText(_translate("main_menu", "Welcome"))
        self.name_label.setText(_translate("main_menu", "ADMINISTRATOR"))
        self.delete_account_button.setText(_translate("main_menu", "DELETE\n"
                                                                   "ACCOUNT"))
        self.add_account_button.setText(_translate("main_menu", "ADD ACCOUNT"))
        self.exit_button.setText(_translate("main_menu", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_menu = QtWidgets.QMainWindow()
    ui = UIAdminMenu()
    ui.setupUi(admin_menu)
    admin_menu.show()
    sys.exit(app.exec_())
