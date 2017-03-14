######################################
#                                    #
# CodinGame Classic Puzzles - Medium #
#               Bender               #
#                                    #
######################################

def pick_direction(board, location, drunk, priorities_reversed, direction = 'SOUTH'):
    compass = direction
    if board[location[0]][location[1]] == 'T':
        warp = [a for a in list([(a, b.index('T')) for a, b in enumerate(board) if 'T' in b]) if a != tuple(location)][0]
    else:
        warp = location
    if board[warp[0]][warp[1]] == 'S':
        candidate_location = [warp[0] + 1, warp[1]]
        compass = priorities[0]
    elif board[warp[0]][warp[1]] == 'E':
        candidate_location = [warp[0], warp[1] + 1]
        compass = priorities[1]
    elif board[warp[0]][warp[1]] == 'N':
        candidate_location = [warp[0] - 1, warp[1]]
        compass = priorities[2]
    elif board[warp[0]][warp[1]] == 'W':
        candidate_location = [warp[0], warp[1] - 1]
        compass = priorities[3]
    else:
        candidate_location = {
            'SOUTH': [warp[0] + 1, warp[1]],
            'EAST': [warp[0], warp[1] + 1],
            'NORTH': [warp[0] - 1, warp[1]],
            'WEST': [warp[0], warp[1] - 1],
        }[direction]
    target = board[candidate_location[0]][candidate_location[1]]
    if target == '#' or (target == 'X' and not drunk):
        priority_sequence = (list(range(4)), list(reversed(range(4))))[priorities_reversed]
        for candidate in priority_sequence:
            if candidate == 0:
                candidate_location = [warp[0] + 1, warp[1]]
                target = board[candidate_location[0]][candidate_location[1]]
                if target != '#' and not (target == 'X' and not drunk): 
                    compass = priorities[candidate]
                    break
            if candidate == 1:
                candidate_location = [warp[0], warp[1] + 1]
                target = board[candidate_location[0]][candidate_location[1]]
                if target != '#' and not (target == 'X' and not drunk): 
                    compass = priorities[candidate]
                    break
            if candidate == 2:
                candidate_location = [warp[0] - 1, warp[1]]
                target = board[candidate_location[0]][candidate_location[1]]
                if target != '#' and not (target == 'X' and not drunk): 
                    compass = priorities[candidate]
                    break
            if candidate == 3:
                candidate_location = [warp[0], warp[1] - 1]
                target = board[candidate_location[0]][candidate_location[1]]
                if target != '#' and not (target == 'X' and not drunk): 
                    compass = priorities[candidate]
                    break
    return candidate_location, compass

l, c = [int(i) for i in input().split()]
board = []
for i in range(l):
    board.append([i for i in input()])
path = []
priorities = {0: 'SOUTH', 1: 'EAST', 2: 'NORTH', 3: 'WEST'}
priorities_reversed = False
drunk = False
bender_location = list([(i, j.index('@')) for i, j in enumerate(board) if '@' in j][0])
next_move, direction = pick_direction(board, bender_location, drunk, priorities_reversed)
path.append(direction)
loop_check = {}
loop_check[tuple(bender_location)] = [board, direction, drunk, priorities_reversed]
while True:
    bender_location = next_move
    if board[bender_location[0]][bender_location[1]] == 'X':
        board[bender_location[0]][bender_location[1]] = ' '
        loop_check = {}
    if board[bender_location[0]][bender_location[1]] == '$':
        break
    if board[bender_location[0]][bender_location[1]] == 'B':
        drunk = not drunk
    if board[bender_location[0]][bender_location[1]] == 'I':
        priorities_reversed = not priorities_reversed
    if tuple(bender_location) in loop_check:
        if loop_check[tuple(bender_location)][0] == board and loop_check[tuple(bender_location)][1] == direction and loop_check[tuple(bender_location)][2] == drunk and loop_check[tuple(bender_location)][3] == priorities_reversed:
            path = ['LOOP']
            break
    else:
        loop_check[tuple(bender_location)] = [board, direction, drunk, priorities_reversed]
    next_move, direction = pick_direction(board, bender_location, drunk, priorities_reversed, path[-1])
    path.append(direction)
for move in path: 
    print(move)