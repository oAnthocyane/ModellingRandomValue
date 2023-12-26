import random
import matplotlib.pyplot as plt

N=[0]*1000
for i in range(1000):
    for k in range(1000):
        N[i]=N[i]+random.randrange(-1, 2, 2)
plt.hist(N, bins=201, range=(-100, 100))
plt.xlabel('Значение')
plt.ylabel('Количество элементов с этим значением')
plt.grid()

