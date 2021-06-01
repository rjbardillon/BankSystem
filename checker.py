

def pin_checkerzeth(pin):
    if user_pin == pin:
        return True
    else:
        return False


def loginzeth():
    tries = 3
    while True:
        pin = input("Please input your pin ")
        if pin_checkerzeth(pin):
            return True
        else:
            tries = tries - 1
            print(f"Pin is incorrect. {tries} tries left.")
        if tries == 0:
            return False
