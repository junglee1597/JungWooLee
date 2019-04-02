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
        return 'Travel Tracker 1.0 - By {}'.format(user_name.capitalize())


def max_city_width(trackers):
    result = 0
    for row in trackers:
        if len(row[0]) > result:
            result = len(row[0])
    return result + 1


def max_country_width(trackers):
    result = 0
    for row in trackers:
        if len(row[1]) > result:
            result = len(row[1])
    return result + 1


def display_places(trackers):
    city_width = max_city_width(trackers)
    country_width = max_country_width(trackers)

    not_visited_count = 0
    for i in range(0, len(trackers)):
        row = trackers[i]
        if row[3] == 'n':
            print('*', end='')
            not_visited_count += 1
        else:
            print('', end=' ')
        print(i + 1, end='. ')
        print("{:{city}}{:{country}}".format(row[0], "in " + row[1], city=city_width,
                                             country=country_width + 3), end='')
        print("Priority: {}".format(row[2]))

    if not_visited_count == 0:
        print(len(trackers), "places. No places left to visit. Why not add a new place?")
    else:
        print(len(trackers), "places. You still want to visit", not_visited_count, "places.")


def main():
    user_name = str(input("Please Enter Your Name:"))
    print(welcome_message(user_name))
    trackers = read_data('places.csv')

    while True:
        menu = """ -----MENU------
L - List place
A - Add New Place
M - Mark a place as visited
Q - Quit"""
        print(menu)
        choice = input("-->").upper()

        if choice == 'L':
            display_places(trackers)

        elif choice == 'A':
            pass

        elif choice == 'M':
            pass

        elif choice == 'Q':
            pass

        else:
            print("Invalid menu choice")


if __name__ == '__main__':
    main()
