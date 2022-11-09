
def tri_bulle(tab):
  comparaison = 0
  affectation = 0
  for i in range(len(tab)-1):
    for j in range(len(tab)-1):
      if tab[j]>tab[j+1]:
        tab[j], tab[j+1] = tab[j+1], tab[j]
        affectation+=3
      comparaison+=1
        
  print(f"comparaison {comparaison}")
  print(f"affectation {affectation}")
  return tab

def tri_bulle_optimise(tab):
  comparaison = 0
  affectation = 0
  stop = True
  for i in range(len(tab)-1):
    for j in range(len(tab)-1):
      if tab[j]>tab[j+1]:
        tab[j], tab[j+1] = tab[j+1], tab[j]
        stop=False
        affectation+=3
      comparaison+=1
    if stop==True:
      break
  print(f"comparaison {comparaison}")
  print(f"affectation {affectation}")
  return tab

#print(tri_bulle([0,1,2,3,4,5]))
#print(tri_bulle_optimise([0,1,2,3,4,5]))

print(tri_bulle([5,4,3,2,1,0]))
print(tri_bulle_optimise([5,4,3,2,1,0]))
