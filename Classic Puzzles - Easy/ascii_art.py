#########################################
#                                       #
#  CodinGame Classic Puzzles  -  Easy   #
#             ASCII Art                 #
#                                       #
#########################################

l = int(input())
h = int(input())
t = input()
alphabet = 27*['']
alphabet_index = []
output_string = t

for i in range(h):
    row = input()
    for j in range(0,27):
        alphabet[j] += row[(j*l):(l+j*l)]

for i in range(len(output_string)):
    if ord(output_string[i]) > 64 and ord(output_string[i]) < 91:
        alphabet_index.append(ord(output_string[i]) - 65)
    elif ord(output_string[i]) > 96 and ord(output_string[i]) < 123:
        alphabet_index.append(ord(output_string[i]) - 97)
    else:
        alphabet_index.append(26)

string_to_print = h*['']

for i in range(len(alphabet_index)):
    for j in range(len(string_to_print)):
        string_to_print[j] += alphabet[alphabet_index[i]][(0 + j*l):(l + j*l)]
        
for j in range(len(string_to_print)):
    print(string_to_print[j])