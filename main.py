import cv2
import matplotlib.pyplot as plt
from pypot import vrep
from pypot.creatures import PoppyErgoJr
import random as r
from math import pi
from math import sqrt
from time import sleep

#C'était donné au début j'sais pas a quoi ça sert
#img=poppy.camera.frame
#plt.imshow(cv2.cvtColor(img.cv2.COLOR_BGR2RGB))

# Fermeture des connexion en entrant dans le programme afin d'éviter les bugs
vrep.close_all_connections()
poppy = PoppyErgoJr(simulator='vrep', scene='poppy_ergo_jr_holder.ttt', camera='dummy')
        

def showpos():
    print(poppy.m1)
    print(poppy.m2)
    print(poppy.m3)
    print(poppy.m4)
    print(poppy.m5)
    print(poppy.m6)
    
    
def default():
    poppy.m1.goal_position = 0
    poppy.m2.goal_position = 0
    poppy.m3.goal_position = 0
    poppy.m4.goal_position = 0
    poppy.m5.goal_position = 0
    poppy.m6.goal_position = 0
    

# def closeall():
#     poppy.stop_simulation()
#     vrep.close_all_connections()


def setfly(x,y,z,r,nbfly):
    points = []
    for i in range(0, nbfly):
        factor = np.random.uniform(0.3,1)
        ir = r * factor
        itheta = np.arccos(np.random.uniform(-1,1))
        iphi = np.random.uniform(0,2*np.pi)
        ix = x + ir * np.sin(itheta) * np.cos(iphi)
        iy = y + ir * np.sin(itheta) * np.sin(iphi)
        iz = abs(z + ir * np.cos(itheta))
        points.append((ix,iy,iz))
    return points


def translategraph(all_pos):
    arr = [[],[],[]]
    y = 0
    while y < len(all_pos):
        arr[0].append(all_pos[y][0])
        arr[1].append(all_pos[y][1])
        arr[2].append(all_pos[y][2])
        y += 1
    return arr


def getactualpos():
    pos = poppy.chain.end_effector
    actualpos = [[pos[0],pos[1],pos[2]]]
    return actualpos


def old(init_pos, all_pos):
    dist = []
    for i in all_pos:
        dist.append([sqrt(((init_pos[0] - i[0]) ** 2) + ((init_pos[1] - i[1]) ** 2)+((init_pos[2] - i[2]) ** 2)), i])
    dist.sort()
    print(dist)
    nearest = dist[0]
    return nearest


def sortbynearest(arr,sort_final):
    sort = []
    l = len(arr[1][0])
    pos_min = 0
    if 0 < l:
        i = 0
        while i < l:
            sort.append([sqrt(((arr[0][0] - arr[1][0][i]) ** 2) + ((arr[0][1] - arr[1][1][i]) ** 2)+((arr[0][2] - arr[1][2][i]) ** 2)), i])
            i += 1
           
        sort.sort()
        pos_min = sort[0][1]
        arr.insert(0,[arr[1][0][pos_min], arr[1][1][pos_min], arr[1][2][pos_min]])
        sort_final.append(arr[0])
        arr.pop(1)
        arr[1][0].pop(pos_min)
        arr[1][1].pop(pos_min)
        arr[1][2].pop(pos_min)
        
        sortbynearest(arr,sort_final)
        
    else:
        return sort_final
    
  
def creategraph(xyz):
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    fig = plt.figure()
    ax = plt.gca(projection='3d')
    ax.plot(x, y, z)
    

def creategraph2D(xy):
    x = xy[0]
    y = xy[1]
    fig, ax = plt.subplots()
    ax.scatter(x,y)
    plt.show()
    
    
def moove(pos):
    x = 0
    for i in pos:
        x = x + 1
        print("")
        print(x)
        print(i)
        angles = poppy.chain.inverse_kinematics(i)
        print(angles)
        print(angles[1]*(180/pi))
        poppy.m1.goto_position(angles[1]*(180/pi),2)
        poppy.m2.goto_position(angles[2]*(180/pi),2)
        poppy.m3.goto_position(angles[3]*(180/pi),2)
        poppy.m4.goto_position(angles[4]*(180/pi),2)
        poppy.m5.goto_position(angles[5]*(180/pi),2)
        poppy.m6.goto_position(angles[6]*(180/pi),2)
        sleep(2)
        

def main():
    fly = setfly(0,0,0,0.2,10)
    fly = translategraph(fly)
    init_pos = getactualpos()
    init_pos.append(fly)
    sort_final = []
    fly = sortbynearest(init_pos,sort_final)
    path = translategraph(sort_final)
    
    print(sort_final)
    print("")
    
    creategraph(path)
    plt.show()
    
    moove(sort_final)
 
    
def rotate():
    i = 0
    graph = [[],[]]
    while i < 180:
        print(i)
        poppy.m1.goto_position(i,5,wait=True)
        graph[0].append(poppy.chain.end_effector[0])
        graph[1].append(poppy.chain.end_effector[1])
        poppy.m1.goto_position(i+180,5,wait=True)
        graph[0].append(poppy.chain.end_effector[0])
        graph[1].append(poppy.chain.end_effector[1])
        i = i + 15
    
    creategraph2D(graph)
    

# Fonction de test afin de vérifier la position dans le plan(x,y) de la pince    
# rotate()

# Fonction principale permettant de créer les mouches aléatoirement et mettre en marche le robot
main()

# sleep(4)

# Fermeture de la simulation et de la connexion
poppy.stop_simulation()
vrep.close_all_connections()

