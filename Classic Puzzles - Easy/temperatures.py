#########################################
#                                       #
#  CodinGame Classic Puzzles  -  Easy   #
#            Temperatures               #
#                                       #
#########################################

n = int(input())
temps = input()

if n != 0:
    results_list = []
    independent_n = len(temps)
    temp_string = ""
    for i in range(len(temps)):
        if temps[i] != " ":
            temp_string += temps[i]
        else:
            results_list.append(int(temp_string))        
            temp_string = ""
    if temp_string != "":
        results_list.append(int(temp_string))
    final_result = 65535
    for i in range(n):
        if abs(results_list[i]) < abs(final_result):
            final_result = results_list[i]
        elif abs(results_list[i]) == abs(final_result) and results_list[i] > final_result:
            final_result = results_list[i]
else:
    final_result = 0        
print(final_result)

# Wow, that's so much worse than the much later version I used in Code Golf.