import csv
import os
from PyQt5.QtCore import QDateTime

today = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss ap')
admin_save_path = '../AdminHistoryFolder/'
user_save_path = '../UserHistoryFolder/'


def create_file():
    file = admin_save_path + 'Accounts.txt'
    if not os.path.exists(file):
        open(file, mode='a')


def get_account():
    file = admin_save_path + 'Accounts.txt'
    create_file()
    values = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            values.append(row)
    csv_file.close()
    return values


def edit_account(values):
    temp_file = admin_save_path + 'Temp.txt'
    file = admin_save_path + 'Accounts.txt'
    create_file()
    with open(temp_file, mode='a', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(values)
    new_file.close()
    os.remove(file)
    os.rename(temp_file, file)


def account_exists(username):
    users = []
    i = 0
    for user in get_account():
        users.append(user[i])
    if users.count(username):
        return True
    else:
        return False


def account_index(username):
    values = get_account()
    i = 0
    for value in values:
        if value[0] == username:
            return i
        else:
            i += 1


def delete_account(username):
    file = admin_save_path + 'Accounts.txt'
    temp_file = admin_save_path + 'Temp.txt'
    create_file()
    accounts = list()
    with open(file, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            accounts.append(row)
        i = 0
        for account in accounts:
            if account[0] == username:
                accounts.pop(i)
            else:
                i += 1
    with open(temp_file, mode='w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(accounts)
    os.remove(file)
    os.rename(temp_file, file)


def update_history(username, transaction, balance):
    file = user_save_path + f'{username}.txt'
    if not os.path.exists(file):
        open(file, mode='a')
    if transaction == "Create Account":
        balance = "+" + balance
    elif transaction == "Delete Account":
        balance = "0"
    elif transaction == "Deposit":
        balance = "+" + balance
    elif transaction == "Withdraw":
        balance = "-" + balance
    values = [[today, transaction, balance]]
    with open(file, mode='a', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(values)


def admin_update_history(username, transaction):
    file = admin_save_path + 'AdminHistory.txt'
    record = ""
    if not os.path.exists(file):
        open(file, mode='a')
    if transaction == "Add Account":
        record = f"Added new account with the username '{username}'"
    elif transaction == "Delete Account":
        record = f"Deleted account with the username '{username}'"
    values = [[today, record]]
    with open(file, mode='a', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(values)


def get_admin_history(file):
    if file == 'AdminHistory.txt':
        file = admin_save_path + "AdminHistory.txt"
    elif file == 'Accounts.txt':
        file = admin_save_path + 'Accounts.txt'
    values = []
    if not os.path.exists(file):
        open(file, mode='a')
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            values.append(row)
    csv_file.close()
    return values


def get_user_history(user_index):
    file = user_save_path + f'{get_account()[user_index][0]}.txt'
    values = []
    if not os.path.exists(file):
        open(file, mode='a')
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            values.append(row)
    csv_file.close()
    return values
