########################################
#                                      #
#  CodinGame Bot Programming Problems  #
#          Ghost in the Cell           #
#                                      #
########################################


factories = {}
factory_count = int(input())
for i in range(factory_count):
    factories[i] = [[],[],0,0,0]
link_count = int(input())  
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    factories[factory_1][0].append(factory_2)
    factories[factory_1][1].append(distance)
    factories[factory_2][0].append(factory_1)
    factories[factory_2][1].append(distance)
treks = []
for i in factories: treks += factories[i][1]
max_trek = max(treks)

while True:
    bombed_this_turn = False
    points_of_attack = []
    entity_count = int(input())  
    troops = {}    
    for i in range(entity_count):
        entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
        entity_id = int(entity_id)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        arg_5 = int(arg_5)
        if entity_id in factories:
            factories[entity_id][2] = arg_1#ownership
            factories[entity_id][3] = arg_3#production
            factories[entity_id][4] = arg_2#garrison
        if entity_type == 'TROOP':
            troops[entity_id] = [arg_1, arg_2, arg_3, arg_4, arg_5]

    action = 'WAIT'
    unclaimed_producers = []
    controlled = []
    rival = []
    
    for factory, content in factories.items():
        if content[2] == 0 and content[3] != 0:
            unclaimed_producers.append(factory)
        if content[2] == 1:
            controlled.append(factory)
        if content[2] == -1:
            rival.append(factory)
    if unclaimed_producers:
        local_max = max_trek
        for i in unclaimed_producers:
            valid_target = True
            assault_team = 0
            for k in troops:
                if troops[k][2] == i: assault_team += troops[k][3]
            if factories[i][4] < assault_team: valid_target = False
            if valid_target:
                for j in controlled:
                    placeholder1 = [n for m,n in zip(factories[i][0], factories[i][1]) if m == j]
                    
                    source, destination, trek = j, i, placeholder1[0]
                    number_of_troops = factories[i][4] + 1
                    if number_of_troops > factories[j][4]: number_of_troops = int(factories[j][4] * 0.85)
                    points_of_attack.append(source)
                    action += ';MOVE ' + str(source) + ' ' + str(destination) + ' ' + str(number_of_troops)
    dream_team = 0
    attack_origin = 0
    for i in controlled:
        if factories[i][4] > dream_team:
            attack_origin = i
            dream_team = factories[i][4]
    dream_target = -1
    for i in rival:
        if factories[i][3] > dream_target:
            attack_point = i
            dream_target = factories[i][3]
    if dream_team> 0 and dream_target > -1:
        attack_team = factories[attack_point][4] + (factories[attack_point][3] * factories[attack_origin][1][factories[attack_origin][0].index(attack_point)])
        if attack_team > factories[attack_origin][4]:
            attack_team = int(factories[attack_origin][4] * 0.85)
        if attack_team // 2 > factories[attack_point][3]:
            points_of_attack.append(attack_origin)
            action += ';MOVE ' + str(attack_origin) + ' ' + str(attack_point) + ' ' + str(attack_team)
    biggest_garrison = -1
    happiest_fuckers = -1
    poorest_fuckers = -1
    smallest_garrison = 65536
    for i in controlled:
        if factories[i][4] > biggest_garrison:
            biggest_garrison = factories[i][4]
            happiest_fuckers = i
        if factories[i][4] < smallest_garrison:
            smallest_garrison = factories[i][4]
            poorest_fuckers = i
    if (biggest_garrison - smallest_garrison) > int(biggest_garrison * 0.25):
        points_of_attack.append(happiest_fuckers)
        action += ';MOVE ' + str(happiest_fuckers) + ' ' + str(poorest_fuckers) + ' ' + str((biggest_garrison - smallest_garrison) // 2)
    for i in controlled:
        if i not in points_of_attack:
            rival_production = -1
            target = -1
            for j in rival:
                if factories[j][3] > rival_production and factories[j][4] > 10:
                    rival_production = factories[j][3]
                    target = j
            if target != -1 and not bombed_this_turn:
                action += ';BOMB ' + str(i) + ' ' + str(target)
                bombed_this_turn = True
    print(action)