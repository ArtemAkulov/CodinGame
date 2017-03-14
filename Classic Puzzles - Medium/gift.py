#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#               The Gift                #
#                                       #
#########################################

n = int(input())
c = int(input())

oods_savings = []
oods_spendings = []

for i in range(n):
    oods_savings.append(int(input()))

remaining_oods = len(oods_savings)
expenses = c
oods_savings.sort()

if sum(oods_savings) < c:
    print('IMPOSSIBLE')
else:
    for ripped_off_ood in oods_savings:
        average_budget = expenses // remaining_oods
        remaining_oods -= 1
        if ripped_off_ood >= average_budget:
            expenses -= average_budget
            oods_spendings.append(average_budget)
        else:
            expenses -= ripped_off_ood
            oods_spendings.append(ripped_off_ood)
    for ripped_off_ood in oods_spendings:
        print(ripped_off_ood)