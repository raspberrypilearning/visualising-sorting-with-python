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
    plt.bar(range(len(some_list)),some_list)
    plt.draw()


def my_quicksort(some_list, start, stop, depth = 0):
    if stop - start < 1:
        return some_list
    else:
        pivot = some_list[start]
        left = start
        right = stop
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

        my_quicksort(some_list, start, right, depth = depth +1)
        my_quicksort(some_list, left, stop, depth = depth + 1)



a = create_random_list(1000)
my_quicksort(a, 0, len(a) - 1)
print('Done')

