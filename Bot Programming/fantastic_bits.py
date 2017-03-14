########################################
#                                      #
#  CodinGame Bot Programming Problems  #
#           Fantastic Bits             #
#                                      #
########################################


my_team_id = int(input())
goal_x = (0, 16000)[my_team_id == 0]
goal_y = 3750

while True:
    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]
    entities = int(input()) 
    players = []
    snaffles = []
    for i in range(entities):
        entity_id, entity_type, x, y, vx, vy, state = input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        state = int(state)
        if entity_type == 'WIZARD':
            player = [entity_id, x, y, vx, vy, state]
            players.append(player)
        elif entity_type == 'SNAFFLE':
            snaffle = [x,y,vx,vy,state]
            snaffles.append(snaffle)
    for i in range(len(players)):
        if players[i][5] == 1:
            print('THROW ' + str(goal_x) + ' ' + str(goal_y) + ' 500')
        else:
            min_dist = int((16000**2 + 3750**2) ** 0.5)
            likely_target = 0
            for j in range(len(snaffles)):
                current_dist = ((snaffles[j][0] - players[i][1]) ** 2 + (snaffles[j][1] - players[i][2]) ** 2) ** 0.5
                if  current_dist < min_dist:
                    min_dist = current_dist
                    likely_target = j
            print('MOVE ' + str(snaffles[likely_target][0]) + ' ' + str(snaffles[likely_target][1]) + ' 150')