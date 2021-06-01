from BankingMethods import account_balance, deposit, withdraw, change_pin, pin_checker


def user_options(choice):
    if choice == "A":
        account_balance()
    elif choice == "B":
        deposit()
    elif choice == "C":
        withdraw()
    elif choice == "D":
        change_pin()
    elif choice == "E":
        print("Thank You for Using our Bank System :)")
        exit()


def login():
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


def user_account():
    if login():
        while True:
            choice = input("A. Account Balance\nB. Deposit\nC. Withdraw\nD. Change Pin\nE. Exit\t")
            user_options(choice.upper())
    else:
        print("Your card is blocked. Please contact the bank for more information. ")
