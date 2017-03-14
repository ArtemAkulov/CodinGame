###################################
#                                 #
#   CodinGame Community Puzzles   #
#          Magic Stones           #
#                                 #
###################################

n = int(input())
stones = sorted([int(i) for i in input().split()])
some_changes = True
while some_changes:
    some_changes = False
    i = 1
    stones.sort()
    while i < len(stones):
        if stones[i] == stones[i - 1]:
            some_changes = True
            j = stones.pop(i)
            stones[i - 1] += 1
        i += 1
print(len(stones))