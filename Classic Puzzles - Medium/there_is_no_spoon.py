#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#         There Is No Spoon             #
#                                       #
#########################################

grid = []
width = int(input())
height = int(input()) 
for i in range(height):
    line = input() 
    grid.append(list(line))
        
for i in range(height):
    for j in range(width):
        coords_self = '-1 -1 '
        coords_neighbor_right = '-1 -1 '
        coords_neighbor_below = '-1 -1'
        if grid[i][j] == '0':
            coords_self = str(j) + ' ' + str(i) + ' '
            if j < (width - 1):
                k = j
                while k < (width - 1):
                    k += 1
                    if grid[i][k] == '0':
                        coords_neighbor_right = str(k) + ' ' + str(i) + ' '
                        break
            if i < (height - 1):
                k = i
                while k < (height - 1):
                    k += 1
                    if grid[k][j] == '0':
                        coords_neighbor_below = str(j) + ' ' + str(k)
                        break
                    
        if coords_self != '-1 -1 ':
            print(coords_self + coords_neighbor_right + coords_neighbor_below)