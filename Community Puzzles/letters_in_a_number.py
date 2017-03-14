###################################
#                                 #
#  CodinGame  Community Puzzles   #
#  Letters in a Number - Binary   #
#                                 #
###################################

start, n = [int(i) for i in input().split()]
for i in range(1, n + 1):
    start_b = "{0:b}".format(start)
    result = 0
    for j in start_b: result += (3, 4)[j == '0']
    if start == result: break
    start = result
print(start)