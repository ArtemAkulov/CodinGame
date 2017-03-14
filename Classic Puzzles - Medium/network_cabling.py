#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#           Network Cabling             #
#                                       #
#########################################

def median(lst):
    lstLen = len(lst)
    index = (lstLen - 1) // 2
    if (lstLen % 2):
        return lst[index]
    else:
        return (lst[index] + lst[index + 1])/2.0

n = int(input())
pos_x = -(2**30) - 1
neg_x = 2**30 + 1
suburb_hell = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    if x > pos_x: pos_x = x
    if x < neg_x: neg_x = x
    suburb_hell.append(y)

suburb_hell.sort()

trenches = pos_x - neg_x

median_y = median(suburb_hell)

for i in range(n):
    trenches += abs(median_y - suburb_hell[i])

print(int(trenches))