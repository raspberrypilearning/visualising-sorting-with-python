import matplotlib.pyplot as plt
from random import randint

plt.ion()

def create_random():
    some_list = [randint(0,20) for i in range(20)]
    return(some_list)

def my_bubble_sort(some_list):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(some_list)-1):
            if some_list[i] > some_list[i + 1]:
                some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
                display(some_list)
                swapped = True
    return some_list

def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.draw()

my_bubble_sort(create_random())
