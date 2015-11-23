import matplotlib.pyplot as plt
from random import shuffle, choice
from time import sleep

## Interactive graph plotting
plt.ion()

def create_random_list(length):
    '''create a random list of given length'''
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return(some_list)

def display(some_list):
    '''display a list as a bar graph'''
    plt.clf()
    plt.scatter(range(len(some_list)),some_list)
    plt.draw()

def my_quicksort(some_list):
    small = []
    medium = []
    large = []
    if len(some_list) > 1:
        pivot = choice(some_list)
        for i in some_list: ## Divide the list into three new lists
            if i < pivot:
                small.append(i)
            elif i > pivot:
                large.append(i)
            else:
                medium.append(i)
        return my_quicksort(small) + medium + my_quicksort(large)
    return some_list

print(my_quicksort(create_random_list(1000)))
