from random import *

# tableau = []

# for i in range(randint(1, 10)):
#     tableau.append(randint(1, 10))

# print('List:', tableau)

def triInsertion(t):
    for i in range (len(t)):
        cle = t[i]
        
        j = i-1
        while j >= 0 and cle < t[j]:
            t[j], t[j+1] = t[j+1], t[j]
            j -= 1
t = [randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50)]
triInsertion(t)
print (t)