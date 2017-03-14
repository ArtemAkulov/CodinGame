#########################################
#                                       #
#  CodinGame Classic Puzzles  -  Easy   #
#           Power of Thor               #
#                                       #
#########################################

a,b,x,y=map(int,input().split())
while 1:print(('',('S','N')[b<y])[y!=b]+('',('E','W')[a<x])[x!=a]);y+=(0,(1,-1)[y>b])[y!=b];x+=(0,(1,-1)[x>a])[x!=a]