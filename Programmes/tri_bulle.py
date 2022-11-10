
def tri_bulle(tab):
  compt=0
  for i in range(len(tab)-1):
    for j in range(len(tab)-1):
      compt+=1 #comparaison
      if tab[j]>tab[j+1]:
        tab[j], tab[j+1] = tab[j+1], tab[j]
        compt+=3 #echange
      
  #print(tab)
  return compt

def tri_bulle_optimise(tab):
  compt = 0
  stop = True
  compt+=1 #affectation
  for i in range(len(tab)-1):
    for j in range(len(tab)-1):
      compt+=1 #comparaison
      if tab[j]>tab[j+1]:
        tab[j], tab[j+1] = tab[j+1], tab[j]
        stop=False
        compt+=4  #affectation + echange
    compt+=1 #comparaison
    if stop==True:
      break
  #print(tab)
  return compt

#print(tri_bulle([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))
#print(tri_bulle_optimise([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))

#print(tri_bulle([19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]))
#print(tri_bulle_optimise([19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]))

