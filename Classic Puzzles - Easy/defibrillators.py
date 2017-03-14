#########################################
#                                       #
#  CodinGame Classic Puzzles  -  Easy   #
#           Defibrillators              #
#                                       #
#########################################

import math

lon = input()
lat = input()
n = int(input())

def_longitude = []
def_latitude = []
def_name = []

for i in range(n):
    defib = input()
    def_latitude.append(float((defib[::-1][:(defib[::-1].find(';'))][::-1]).replace(',','.')))
    defib = defib[::-1][(defib[::-1].find(';') + 1):][::-1]
    def_longitude.append(float((defib[::-1][:(defib[::-1].find(';'))][::-1]).replace(',','.')))
    defib = defib[(defib.find(';') + 1):]
    def_name.append(defib[:(defib.find(';'))])

longitude = float(lon.replace(',','.'))
latitude = float(lat.replace(',','.'))

distance = 16000000.0

for i in range(n):
    if distance > math.sqrt(((def_longitude[i] - longitude) * (math.cos((def_latitude[i] + latitude) / 2))) ** 2 + (def_latitude[i] - latitude) ** 2) * 63731:
        distance = math.sqrt(((def_longitude[i] - longitude) * (math.cos((def_latitude[i] + latitude) / 2))) ** 2 + (def_latitude[i] - latitude) ** 2) * 63731
        final_answer = def_name[i]
    
print(final_answer)