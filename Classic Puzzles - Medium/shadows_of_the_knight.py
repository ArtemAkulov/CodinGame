#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#       Shadows of the Knight           #
#                                       #
#########################################

w, h = [int(i) for i in input().split()]
n = int(input())
x, y = [int(i) for i in input().split()]
upper_lim_x = w
upper_lim_y = h
lower_lim_x = 0
lower_lim_y = 0
while True:
    bomb_dir = input()
    if 'R' in bomb_dir:
        x_delta = (upper_lim_x - x) // 2
        lower_lim_x = x
    elif 'L' in bomb_dir:
        x_delta = (lower_lim_x - x) // 2
        upper_lim_x = x
    else:
        x_delta = 0
        lower_lim_x = x
        upper_lim_x = x
    if 'U' in bomb_dir:
        y_delta = (lower_lim_y - y) // 2
        upper_lim_y = y
    elif 'D' in bomb_dir:
        y_delta = (upper_lim_y - y) // 2
        lower_lim_y = y
    else:
        y_delta = 0
        lower_lim_y = y
        upper_lim_y = y
    x += x_delta
    y += y_delta
    print(str(x) + ' ' + str(y))