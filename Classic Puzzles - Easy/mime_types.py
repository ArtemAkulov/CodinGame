#########################################
#                                       #
#  CodinGame Classic Puzzles  -  Easy   #
#             MIME Type                 #
#                                       #
#########################################

n = int(input())
q = int(input()) 

mime_dictionary = {}
for i in range(n):
    ext, mt = input().split()
    mime_dictionary[ext.upper()] = mt
for i in range(q):
    fname = input()
    if fname.upper()[::-1][:(fname.upper()[::-1].find('.'))][::-1] in mime_dictionary:
        print(mime_dictionary[fname.upper()[::-1][:(fname.upper()[::-1].find('.'))][::-1]])
    else:
        print('UNKNOWN')