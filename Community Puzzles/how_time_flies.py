###################################
#                                 #
#   CodinGame Community Puzzles   #
#         How Time Flies          #
#                                 #
###################################

from datetime import date

begin = input()
end = input()

start_year = int(begin[6:])
end_year = int(end[6:])

start_month = int(begin[3:5])
end_month = int(end[3:5])

start_day = int(begin[:2])
end_day = int(end[:2])

final_word = ''

d0 = date(start_year, start_month, start_day)
d1 = date(end_year, end_month, end_day)
delta = d0 - d1

delta_years = end_year - start_year

if end_month > start_month:
    delta_months = end_month - start_month
elif start_month > end_month:
    delta_years -= 1
    delta_months = (end_month + (12 - start_month))
else: delta_months = 0    

if start_day > end_day:
    delta_months -= 1

if delta_years > 0:
    if delta_years % 10 == 1: years_str = ' year, '
    else: years_str = ' years, '
    final_word += str(delta_years) + years_str

if delta_months > 0:
    if delta_months % 10 == 1: months_str = ' month, '
    else: months_str = ' months, '
    final_word += str(delta_months) + months_str

if abs(delta.days) % 10 == 1: days_str = ' day'
else: days_str = ' days'

final_word += 'total ' + str(abs(delta.days)) + days_str

print(final_word)