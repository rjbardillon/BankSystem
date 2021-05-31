from User import user_account




def show_screen():
    choice = input("A. Admin\nB. User\t")
    if choice.upper() == "A":
        admin_account()
    else:
        user_account()


def admin_account():
    print("Admin Account")


show_screen()
