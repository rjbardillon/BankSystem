import mysql.connector


my_db = mysql.connector.connect(host="localhost", user="root", passwd="admin1234", database="atmsystem")
my_cursor = my_db.cursor()


def get_item(username, item):
    my_cursor.execute(f"SELECT {item} from customer where username='{username}'")
    for i in my_cursor:
        return i[0]


def add_account(username, name, pin, balance):
    try:
        my_cursor.execute(f"INSERT into customer values('{username}','{name}', {pin}, {balance})")
        my_db.commit()
        return True
    except mysql.connector.errors.IntegrityError:
        return False


def delete_account(username):
    my_cursor.execute(f"DELETE from customer WHERE username='{username}'")
    my_db.commit()


def deposit(username, money_deposited):
    balance = get_item(username, "balance")
    my_cursor.execute(f"UPDATE customer SET balance = {balance + money_deposited} where username='{username}'")
    my_db.commit()


def withdraw(username, money_withdrawn):
    balance = get_item(username, "balance")
    my_cursor.execute(f"UPDATE customer SET balance = {balance - money_withdrawn} where username='{username}'")
    my_db.commit()


def change_pin(username, new_pin):
    my_cursor.execute(f"UPDATE customer SET pin = {new_pin} where username='{username}'")
    my_db.commit()


# print(add_account('romsky1.bardillon', 'Romeo Jr M Bardillon', 1234, 10000))
# delete_account("jj.gmail")
# deposit("romsky.bardillon", 10000)
# withdraw("romsky.bardillon", 10000)
# change_pin("romsky.bardillon", 4321)
# print(get_item("romsky.bardillon", "name"))
