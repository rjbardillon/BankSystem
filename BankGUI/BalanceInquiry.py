from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from BankGUI.AccountCsv import get_account


class Ui_balance_inquiry_window(object):
    def setupUi(self, balance_inquiry_window):
        balance_inquiry_window.setObjectName("balance_inquiry_window")
        balance_inquiry_window.resize(800, 600)
        balance_inquiry_window.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(balance_inquiry_window)
        self.centralwidget.setObjectName("centralwidget")
        self.balance_label = QtWidgets.QLabel(self.centralwidget)
        self.balance_label.setGeometry(QtCore.QRect(30, 140, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.balance_label.setFont(font)
        self.balance_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.balance_label.setObjectName("balance_label")
        self.log_label = QtWidgets.QLabel(self.centralwidget)
        self.log_label.setGeometry(QtCore.QRect(690, 10, 101, 91))
        self.log_label.setText("")
        self.log_label.setPixmap(QtGui.QPixmap("../images/Bank logo 1.png"))
        self.log_label.setObjectName("log_label")
        self.input_deposit = QtWidgets.QLineEdit(self.centralwidget)
        self.input_deposit.setGeometry(QtCore.QRect(270, 140, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.input_deposit.setFont(font)
        self.input_deposit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(85, 170, 255);")
        self.input_deposit.setObjectName("input_deposit")
        balance_inquiry_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(balance_inquiry_window)
        self.statusbar.setObjectName("statusbar")
        balance_inquiry_window.setStatusBar(self.statusbar)

        self.retranslateUi(balance_inquiry_window)
        QtCore.QMetaObject.connectSlotsByName(balance_inquiry_window)

    def retranslateUi(self, balance_inquiry_window):
        _translate = QtCore.QCoreApplication.translate
        balance_inquiry_window.setWindowTitle(_translate("balance_inquiry_window", "Balance Inquiry"))
        self.balance_label.setText(_translate("balance_inquiry_window", "Your Balance is"))
        self.input_deposit.setText(_translate("balance_inquiry_window", "₱"))

    def show_balance(self):
        balance = get_account()[0][2]
        message = QMessageBox()
        message.setWindowTitle("Balance Inquiry")
        message.setText(f"Your balance is {balance}")
        message.setIcon(QMessageBox.Information)
        message.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    balance_inquiry_window = QtWidgets.QMainWindow()
    ui = Ui_balance_inquiry_window()
    ui.setupUi(balance_inquiry_window)
    balance_inquiry_window.show()
    sys.exit(app.exec_())
