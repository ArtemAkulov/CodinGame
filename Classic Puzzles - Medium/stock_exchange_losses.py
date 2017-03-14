#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#       Stock Exchange Losses           #
#                                       #
#########################################

vmax = 0
vmin = 0
net_loss = 0
n = int(input())
for i in input().split():
    v = int(i)
    if v > vmax:
        vmax = v
        vmin = v
    if v < vmin:
        vmin = v
    if vmax - vmin > net_loss:
        net_loss = vmax - vmin
print(-1*net_loss)