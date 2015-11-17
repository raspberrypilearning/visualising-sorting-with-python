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

def my_bubble_sort(some_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(some_list)-1):
            if some_list[i] > some_list[i + 1]:
                some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
                display(some_list)
                swapped = True
    return some_list

def my_insertion_sort(some_list):
    for i in range(1,len(some_list)):
        while i > 0 and some_list[i-1] > some_list[i]:
            some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
            i-=1
            display(some_list)
    return some_list

def my_selection_sort(some_list):
    for i in range(len(some_list)):
        smallest_value = i

        for j in range(i+1,len(some_list)):
            if some_list[j] < some_list[smallest_value]:
                smallest_value = j

        some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
        display(some_list)	

    return some_list
    
def my_quick_sort(some_list):
    small = []
    equal = []
    large = []
    if len(some_list) > 1:
        pivot = some_list[len(some_list)//2]
        for i in some_list:
            if i > pivot:
                large.append(i)
            elif i < pivot:
                small.append(i)
            else:
                equal.append(i)
        new_list = my_quick_sort(small) + equal + my_quick_sort(large)
        display(new_list)
        return new_list
    else:
        display(some_list)
        return some_list     

#my_bubble_sort(create_random_list(100))
#my_insertion_sort(create_random_list(100))
my_selection_sort(create_random_list(200))
#my_quick_sort(create_random_list(100))

