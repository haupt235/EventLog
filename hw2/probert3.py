import math
import numpy
# Part i
# Subsection a: distance between interactions

position_f = (3,4,5)
position_i = (8,1,2)

def collision_distance(position_i, position_f):
    y=[]
    for x in range(len(position_i)):  
        y+=[(position_f[x]-position_i[x])**2]
    return math.sqrt(sum(y))

    
print(collision_distance(position_i, position_f))

#Subsection b: unit vectors

def unit_vector(position_i, position_f):
    z=[]
    a=[]
    for x in range(len(position_i)):  
        z+=[position_f[x]-position_i[x]]
    for x in range(len(position_i)):   
        a+=[z[x]/collision_distance(position_i, position_f)]
    return a

print(unit_vector(position_i, position_f))

# Subsection c: energy of particle in eV

MeV= 2.3

def eV_converter(MeV):
    eV=MeV*1e6
    return eV

print(eV_converter(MeV))

# Part ii
# The best container to store information about an event that is classified in some way is a dictionary. This is better than a tuple because it can change order and be concatenated, better than a list as each item can be categorized, and better than a set because the concepts of set theory aren't useful for such cataloging.

part_num = 43
element = (1,2)
reaction_code = 102

event_dict = {'Particle Number':part_num, 'Final Event Location': position_f, 'Direction of Particle': unit_vector(position_i, position_f),'Particle Energy [eV]':eV_converter(MeV), 'Element (atomic and mass numbers)': element, 'Reaction Code': reaction_code}

# Part iii
# The best configuration to store many events would be a list of the dictionaries for each event, as it would keep information about each particular event together. This is more intuitive than having many lists that are then compiled in a dictionary as that would require far more work to modify anything in each particular list. The many dictionaries allow for discrete data addition. 

event_log = []
for x in range(3):
    event_log.append(event_dict)
print(event_log)

# Part iv
# Subsection a: change in energy between fifth and sixth event

event_log[6]["Particle Energy [eV]"]-event_log[5]["Particle Energy [eV]"]

# Subsection b: calculate distance between 7th and 8th event

collision_distance(event_log[7]["Final Event Location"],event_log[8]["Final Event Location"])

# Subsection c: see which unit vector (4th or 9th) is more aligned with the z axis

d_4 = numpy.dot(event_log[1]["Direction of Particle"], (0,0,1))
d_9 = numpy.dot(event_log[2]["Direction of Particle"], (0,0,1))

if d_4>d_9 == True
    print ('4th unit vector is more aligned with the z axis.')
    elif d_4=d_9 == True
        print('They are equal.')
        elif print('9th unit vector is more aligned with the z axis.')




