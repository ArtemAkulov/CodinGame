#########################################
#                                       #
#  CodinGame Classic Puzzles  -  Easy   #
#            The Descent                #
#                                       #
#########################################

while True:
    height_max = 0
    crosshair = 0
    for i in range(8):
        mountain_h = int(input()) 
        if mountain_h > height_max:
            crosshair = i
            height_max = mountain_h
    print(crosshair)