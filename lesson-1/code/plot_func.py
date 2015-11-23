import matplotlib.pyplot as plt
from random import shuffle

plt.ion()

def display(some_list):
    plt.clf()
    plt.plot(range(len(some_list)),some_list)
    plt.scatter(range(len(some_list)),some_list)
    plt.draw()


a = [50 - i for i in range(50)]
b = [i**2 for i in range(20)]
c = [100**2 - i**2 for i in range(100)]

display(c)
