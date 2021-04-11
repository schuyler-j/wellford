#!/usr/bin/python3

import random
import re


def isbound():
    x = open('map_bounds.txt', 'r')
    map_file = x.read()

    z = input("check:")

    if z in map_file:
        print("In Bounds")

    else:
        print("Out of Bounds")



letter = ["A", "B", "C", "D", "E", "F", "X"]

rows = [1, 2, 3, 4, 5, 6]

map_row = {
        1: "1 ".join(letter),
        2: "2 ".join(letter),
        3: "3 ".join(letter),
        4: "4 ".join(letter),
        5: "5 ".join(letter),
        6: "6 ".join(letter),

}

global pointer
pointer = 1
global row
row = 4

print("Locate the treasure.")
print("Type 'move left/right/up/down' to move around.")
print("Type 'check' to see if you have found the treasure.")
print("Type 'map' to view the map.")
print("")

l = []
count = 0

class map:

    def place_origin():
        num = 3
        roll_letter = 1
        roll = letter[roll_letter]
        x = open('map_bounds.txt', 'r')
        map_file = x.read()

        global origin

        origin = str(num)+str(roll)

        map.move()


    def place_goal():
        global num
        num = random.randint(1,6) 
        global roll_letter
        roll_letter = random.randint(0,5) 
        roll = letter[roll_letter]

        x = open('map_bounds.txt', 'r')
        global map_file
        map_file = x.read()
        map_file = str(map_file)

        global goal

        goal = str(num)+str(roll)
        l.append(goal)
        print(l[0], "is the goal.")



    def move():

        global pointer

        global row

        map.place_goal() 
        print("Catch me if you can...")

        place_split = map_row[row].split(" ")

        reverse = place_split[pointer]
        position = reverse[::-1]
        print("You are here --->", position)

        if row == 0 or row == 7:
            print("Out of Bounds!")
            return 0

        if position == "X":
            print("Out of Bounds!")
            return 0

        query_movement = input("Where would you like to go? ")
        print("")
        global count
        count = count + 1


        if query_movement == "check":
            if position == (l[0]):
                print("You Win!")
                print(count-1)
            else:
                print("Try Again...")
                map.move()

        if query_movement == "map":
            count = count - 1
            print(map_file)
            map.move()
        else:
            pass

        if query_movement == "move left":
            pointer = pointer - 1
            reverse = place_split[pointer]
            position = reverse[::-1]
            map.move()

        elif query_movement == "move right":
            pointer = pointer + 1
            reverse = place_split[pointer]
            position = reverse[::-1]
            map.move()

        elif query_movement == "move up":
            row = row - 1
            place_split = map_row[row].split(" ")
            reverse = place_split[pointer]
            position = reverse[::-1]
            map.move()


        elif query_movement == "move down":
            row = row + 1
            place_split = map_row[row].split(" ")
            reverse = place_split[pointer]
            position = reverse[::-1]
            map.move()
        



'''
        reverse = place_split[pointer]
        position = reverse[::-1]
'''

map.place_origin()
