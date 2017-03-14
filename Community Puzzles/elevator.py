###################################
#                                 #
#   CodinGame Community Puzzles   #
#            Elevator             #
#                                 #
###################################

n, a, b, k, m = [int(i) for i in input().split()]

number_of_moves = 0

def try_to_go_up(building_floors, current_floor, step):
    return (current_floor + step) <= building_floors
    
def try_to_go_down(building_floors, current_floor, step):
    return (current_floor - step) > 0


while k != m:
    if k < m and try_to_go_up(n, k, a):
        k += a
        number_of_moves += 1
    elif k > m and try_to_go_down(n, k, b):
        k -= b
        number_of_moves += 1
    elif k < m and try_to_go_down(n, k, b):
        k -= b
        number_of_moves += 1
    elif k > m and try_to_go_up(n, k, a):
        k += a
        number_of_moves += 1
    else:
        number_of_moves = 0
        break
    if number_of_moves > n:
        number_of_moves = 0
        break
    
if number_of_moves != 0:
    print(number_of_moves)
else:
    print("IMPOSSIBLE")