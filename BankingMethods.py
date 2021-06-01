from time import sleep
from ClearScreen import clear
balance = 10000
user_pin = 1234


def format_float(balance):
    return "₱{:,.2f}".format(balance)


def account_balance():
    print(f"Your balance is {format_float(balance)}")
    sleep(2)
    clear()


def deposit():
    global balance
    print(f"Your Balance is {balance}")
    money_deposited = float(input("How much money you want to deposit? "))
    balance += money_deposited
    print(f"Your new balance is {format_float(balance)}")
    sleep(2)
    clear()


def withdraw():
    global balance
    print(f"Your Balance is {format_float(balance)}")
    while balance > 0:
        while True:
            money_withdrawn = float(input("How much money you want to withdraw? "))
            if money_withdrawn > balance:
                print("You don't have enough balance.")
                sleep(2)
            else:
                balance -= money_withdrawn
                print(f"Your new balance is {format_float(balance)}")
                sleep(2)
                clear()
                break
        break


def change_pin():
    global user_pin
    while True:
        new_pin = int(input("Input your new pin: "))
        confirm_pin = int(input("Confirm your new pin: "))
        if new_pin == confirm_pin:
            user_pin = new_pin
            print(f"Pin was changed. Your new pin is {user_pin}")
            break
        else:
            print("Pin didn't matched.")
    sleep(2)
    clear()


def pin_checker(pin):
    if user_pin == pin:
        return True
    else:
        return False
