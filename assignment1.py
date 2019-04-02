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


def city_value():
    while True:
        city = str(input("City Name:"))
        if len(city) == 0:
            print('Input can not be blank')
        else:
            return city.capitalize()


def country_value():
    while True:
        country = str(input("Country Name:"))
        if len(country) == 0:
            print('Input can not be blank')
        else:
            return country.capitalize()


def priority_value():
    while True:
        num = input("Priority: ")
        try:
            num = int(num)
        except:
            print("Invalid input; enter a valid number")
            continue
        if num <= 0:
            print("Number must be > 0")
        else:
            return num


def add_new_tracker(trackers, city, country, priority):
    print("{} in {}  (Priority: {}) added to Travel tracker".format(city, country, str(priority)))
    new_tracker = [city, country, priority, 'n']
    trackers.append(new_tracker)
    return sort_list(trackers)


def mark_place(trackers):
    start_not_visited_count = 0
    for i in range(0, len(trackers)):
        row = trackers[i]
        if row[3] == 'v':
            start_not_visited_count = i + 1

    if start_not_visited_count == 1:
        print("No unvisited place")
        return trackers

    display_places(trackers)

    print("Enter the number of a place to mark as visited.")
    while True:
        choice = input(">>>")
        try:
            choice = int(choice)
        except:
            print("Invalid input; enter a valid number.")
            continue

        if choice <= 0:
            print("Number must be > 0")

        elif choice > len(trackers):
            print("Invalid places number.")

        elif choice >= start_not_visited_count:
            print("That place is already visited")
            return sort_list(trackers)
        else:
            choice = choice - 1
            trackers[choice][3] = 'v'
            print(trackers[choice][0], 'in', trackers[choice][1], 'visited!')

    return sort_list(trackers)


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
            city = city_value()
            country = country_value()
            priority = priority_value()
            add_new_tracker(trackers, city, country, priority)

        elif choice == 'M':
            mark_place(trackers)

        elif choice == 'Q':
            pass

        else:
            print("Invalid menu choice")


if __name__ == '__main__':
    main()
