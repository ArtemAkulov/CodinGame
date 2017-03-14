###################################
#                                 #
#   CodinGame Community Puzzles   #
#      Simple Safecracking        #
#                                 #
###################################

msg = input()
code = msg[(msg.find(':') + 2):]
cipher = msg[:msg.find(':')].lower()

digits = []

while code.find('-') != -1:
    digits.append(code[:code.find('-')])
    code = code[(code.find('-') + 1):]
digits.append(code)

for i in range(len(digits)):
    if len(digits[i]) == 5:
        if digits[i][0] == cipher[2]:
            digits[i] = '8'
        elif digits[i][0] == cipher[4]:
            digits[i] = '7'
        else:
            digits[i] = '3'
    elif len(digits[i]) == 4:
        if digits[i][3] == cipher[10]:
            digits[i] = '0'
        elif digits[i][1] == cipher[10]:
            digits[i] = '4'
        elif digits[i][0] == cipher[6]:
            digits[i] = '5'    
        else:
            digits[i] = '9'
    else:
        if digits[i][0] == cipher[10]:
            digits[i] = '1'
        elif digits[i][0] == cipher[0]:
            digits[i] = '2'
        else:
            digits[i] = '6'

print(''.join(digits))