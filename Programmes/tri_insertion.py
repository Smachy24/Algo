from random import *

def triInsertion(t):
    comp = 0
    for i in range (1, len(t)):
        cle = t[i]  
        j = i-1   
        comp+=4 # 2 affectations + 2 comparaisons
        while j >= 0 and cle < t[j]:
            t[j+1] = t[j]
            j -= 1
            t[j+1] = cle
            comp += 3 # echange
    #print(t)
    return comp
#t = [randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50), randint(-10, 50)]
#print(triInsertion(t))

# dans le meilleur des cas 36 au compteur
# dans le pire des cas 261 au compteur