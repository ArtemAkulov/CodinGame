###################################
#                                 #
#   CodinGame Community Puzzles   #
#           The Fastest           #
#                                 #
###################################


total_time = []
string_time = []

n = int(input())
for i in range(n):
    t = input()
    string_time.append(t)

for i in range(len(string_time)):
    hours = string_time[i][:2]
    minutes = string_time[i][3:5]
    seconds = string_time[i][6:]
    total_time.append(int(hours) * 60 * 60 + int(minutes) * 60 + int(seconds))

result = 0
    
for i in range(1, len(total_time)):
    if total_time[i] < total_time[result]:
        result = i

print(string_time[result])   