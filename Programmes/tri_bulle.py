
def tri_bulle(tab):
  compt=0
  for i in range(len(tab)-1):
    for j in range(len(tab)-1):
      if tab[j]>tab[j+1]:
        tab[j], tab[j+1] = tab[j+1], tab[j]
        compt+=3
      compt+=1
  print(tab)
  return compt

def tri_bulle_optimise(tab):
  compt = 0
  stop = True
  for i in range(len(tab)-1):
    for j in range(len(tab)-1):
      if tab[j]>tab[j+1]:
        tab[j], tab[j+1] = tab[j+1], tab[j]
        stop=False
        compt+=3
      compt+=1
    if stop==True:
      break
  print(tab)
  return compt

#print(tri_bulle([0,1,2,3,4,5,6,7,8,9]))
#print(tri_bulle_optimise([0,1,2,3,4,5,6,7,8,9]))

#print(tri_bulle([9,8,7,6,5,4,3,2,1,0]))
#print(tri_bulle_optimise([9,8,7,6,5,4,3,2,1,0]))

