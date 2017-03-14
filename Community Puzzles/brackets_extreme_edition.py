###################################
#                                 #
#  CodinGame Community Puzzles    #
#   Brackets, Extreme Edition     #
#                                 #
###################################

def brackets_check(expression):
    deck = []
    opening, closing = '({[', ')}]'
    for _ in expression:
        if _ in opening: deck.append(_)
        elif _ in closing:
            if not deck: return 'false'
            else:
                if deck.pop() != opening[closing.index(_)]: return 'false'
    return 'false' if deck else 'true'
print(brackets_check(input()))