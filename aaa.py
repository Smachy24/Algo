from random import *

def triInsertion(t):
    comp = 0
    affec = 0
    
    for i in range (1, len(t)):
        cle = t[i]
        
        j = i-1
        affec+=2
        comp+=2
        while j >= 0 and cle < t[j]:
            t[j+1] = t[j]
            j -= 1
            t[j+1] = cle
            affec += 5 
    print('Voici le nombre de comparaisons effectuées :', comp)
    print("Voici le nombre d'affectations effectuées :", affec)
    
#t = [randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50)]
t = [9 ,8 ,7 ,6 ,5 ,4, 3, 2, 1, 0]

triInsertion(t)
print (t)