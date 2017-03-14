###################################
#                                 #
#   CodinGame Community Puzzles   #
#           Hanoi Towers          #
#                                 #
###################################

def make_a_move(pegs, first, second):
    if max(pegs[first]) == 0:
        position = pegs[second].index(min([i for i in pegs[second] if i != 0]))
        pegs[first][-1] = pegs[second][position]
        pegs[second][position] = 0
    elif max(pegs[second]) == 0:
        position = pegs[first].index(min([i for i in pegs[first] if i != 0]))
        pegs[second][-1] = pegs[first][position]
        pegs[first][position] = 0
    else:
        min_1 = min([i for i in pegs[first] if i != 0])
        min_2 = min([i for i in pegs[second] if i != 0])
        position_1 = pegs[first].index(min_1)
        position_2 = pegs[second].index(min_2)
        if min_1 > min_2:
            pegs[first][position_1 - 1] = pegs[second][position_2]
            pegs[second][position_2] = 0
        else:
            pegs[second][position_2 - 1] = pegs[first][position_1]
            pegs[first][position_1] = 0
    return pegs

n = int(input())
t = int(input())

pegs = {}
pegs[1] = []
pegs[2] = []
pegs[3] = []
for i in range(1,n+1):
    pegs[1].append(i)
    pegs[2].append(0)
    pegs[3].append(0)

if n % 2 == 0:
    counter = 0
    while True:
        counter += 1
        pegs = make_a_move(pegs, 1, 2)
        if counter == t: break
        counter += 1
        pegs = make_a_move(pegs, 1, 3)
        if counter == t: break
        counter += 1
        pegs = make_a_move(pegs, 2, 3)
        if counter == t: break     
else:
    counter = 0
    while True:
        counter += 1
        pegs = make_a_move(pegs, 1, 3)
        if counter == t: break
        counter += 1
        pegs = make_a_move(pegs, 1, 2)
        if counter == t: break
        counter += 1
        pegs = make_a_move(pegs, 2, 3)
        if counter == t: break     

for i in range(n):
    first_peg_str = (' ' * (n - pegs[1][i]) + '#' * (pegs[1][i] * 2 + 1) + ' ' * (n - pegs[1][i]),' ' * n + '|' + ' ' * n)[pegs[1][i] == 0]
    second_peg_str = (' ' * (n - pegs[2][i]) + '#' * (pegs[2][i] * 2 + 1) + ' ' * (n - pegs[2][i]),' ' * n + '|' + ' ' * n)[pegs[2][i] == 0]
    third_peg_str = (' ' * (n - pegs[3][i]) + '#' * (pegs[3][i] * 2 + 1),' ' * n + '|')[pegs[3][i] == 0]
    print(first_peg_str + ' ' + second_peg_str + ' ' + third_peg_str)
print(2 ** n - 1)