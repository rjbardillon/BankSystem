import csv
import os


def get_account():
    values = []
    with open('Accounts.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            values.append(row)
    csv_file.close()
    return values


def write_account(values):
    new_file = open('Temp.txt', 'w', newline='')
    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(values)
    new_file.close()
    os.remove("Accounts.txt")
    os.rename("Temp.txt", "Accounts.txt")
