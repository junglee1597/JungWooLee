"""
Name:JUNG WOO LEE
Date started: 27 MARCH 2019
GitHub URL:
"""
import csv


def read_data(file_name):
    trackers = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row[2] = int(row[2])
            trackers.append(row)
    print(len(trackers), "places loaded from", file_name)
    return sort_list(trackers)


def sort_list(lst):
    lst = sorted(lst, key=sort_key)
    return lst


def sort_key(row):
    return row[3], row[2]


def welcome_message(user_name):
    if len(user_name) == 0:
        return "Input can not be blank"
    else:
        return 'Travel Tracker 1.0 - By ,{}'.format(user_name.capitalize())


def main():
    user_name = str(input("Please Enter Your Name:"))
    print(welcome_message(user_name))
    trackers = read_data('places.csv')


if __name__ == '__main__':
    main()
