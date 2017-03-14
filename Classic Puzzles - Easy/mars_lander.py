#########################################
#                                       #
#  CodinGame Classic Puzzles  -  Easy   #
#            Mars Lander                #
#                                       #
#########################################

surface_n = int(input()) 
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if y > 2499:
        thrust = 0
    elif y > 2300:
        thrust = 1
    elif y> 2200:
        thurst = 2
    elif y > 1600:
        thrust = 3
    else:
        thrust = 4
    print(0, thrust)