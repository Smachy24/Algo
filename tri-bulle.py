
def tri_bulle(tab):
  comparaison = 0
  affectation = 0

  for i in range(len(tab)):
    for j in range(len(tab)-1):
      if tab[j]>tab[j+1]:
        tab[j], tab[j+1] = tab[j+1], tab[j]
        affectation+=3
      comparaison+=1
        
  print(f"comparaison {comparaison}")
  print(f"affectation {affectation}")
  return tab


print(tri_bulle([9,8,7,6,5,4]))
print(tri_bulle([0,1,2,3,4,5]))