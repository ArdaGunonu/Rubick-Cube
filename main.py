import numpy as np
from numpy import random
import rotate

side1 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) #creating sides of cube
side2 = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
side3 = np.array([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
side4 = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])
side5 = np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
side6 = np.array([[6, 6, 6], [6, 6, 6], [6, 6, 6]])
c = " "

for x in range(30): #shuffling cube
    i = random.randint(12)
    if i == 0:
        side1, side2, side3, side4, side5 = rotate.s1(side1, side2, side3, side4, side5)
    elif i == 1:
        side1, side2, side3, side4, side5 = rotate.s1_(side1, side2, side3, side4, side5)
    elif i == 2:
        side2, side1, side3, side6, side5 = rotate.s2(side2, side1, side3, side6, side5)
    elif i == 3:
        side2, side1, side3, side6, side5 = rotate.s2_(side2, side1, side3, side6, side5)
    elif i == 4:
        side3, side1, side4, side6, side2 = rotate.s3(side3, side1, side4, side6, side2)
    elif i == 5:
        side3, side1, side4, side6, side2 = rotate.s3_(side3, side1, side4, side6, side2)
    elif i == 6:
        side4, side1, side5, side6, side3 = rotate.s4(side4, side1, side5, side6, side3)
    elif i == 7:
        side4, side1, side5, side6, side3 = rotate.s4_(side4, side1, side5, side6, side3)
    elif i == 8:
        side5, side1, side2, side6, side4 = rotate.s5(side5, side1, side2, side6, side4)
    elif i == 9:
        side5, side1, side2, side6, side4 = rotate.s5_(side5, side1, side2, side6, side4)
    elif i == 10:
        side6, side5, side2, side3, side4 = rotate.s6(side6, side5, side2, side3, side4)
    elif i == 11:
        side6, side5, side2, side3, side4 = rotate.s6_(side6, side5, side2, side3, side4)

rotate.print_(side1, side2, side3, side4, side5, side6) #printing sides

while True:
    c = input("Choose side to rotate: ") #getting command from user
    print("************\n************")

    if c == "r1": #rotating cube
        side1, side2, side3, side4, side5 = rotate.s1(side1, side2, side3, side4, side5)
    elif c == "l1":
        side1, side2, side3, side4, side5 = rotate.s1_(side1, side2, side3, side4, side5)
    elif c == "r2":
        side2, side1, side3, side6, side5 = rotate.s2(side2, side1, side3, side6, side5)
    elif c == "l2":
        side2, side1, side3, side6, side5 = rotate.s2_(side2, side1, side3, side6, side5)
    elif c == "r3":
        side3, side1, side4, side6, side2 = rotate.s3(side3, side1, side4, side6, side2)
    elif c == "l3":
        side3, side1, side4, side6, side2 = rotate.s3_(side3, side1, side4, side6, side2)
    elif c == "r4":
        side4, side1, side5, side6, side3 = rotate.s4(side4, side1, side5, side6, side3)
    elif c == "l4":
        side4, side1, side5, side6, side3 = rotate.s4_(side4, side1, side5, side6, side3)
    elif c == "r5":
        side5, side1, side2, side6, side4 = rotate.s5(side5, side1, side2, side6, side4)
    elif c == "l5":
        side5, side1, side2, side6, side4 = rotate.s5_(side5, side1, side2, side6, side4)
    elif c == "r6":
        side6, side5, side2, side3, side4 = rotate.s6(side6, side5, side2, side3, side4)
    elif c == "l6":
        side6, side5, side2, side3, side4 = rotate.s6_(side6, side5, side2, side3, side4)
    elif c == "stop":
        rotate.print_(side1, side2, side3, side4, side5, side6)
        print("STOP")
        break
    else:
        print("Please insert valid command")
        continue
    
    s1 = np.all(side1 == side1[1, 1]) #checking cube (finished or not)
    s2 = np.all(side2 == side2[1, 1])
    s3 = np.all(side3 == side3[1, 1])
    s4 = np.all(side4 == side4[1, 1])
    s5 = np.all(side5 == side5[1, 1])
    s6 = np.all(side6 == side6[1, 1])
    if s1 and s2 and s3 and s4 and s5 and s6:
        rotate.print_(side1, side2, side3, side4, side5, side6)
        print("---You Win---")
        break
    
    rotate.print_(side1, side2, side3, side4, side5, side6) #printing sides
