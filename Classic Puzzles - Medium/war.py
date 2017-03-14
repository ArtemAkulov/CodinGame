#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#                 War                   #
#                                       #
#########################################

dec_values = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'10':8,'J':9,'Q':10,'K':11,'A':12,}
deck_1 = []
deck_2 = []
n = int(input()) 
for i in range(n):
    cardp_1 = input()  
    deck_1.append(dec_values[cardp_1[:-1]])
m = int(input())  
for i in range(m):
    cardp_2 = input() 
    deck_2.append(dec_values[cardp_2[:-1]])

def simulate_game(deck_1, deck_2):
    moves = 0
    while 1:
        moves += 1
        play_1 = deck_1.pop(0)
        play_2 = deck_2.pop(0)
        if play_1 > play_2:
            deck_1 += play_1, play_2
        elif play_2 > play_1:
            deck_2 += play_1, play_2
        else:
            spoils_of_war_1 = []
            spoils_of_war_1.append(play_1)
            spoils_of_war_2 = []
            spoils_of_war_2.append(play_2)
            while play_1 == play_2 and len(deck_1) > 3 and len(deck_2) > 3:
                for i in range(4): 
                    spoils_of_war_1.append(deck_1.pop(0))
                    spoils_of_war_2.append(deck_2.pop(0))
                play_1 = spoils_of_war_1[-1]
                play_2 = spoils_of_war_2[-1]
            if play_1 == play_2: 
                return('PAT')
            elif play_1 > play_2:
                deck_1 += (spoils_of_war_1 + spoils_of_war_2)
            else:
                deck_2 += (spoils_of_war_1 + spoils_of_war_2)
        if len(deck_1) == 0:
            return('2 ' + str(moves))
        elif len(deck_2) == 0:
            return('1 ' + str(moves))

print(simulate_game(deck_1,deck_2))