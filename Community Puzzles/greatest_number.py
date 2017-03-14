###################################
#                                 #
#   CodinGame Community Puzzles   #
#       The Greatest Number       #
#                                 #
###################################

input()
pile = input()
positive = True
dot = False
answer = []
for i in pile:
    if i == '.': dot = True
    elif i == '-': positive = False
    elif ord(i) > 47 and ord(i) < 58: answer.append(i)
answer.sort(reverse = positive)
if answer[0] == '0' and len(set(answer)) == 1: print(0)
else:
    if not positive: 
        answer.insert(0, '-')
        if dot: answer.insert(2, '.')    
    else:
        if dot:
            if answer[-1] != '0': answer.insert(-1, '.')
            else: answer.pop(-1)
    print(''.join(answer))