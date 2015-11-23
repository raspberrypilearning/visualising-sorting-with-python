import matplotlib.pyplot as plt
from random import shuffle

plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return(some_list)

def display(some_list):
    plt.clf()
    plt.scatter(range(len(some_list)),some_list)
    plt.draw()

def my_bubble_sort(some_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(some_list)-1):
            if some_list[i] > some_list[i + 1]:
                some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
                swapped = True
#        display(some_list)
    return some_list

print(my_bubble_sort(create_random_list(5000))[-1])
