#!/usr/bin/python3

import sys

# Test 1
# input = ">"
# Test 2
# input = "^>v<"
# Test 3
# input = "^v^v^v^v^v"

map = {}
map[0, 0] = 1
santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0

def update_map(x, y, map):
    if c == '>':
        x += 1
    elif c == '<':
        x -= 1
    elif c == '^':
        y += 1
    elif c == 'v':
        y -= 1
    else:
        print("Invalid input: %c" % c)
    if (x, y) in map.keys():
        map[ x, y ] +=  1
    else:
        map[ x, y ] = 1
    return (x, y, map)

# Loop through the input instructions
input = sys.stdin.readline().rstrip()
turn = 0
for c in input:
    if turn == 0:
        # Santa's turn
        (santa_x, santa_y, map) = update_map(santa_x, santa_y, map)
        turn = 1
    else:
        # Robo-santa's turn
        (robo_x, robo_y, map) = update_map(robo_x, robo_y, map)
        turn = 0
    
# Count the number of entries in the map hash
house_count = 0
for location in map:
    house_count += 1
print("House count: %d" % house_count)

