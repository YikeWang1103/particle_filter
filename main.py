# In this exercise, write a program that will
# run your previous code twice.
# Please only modify the indicated area below!

from math import *
import random
import matplotlib.pyplot as plt
import numpy as np

from robot import landmarks, world_size, robot, eval, plotLandmarks

myrobot = robot()
myrobot = myrobot.move(0.1, 5.0)
Z = myrobot.sense()
N = 1000
T = 20 #Leave this as 10 for grading purposes.

p = []
for i in range(N):
    r = robot()
    r.set_noise(0.05, 0.05, 5.0)
    p.append(r)
print(eval(myrobot,p))

plotLandmarks(landmarks)

for t in range(T):
    myrobot = myrobot.move(0.1, 5.0)
    Z = myrobot.sense()

    p2 = []
    for i in range(N):
        p2.append(p[i].move(0.1, 5.0))
    p = p2

    w = []
    for i in range(N):
        w.append(p[i].measurement_prob(Z))

    p3 = []
    index = int(random.random() * N)
    beta = 0.0
    mw = max(w)
    for i in range(N):
        beta += random.random() * 2.0 * mw
        while beta > w[index]:
            beta -= w[index]
            index = (index + 1) % N
        p3.append(p[index])
    p = p3
    #enter code here, make sure that you output 10 print statements.
    print(eval(myrobot,p))
