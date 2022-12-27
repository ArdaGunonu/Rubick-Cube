import numpy as np
from numpy import random

def s1(s1, s2, s3, s4, s5): #rotating side 1 to right function
    s1 = np.rot90(s1, k=-1) #rotating side 1 to right
    temp = np.copy(s2)
    s2[0, 0], s2[0, 1], s2[0, 2] = s3[0, 0], s3[0, 1], s3[0, 2] #rotating edges that conjoint to side 1
    s3[0, 0], s3[0, 1], s3[0, 2] = s4[0, 0], s4[0, 1], s4[0, 2]
    s4[0, 0], s4[0, 1], s4[0, 2] = s5[0, 0], s5[0, 1], s5[0, 2]
    s5[0, 0], s5[0, 1], s5[0, 2] = temp[0, 0], temp[0, 1], temp[0, 2]
    return s1, s2, s3, s4, s5

def s1_(s1, s2, s3, s4, s5): #rotating side 1 to left function
    s1 = np.rot90(s1, k=1) #rotating side 1 to right
    temp = np.copy(s2)
    s2[0, 0], s2[0, 1], s2[0, 2] = s5[0, 0], s5[0, 1], s5[0, 2] #rotating edges that conjoint to side 1
    s5[0, 0], s5[0, 1], s5[0, 2] = s4[0, 0], s4[0, 1], s4[0, 2]
    s4[0, 0], s4[0, 1], s4[0, 2] = s3[0, 0], s3[0, 1], s3[0, 2]
    s3[0, 0], s3[0, 1], s3[0, 2] = temp[0, 0], temp[0, 1], temp[0, 2]
    return s1, s2, s3, s4, s5

def s2(s2, s1, s3, s6, s5):#rotating side 2 to right function
    s2 = np.rot90(s2, k=-1) #rotating side 2 to right
    temp = np.copy(s1)
    s1[0, 0], s1[1, 0], s1[2, 0] = s5[2, 2], s5[1, 2], s5[0, 2] #rotating edges that conjoint to side 2
    s5[0, 2], s5[1, 2], s5[2, 2] = s6[0, 2], s6[1, 2], s6[2, 2]
    s6[0, 2], s6[1, 2], s6[2, 2] = s3[2, 0], s3[1, 0], s3[0, 0]
    s3[0, 0], s3[1, 0], s3[2, 0] = temp[0, 0], temp[1, 0], temp[2, 0]
    return s2, s1, s3, s6, s5

def s2_(s2, s1, s3, s6, s5):#rotating side 2 to left function
    s2 = np.rot90(s2, k=1) #rotating side 2 to left
    temp = np.copy(s1)
    s1[0, 0], s1[1, 0], s1[2, 0] = s3[0, 0], s3[1, 0], s3[2, 0] #rotating edges that conjoint to side 2
    s3[0, 0], s3[1, 0], s3[2, 0] = s6[2, 2], s6[1, 2], s6[0, 2]
    s6[0, 2], s6[1, 2], s6[2, 2] = s5[0, 2], s5[1, 2], s5[2, 2]
    s5[0, 2], s5[1, 2], s5[2, 2] = temp[2, 0], temp[1, 0], temp[0, 0]
    return s2, s1, s3, s6, s5

def s3(s3, s1, s4, s6, s2): #rotating side 3 to right function
    s3 = np.rot90(s3, k=-1) #rotating side 3 to right
    temp = np.copy(s1)
    s1[2, 0], s1[2, 1], s1[2, 2] = s2[2, 2], s2[1, 2], s2[0, 2] #rotating edges that conjoint to side 3
    s2[0, 2], s2[1, 2], s2[2, 2] = s6[2, 2], s6[2, 1], s6[2, 0]
    s6[2, 2], s6[2, 1], s6[2, 0] = s4[2, 0], s4[1, 0], s4[0, 0]
    s4[2, 0], s4[1, 0], s4[0, 0] = temp[2, 2], temp[2, 1], temp[2, 0]
    return s3, s1, s4, s6, s2

def s3_(s3, s1, s4, s6, s2): #rotating side 3 to left function
    s3 = np.rot90(s3, k=1) #rotating side 3 to left
    temp = np.copy(s1)
    s1[2, 0], s1[2, 1], s1[2, 2] = s4[0, 0], s4[1, 0], s4[2, 0] #rotating edges that conjoint to side 3
    s4[2, 0], s4[1, 0], s4[0, 0] = s6[2, 2], s6[2, 1], s6[2, 0]
    s6[2, 2], s6[2, 1], s6[2, 0] = s2[0, 2], s2[1, 2], s2[2, 2]
    s2[0, 2], s2[1, 2], s2[2, 2] = temp[2, 2], temp[2, 1], temp[2, 0]
    return s3, s1, s4, s6, s2

def s4(s4, s1, s5, s6, s3): #rotating side 4 to right function
    s4 = np.rot90(s4, k=-1) #rotating side 4 to right
    temp = np.copy(s1)
    s1[0, 2], s1[1, 2], s1[2, 2] = s3[0, 2], s3[1, 2], s3[2, 2] #rotating edges that conjoint to side 4
    s3[0, 2], s3[1, 2], s3[2, 2] = s6[2, 0], s6[1, 0], s6[0, 0]
    s6[2, 0], s6[1, 0], s6[0, 0] = s5[2, 0], s5[1, 0], s5[0, 0]
    s5[2, 0], s5[1, 0], s5[0, 0] = temp[0, 2], temp[1, 2], temp[2, 2]
    return s4, s1, s5, s6, s3

def s4_(s4, s1, s5, s6, s3): #rotating side 4 to left function
    s4 = np.rot90(s4, k=1) #rotating side 4 to left
    temp = np.copy(s1)
    s1[0, 2], s1[1, 2], s1[2, 2] = s5[2, 0], s5[1, 0], s5[0, 0] #rotating edges that conjoint to side 4
    s5[2, 0], s5[1, 0], s5[0, 0] = s6[2, 0], s6[1, 0], s6[0, 0]
    s6[2, 0], s6[1, 0], s6[0, 0] = s3[0, 2], s3[1, 2], s3[2, 2]
    s3[0, 2], s3[1, 2], s3[2, 2] = temp[0, 2], temp[1, 2], temp[2, 2]
    return s4, s1, s5, s6, s3

def s5(s5, s1, s2, s6, s4): #rotating side 5 to right function
    s5 = np.rot90(s5, k=-1) #rotating side 5 to right
    temp = np.copy(s1)
    s1[0, 0], s1[0, 1], s1[0, 2] = s4[0, 2], s4[1, 2], s4[2, 2] #rotating edges that conjoint to side 5
    s4[0, 2], s4[1, 2], s4[2, 2] = s6[0, 0], s6[0, 1], s6[0, 2]
    s6[0, 0], s6[0, 1], s6[0, 2] = s2[2, 0], s2[1, 0], s2[0, 0]
    s2[2, 0], s2[1, 0], s2[0, 0] = temp[0, 0], temp[0, 1], temp[0, 2]
    return s5, s1, s2, s6, s4

def s5_(s5, s1, s2, s6, s4): #rotating side 5 to left function
    s5 = np.rot90(s5, k=1) #rotating side 5 to left
    temp = np.copy(s1)
    s1[0, 0], s1[0, 1], s1[0, 2] = s2[2, 0], s2[1, 0], s2[0, 0] #rotating edges that conjoint to side 5
    s2[2, 0], s2[1, 0], s2[0, 0] = s6[0, 0], s6[0, 1], s6[0, 2]
    s6[0, 0], s6[0, 1], s6[0, 2] = s4[0, 2], s4[1, 2], s4[2, 2]
    s4[0, 2], s4[1, 2], s4[2, 2] = temp[0, 0], temp[0, 1], temp[0, 2]
    return s5, s1, s2, s6, s4

def s6(s6, s5, s2, s3, s4): #rotating side 6 to right function
    s6 = np.rot90(s6, k=-1) #rotating side 6 to right
    temp = np.copy(s5)
    s5[2, 2], s5[2, 1], s5[2, 0] = s4[2, 2], s4[2, 1], s4[2, 0] #rotating edges that conjoint to side 6
    s4[2, 2], s4[2, 1], s4[2, 0] = s3[2, 2], s3[2, 1], s3[2, 0]
    s3[2, 2], s3[2, 1], s3[2, 0] = s2[2, 2], s2[2, 1], s2[2, 0]
    s2[2, 2], s2[2, 1], s2[2, 0] = temp[2, 2], temp[2, 1], temp[2, 0]
    return s6, s5, s2, s3, s4

def s6_(s6, s5, s2, s3, s4): #rotating side 6 to left function
    s6 = np.rot90(s6, k=1) #rotating side 6 to left
    temp = np.copy(s5)
    s5[2, 2], s5[2, 1], s5[2, 0] = s2[2, 2], s2[2, 1], s2[2, 0] #rotating edges that conjoint to side 6
    s2[2, 2], s2[2, 1], s2[2, 0] = s3[2, 2], s3[2, 1], s3[2, 0]
    s3[2, 2], s3[2, 1], s3[2, 0] = s4[2, 2], s4[2, 1], s4[2, 0]
    s4[2, 2], s4[2, 1], s4[2, 0] = temp[2, 2], temp[2, 1], temp[2, 0]
    return s6, s5, s2, s3, s4

def print_(s1, s2, s3, s4, s5, s6):
    print("Side 1")
    for x in s1:
    
        print(x)
    print("--------")
    print("Side 2")
    for x in s2:
        print(x)
    print("--------")
    print("Side 3")
    for x in s3:
        print(x)
    print("--------")
    print("Side 4")
    for x in s4:
        print(x)
    print("--------")
    print("Side 5")
    for x in s5:
        print(x)
    print("--------")
    print("Side 6")
    for x in s6:
        print(x)
    print("--------")