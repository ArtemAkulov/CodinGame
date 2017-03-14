###################################
#                                 #
#  CodinGame Community Puzzles    #
#             Gravity             #
#                                 #
###################################

i,i=map(int,input().split());o=(input()for _ in range(i))
for _ in zip(*(sorted(__,reverse=True)for __ in zip(*o))):print(*_,sep="")