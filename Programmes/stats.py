import tri_bulle
import tri_insertion
import tri_selection
from random import randint


def stats(min, max, step, nbr, tri):
  """
  @param min(int): taille minimale du premier tableau
  @param max(int): taille maximale du dernier tableau
  @param step(int): ecart entre le nombre de valeurs de chaque tableau
  @param nbr(int): nombre de tableau possible pour chaque step
  CU:
    step > 0
  """
  for i in range(min, max+1, step): 
    moyenne=0
    for j in range(nbr):
      tab = []
      for el in range(i): #On ajoute i elements dans le tab
        tab.append(randint(-10,50))
      moyenne+=tri(tab)
    moyenne/=nbr
    print(f"{i} : {moyenne}")
    

print(stats(10,20,5,10, tri_bulle.tri_bulle_optimise))
print("---------------------------------------")
print(stats(10,20,5,10, tri_bulle.tri_bulle))
print("---------------------------------------")
print(stats(10,20,5,10, tri_insertion.triInsertion))
print("---------------------------------------")
print(stats(10,20,5,10, tri_selection.tri_selection))