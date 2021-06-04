import csv
import os


def get_account(file):
    values = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            values.append(row)
    csv_file.close()
    return values


def add_account(values, file):
    with open('Temp.txt', mode='a', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(values)
    new_file.close()
    os.remove(file)
    os.rename('Temp.txt', file)
