###################################
#                                 #
#  CodinGame Community Puzzles    #
#    Minimal Number of Swaps      #
#                                 #
###################################

input()
chain = [int(_) for _ in input().split()]
swaps=0
for i in range(len(chain)-1,-1,-1):
    if chain[i] == 1:
        for j in range(0,i-1):
            if chain[j] == 0:
                chain[i],chain[j] = chain[j],chain[i]
                swaps += 1
                break
print(swaps)