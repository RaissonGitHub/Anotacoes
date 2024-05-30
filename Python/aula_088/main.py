# count é um iterador sem fim
# ao contrario de range, count não tem fim
from itertools import count

c1 = count()
# pode colocar start e step tambem
# c2 = count(10, 2) # por exemplo
for i in c1:
    if i == 100:
        break
    print(i)