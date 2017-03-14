#########################################
#                                       #
#  CodinGame Classic Puzzles  -  Easy   #
#           Chuck Norris                #
#                                       #
#########################################

message = input()
unary_message = ''
binary_message = ''

for i in range(len(message)):
    temp_string = bin(ord(message[i]))[2:]
    temp_string = (7 - len(temp_string)) * '0' + temp_string
    binary_message += temp_string

parsed_binary = []
parsed_binary.append(binary_message[0])
j = 0

for i in range(1, len(binary_message)):
    if binary_message[i] == binary_message[i - 1]:
        parsed_binary[j] += binary_message[i]
    else:
        j += 1
        parsed_binary.append(binary_message[i])

for i in range(len(parsed_binary)):
    if parsed_binary[i][0] == '0':
        unary_message += '00 '
    else:
        unary_message += '0 '
    unary_message += len(parsed_binary[i]) * '0' + ' '
unary_message = unary_message[:len(unary_message) - 1]
print(unary_message)