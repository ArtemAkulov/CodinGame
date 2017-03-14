######################################
#                                    #
# CodinGame Classic Puzzles - Medium #
#          Mayan Calculation         #
#                                    #
######################################

def to_mayan(non_mayan, base):
   conversion = '0123456789ABCDEFGHIJ'
   if non_mayan < base: return conversion[non_mayan]
   else: return to_mayan(non_mayan//base,base) + conversion[non_mayan%base]
raw_numerals = []
numerals={}
raw_first_number = []
raw_second_number = []
first_number = 0
second_number = 0
digit = ''
glyphs = []
numeral_width, numeral_height = [int(i) for i in input().split()]
for i in range(numeral_height): raw_numerals.append(input())
first_number_lines = int(input())
for i in range(first_number_lines): raw_first_number.append(input())
second_number_lines = int(input())
for i in range(second_number_lines): raw_second_number.append(input())
operation = input()
for i in range(20):
    mayan_numeral = ''
    for j in range(numeral_height): mayan_numeral += raw_numerals[j][i * numeral_width:i * numeral_width + numeral_width]
    numerals[mayan_numeral] = to_mayan(i, 20)
for i in range(0, first_number_lines, numeral_height):
    for j in range(0, numeral_height): digit += raw_first_number[i + j]
    first_number += int(numerals[digit], 20) * (20 ** (first_number_lines/numeral_height - 1 - i/numeral_height))
    digit = ''
for i in range(0, second_number_lines, numeral_height):
    for j in range(0, numeral_height): digit += raw_second_number[i + j]
    second_number += int(numerals[digit], 20) * (20 ** (second_number_lines/numeral_height - 1 - i/numeral_height))
    digit = ''
if operation == '*': result_mayan = to_mayan(int(first_number * second_number), 20)
elif operation == '/': result_mayan = to_mayan(int(first_number // second_number), 20)
elif operation == '-': result_mayan = to_mayan(int(first_number - second_number), 20)
else: result_mayan = to_mayan(int(first_number + second_number), 20)
for i in result_mayan: glyphs.append(list(numerals.keys())[list(numerals.values()).index(i)])
for j in glyphs:
    for i in range(0, numeral_height): print(j[i*numeral_width:i*numeral_width + numeral_width])