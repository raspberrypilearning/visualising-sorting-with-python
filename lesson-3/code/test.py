import matplotlib.pyplot as plt
from random import shuffle

plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return(some_list)

def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.draw()

some_list = [4,2,3,1]

i = 3

while some_list[i-1] > some_list[i]:
    some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
    print(i)
    i -= 1
