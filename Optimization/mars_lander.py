###################################
#                                 #
# CodinGame Optimization Problems #
#           Mars Lander           #
#                                 #
###################################

surface_x = []
surface_y = []
flat_start = -1
flat_finish = -1
flat_y = -1
n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(n):
    land_x, land_y = [int(j) for j in input().split()]
    surface_x.append(land_x)
    surface_y.append(land_y)
    if i > 0:
        if land_y == surface_y[i - 1]:
            flat_start = surface_x[i - 1]
            flat_y = surface_y[i - 1]
    if flat_start >= 0 and flat_finish == -1:
        if land_y != surface_y[i - 1]:
            flat_finish = surface_x[i - 1]
landing_zone = []
for i in range((flat_start), (flat_finish)):
    landing_zone.append(i)    

first_loop = True
safe_zone = []
while True:
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]
    thrust = 4
    rotate = 0
   #-------->thrust<------- 
    if first_loop == True:
        first_loop = False
        if x in landing_zone:
            distance_x = 0
        elif x > landing_zone[-1]:
            distance_x = (x - landing_zone[-1])
        elif x < landing_zone[0]:
            distance_x = (landing_zone[0] - x)
        distance_y = y - flat_y    
        initial_distance_x = distance_x
        initial_distance_y = distance_y
        if x > landing_zone[-1]:
            safe_start = flat_start# + ((flat_finish - flat_start) // 10)
            safe_finish = flat_finish
        elif x < landing_zone[0]:
            safe_start = flat_start
            safe_finish = flat_finish# - ((flat_finish - flat_start) // 10)
        for i in range(flat_start, flat_finish):
            safe_zone.append(i)    
            
    else:
        if x in safe_zone:
            distance_x = 0
        elif x > safe_zone[-1]:
            distance_x = (x - safe_zone[-1])
        elif x < safe_zone[0]:
            distance_x = (safe_zone[0] - x)
        distance_y = y - flat_y    

    if vs < -40:
        vertical_coefficient = 40
    else:
        vertical_coefficient = abs(vs)
        
    vertical_coefficient //= 10
    
    if distance_x < 350 and vs < 10 and abs(hs) < 63:
        thrust = vertical_coefficient
   
    if distance_y < 1000 and y > 2750:
        thrust = int(thrust * 0.5)
   
    #------->rotate<-------
    
    if safe_start > x:
        rotate_direction = -1
    elif safe_finish < x:    
        rotate_direction = 1
    else:
        rotate_direction = 0
        
        
    if distance_x != 0:
        rotate = distance_x // (initial_distance_x // 90)
    
    rotate *= rotate_direction
    
    horizontal_coefficient = hs
    
    if abs(hs) > 13:
        rotate += horizontal_coefficient
    if rotate < -41:
        rotate = -41
    elif rotate > 41:
        rotate = 41
    
    if distance_y < 200 and distance_x != 0:
        rotate = int(rotate * 0.1)
    elif distance_y < 400 and distance_x != 0:
        rotate = int(rotate * 0.3)
    elif distance_y < 600 and distance_x != 0:
        rotate = int(rotate * 0.4)
    elif distance_y < 800 and distance_x != 0:
        rotate = int(rotate * 0.5)
    elif distance_y < 1000 and distance_x != 0:
        rotate = int(rotate * 0.7)
    
    if distance_y < 100 and distance_x == 0 and abs(hs) < 20:
        rotate = 0
    
    print(rotate, thrust)   