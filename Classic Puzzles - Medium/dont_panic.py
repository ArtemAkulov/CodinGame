#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#            Don't Panic                #
#                                       #
#########################################

e={};o,w,q,x,z,k,y,n=[int(i)for i in input().split()]
for i in range(n):
 a,b=[int(j)for j in input().split()]
 e[a]=b
e[x]=z
while 1:
 f,c,d=input().split()
 if d!='NONE':print(('BLOCK','WAIT')[(e[int(f)]<(int(c)+1)and d=='LEFT')or(e[int(f)]>(int(c)-1)and d=='RIGHT')])
 else:print('WAIT')
 
# The remnants of a not particularly successful attempt at golfing. Eventually it got better. 