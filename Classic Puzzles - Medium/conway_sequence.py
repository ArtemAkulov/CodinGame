#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#           Conway Sequence             #
#                                       #
#########################################

def next_line_x(current_line, target_line, conway):
    current_line += 1
    in_progress = conway
    i = 1
    conway = ''
    if in_progress.find(' ') == -1:
        test_value = in_progress
    else: 
        test_value = in_progress[:in_progress.find(' ')]
        in_progress = in_progress[in_progress.find(' ') + 1:]
    
    while in_progress.find(' ') != -1:
        if in_progress[:in_progress.find(' ')] == test_value:
            i += 1
            in_progress = in_progress[in_progress.find(' ') + 1:]
        else:
            conway += (str(i) + ' ' + test_value + ' ')
            test_value = in_progress[:in_progress.find(' ')]
            in_progress = in_progress[in_progress.find(' ') + 1:]
            i = 1
    if test_value == in_progress:
        i += 1
        conway += (str(i) + ' ' + in_progress)
    else:
        conway += (str(i) + ' ' + test_value + ' 1 ' + in_progress)
    if current_line == target_line: 
        return conway
    else: return(next_line_x(current_line, target_line, conway))
    
conway = input()
target_line = int(input())


current_line = 1
if target_line == 2: 
    conway = '1 ' + conway
    target_line -= 1
if current_line >= target_line: result = conway
else: result = next_line_x(current_line, target_line - 1, '1 ' + conway)    

print(result)