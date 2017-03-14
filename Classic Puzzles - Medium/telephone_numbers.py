#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#          Telephone Numbers            #
#                                       #
#########################################

n = int(input())
telephone = []
for i in range(n):
    telephone.append(input())

def estimate_space(t9_book):
   space_required = 0
   for digit in t9_book:
     if digit != '':
         space_required += 1
     if type(t9_book[digit]) is dict:
       space_required += estimate_space(t9_book[digit])
   return space_required 
 
def build_a_trie(phone_book):
    t9 = {}
    for number in phone_book:
        _t9 = t9
        for digit in number:
            _t9 = _t9.setdefault(digit, {})
        _t9 = _t9.setdefault('', '')
    return t9

t9_book = build_a_trie(telephone)
print(estimate_space(t9_book))