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


def my_quicksort(some_list, start, stop):
    if stop - start < 1:
        return None
    else:
        pivot, left, right = some_list[start], start, stop
        while left <= right:
            while some_list[left] < pivot:
                left += 1
            while some_list[right] > pivot:
                right -= 1
            if left <= right:
                some_list[left], some_list[right] = some_list[right], some_list[left]
                left += 1
                right -= 1
        display(some_list)
        
        my_quicksort(some_list, start, right)
        my_quicksort(some_list, left, stop)
        print(pivot)
        

#my_list = [6,4,8,2,9,1]
my_list = create_random_list(500)
my_quicksort(my_list,0,5)
print(my_list)
