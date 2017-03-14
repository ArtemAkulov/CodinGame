#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#          The Last Crusade             #
#                                       #
#########################################

directions = {'Down' : ['01TOP','01LEFT','01RIGHT', '03TOP', '04RIGHT', '05LEFT', '07TOP', '07RIGHT', '08LEFT', '08RIGHT', '09TOP', '09LEFT', '12RIGHT', '13LEFT'], 'Left' : ['02RIGHT', '04TOP', '06RIGHT', '10TOP'], 'Right' : ['02LEFT', '05TOP', '06LEFT', '11TOP']}
cave_grid = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    cave_grid.append(input().split())
ex = int(input())
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    for i in directions:
        for j in directions[i]:
            if j[2:] == pos and int(j[:2]) == int(cave_grid[yi][xi]): next_move = i
    if next_move == 'Down': yi += 1
    elif next_move == 'Right': xi += 1
    else: xi -= 1       
    print(xi,yi)   