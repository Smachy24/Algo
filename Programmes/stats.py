import tri_bulle
import tri_insertion
import tri_selection
from random import randint


def stats(min, max, step, nbr):
  """
  @param min(int): taille minimale du premier tableau
  @param max(int): taille maximale du dernier tableau
  @param step(int): ecart entre le nombre de valeurs de chaque tableau
  @param nbr(int): nombre de tableau possible pour chaque step
  CU:
    step > 0
  """
  moyenne = 0
  for i in range(min, max+1, step): 
    tab = []

    for el in range(i): #On ajoute i elements dans le tab
      tab.append(randint(-10,50))
    moyenne+=tri_bulle.tri_bulle(tab)
    print(moyenne)
  moyenne/=nbr
  print(moyenne)
    


stats(2,10,2,10)