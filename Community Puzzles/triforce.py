###################################
#                                 #
#   CodinGame Community Puzzles   #
#            Triforce             #
#                                 #
###################################

n = int(input())
s1 = 2 * n - 1
s2 = 1
for i in range(n):
    print('.' * (i == 0) + ' ' * (s1 - (i == 0)) + '*' * s2)
    s1 -= 1
    s2 += 2
s1 = n - 1
s2 = 1
s3 = n * 2 - 1
for i in range(0, n, 1):
    print(' ' * s1 + '*' * s2 + ' ' * s3 + '*' * s2)
    s1 -= 1
    s2 += 2
    s3 -= 2