from
CONST_PIN = 1234
CONST_BALANCE = 10000


def login():
    pin = 0
    tries = 3
    while True:
        pin = int(input("Please input your pin "))
        if pin_checker(pin):
            return True
        else:
            tries = tries - 1
            print(f"Pin is incorrect. {tries} tries left.")
        if tries == 0:
            return False


def pin_checker(pin):
    if CONST_PIN == pin:
        return True
    else:
        return False


def user_account():
    if login():
        choice = input("A. Account Balance\nB. Deposit\nC. Withdraw\nD. Change Pin")
        user_options(choice.upper())
    else:
        print("Your card is blocked. Please contact the bank for more information. ")


def user_options(choice):
    if choice == "A":
        print("Account Balance")
    if choice == "B":
        print("Deposit")
    if choice == "C":
        print("Withdraw")
    if choice == "D":
        print("Change Pin")