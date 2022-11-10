def tri_selection(tab):
  compt = 0
  for i in range(0,len(tab)-1):
    min = i 
    compt+=1 #affectation
    for j in range(i+1,len(tab)):
      compt+=1 #comparaison
      if tab[j]<tab[min]:
        min = j
        compt+=1 #affectation
    compt+=1 #comparaison
    if (tab[min] != tab[i]):
      tmp = tab[i]
      tab[i] = tab[min]
      tab[min] = tmp
      compt+=3 #echange
  print(tab)
  return compt

#print(tri_selection([9,8,7,6,5,4,3,2,1,0]))