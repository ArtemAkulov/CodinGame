########################################
#                                      #
#  CodinGame Bot Programming Problems  #
#         Coders Strike Back           #
#                                      #
########################################

j = 0
k = 1
dest_x = [1,2,3]
dest_y = [1,2,3]

last_checkpoint_x = 0
last_checkpoint_y = 0
next_checkpoint_x = 0
next_checkpoint_y = 0
boost_available = True

while True:
    
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if last_checkpoint_x != next_checkpoint_x and last_checkpoint_y != next_checkpoint_y:
        last_checkpoint_x = next_checkpoint_x
        last_checkpoint_y = next_checkpoint_y
        dest_x[j] = next_checkpoint_x
        dest_y[j] = next_checkpoint_y
        if j == 2:
            j = 0
        else:
            j += 1
        k += 1    
        
    if k < 4:
        next_relative_index = -1
    elif j == 3:
        next_relative_index = 0
    else:
        next_relative_index = j
    relative_index = j - 1    
    
    if next_checkpoint_dist < 700 and next_relative_index != -1:
        final_dest_x = dest_x[next_relative_index]
        final_dest_y = dest_y[next_relative_index]
    else:
        final_dest_x = dest_x[relative_index]
        final_dest_y = dest_y[relative_index]
        
    if next_checkpoint_dist < 650:
        thrust = 0
    elif next_checkpoint_dist < 850:
        thrust = 10
    elif next_checkpoint_dist < 950:
        thrust = 20
    elif next_checkpoint_dist < 1050:
        thrust = 30
    elif next_checkpoint_dist < 1150:
        thrust = 40
    elif next_checkpoint_dist < 1350:
        thrust = 60
    elif next_checkpoint_dist < 1600:
        thrust = 80
    else:
        thrust = 100
    
    if abs(next_checkpoint_angle) > 90:
        thrust = 0
    elif abs(next_checkpoint_angle) > 80:    
        thrust = int(thrust * 0.3)    
    elif abs(next_checkpoint_angle) > 60:    
        thrust = int(thrust * 0.7)
    elif abs(next_checkpoint_angle) > 50:    
        thrust = int(thrust * 0.8)
    elif abs(next_checkpoint_angle) > 60:    
        thrust = int(thrust * 0.9)    
    else:
        thrust = 100
        
    if abs(next_checkpoint_angle) < 15 and next_checkpoint_dist > 6000 and boost_available:
        print(str(final_dest_x) + " " + str(final_dest_y) + " " + "BOOST")
        boost_available = False
    else:
        print(str(final_dest_x) + " " + str(final_dest_y) + " " + str(thrust))