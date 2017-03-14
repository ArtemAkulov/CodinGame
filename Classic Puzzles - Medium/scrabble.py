#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#               Scrabble                #
#                                       #
#########################################

letter_scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
                 "x": 8, "z": 10}
          
def word_score(word):
    return sum(letter_scores[letter] for letter in word)

def spellable(letters, word):
    mutated_letters = sorted(letters)
    mutated_word = sorted(word)
    for letter in mutated_word:
        if not(letter in mutated_letters): return False
        mutated_letters.pop(mutated_letters.index(letter))    
    return True    

words_dictionary = []
possible_words = {}
n = int(input())
for i in range(n): words_dictionary.append(input())
letters = input()
words_dictionary = words_dictionary[::-1]

for candidate in words_dictionary:
    if spellable(letters, candidate): possible_words[word_score(candidate)] = candidate
print(possible_words[max(possible_words.keys(), key=int)])