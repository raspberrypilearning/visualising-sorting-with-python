import matplotlib.pyplot as plt
from random import shuffle
from time import sleep

plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return(some_list)

def display(some_list):
    plt.clf()
    plt.scatter(range(len(some_list)),some_list)
    plt.draw()

def my_selection_sort(some_list):
    for i in range(len(some_list)):
        smallest_value = i
        for j in range(i+1,len(some_list)):
            if some_list[j] < some_list[smallest_value]:
                smallest_value = j

        some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
        display(some_list)	

    return some_list

my_selection_sort(create_random_list(200))


