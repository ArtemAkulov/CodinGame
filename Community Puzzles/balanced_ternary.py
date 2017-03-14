###################################
#                                 #
#   CodinGame Community Puzzles   #
#        Balanced Ternary         #
#                                 #
###################################

decimal = int(input())
if decimal == 0:
    print('0')
elif decimal < 0:
    invert_it = True
else:
    invert_it = False

decimal = abs(decimal)
    
ternary = ''
while decimal != 0:
    ternary += str(decimal%3)
    decimal = decimal // 3

balanced_ternary = ''
i = 0
z = 0
while i < len(ternary):
    next_digit = int(ternary[i]) + z
    if next_digit == 0 or next_digit == 1:
        balanced_ternary += str(next_digit)
        z = 0
    elif next_digit == 2:
        balanced_ternary += 'T'
        z = 1
    else:
        balanced_ternary += '0'
        z = 1
    i += 1
if z != 0:
    balanced_ternary += str(z)    

if invert_it == True:
    inverted_ternary = ''
    for i in balanced_ternary:
        if i == 'T':
            inverted_ternary += '1'
        elif i == '1':
            inverted_ternary += 'T'
        else:
            inverted_ternary += i
    balanced_ternary = inverted_ternary        

    
print(balanced_ternary[::-1])  