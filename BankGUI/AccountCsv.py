import csv
import os


def create_file():
    if not os.path.exists('Accounts.txt'):
        open('Accounts.txt', mode='a')


def get_account():
    if not os.path.exists('Accounts.txt'):
        create_file()
    values = []
    with open('Accounts.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            values.append(row)
    csv_file.close()
    return values


def edit_account(values):
    if not os.path.exists('Accounts.txt'):
        create_file()
    with open('Temp.txt', mode='a', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(values)
    new_file.close()
    os.remove("Accounts.txt")
    os.rename('Temp.txt', "Accounts.txt")


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
    if not os.path.exists('Accounts.txt'):
        create_file()
    accounts = list()
    with open('Accounts.txt', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            accounts.append(row)
        i = 0
        for account in accounts:
            if account[0] == username:
                accounts.pop(0)
            else:
                i += 1
    with open('Temp.txt', mode='w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(accounts)
    os.remove('Accounts.txt')
    os.rename('Temp.txt', 'Accounts.txt')
