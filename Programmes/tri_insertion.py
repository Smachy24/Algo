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

print(triInsertion([9,8,7,6,5,4,3,2,1,0]))
