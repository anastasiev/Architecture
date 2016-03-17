from view import *

def england(lst):
    for i in lst:
        if i[0] == 'England':
            output_match(i)


def spain(lst):
    for i in lst:
        if i[0] == 'Spain':
            output_match(i)


def ukraine(lst):
    for i in lst:
        if i[0] == 'Ukraine':
            output_match(i)


def sort_goals(arr):
    mas = []
    for i in arr:
        k = i[3] + i[4]
        if k not in mas:
            mas.append(k)
    mas.sort(reverse=True)
    for i in mas:
        for j in arr:
            if i == j[3] + j[4]:
                output_match(j)

def sort_date(arr):
    mas = []
    for i in arr:
        mas.append(i[5][0])
    mas.sort()
    for i in mas:
        for j in arr:
            if i == j[5][0]:
                output_match(j)

def menu(arr):
    ch = ''
    while(ch != '6'):
        print("""
        1. England
        2. Spain
        3. Ukraine
        4. Sort by number of goals
        5. Sort by date
        6. Exit
        """)
        ch = input()

        if ch == '1':
            england(arr)
        elif ch == '2':
            spain(arr)
        elif ch == '3':
            ukraine(arr)
        elif ch == '4':
            sort_goals(arr)
        elif ch == '5':
            sort_date(arr)
        elif ch == '6':
            exit()
        else:
            print('Please try again')
