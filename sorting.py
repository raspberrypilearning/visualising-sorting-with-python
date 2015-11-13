from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
pause = 0.02

def randomise():
    alist = [[randint(45,255)]*3 for i in range(64)]
    sense.set_pixels(alist)
    return(alist)

def my_bubble_sort(some_list):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(some_list)-1):
            if some_list[i][0] > some_list[i + 1][0]:
                some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
                sense.set_pixels(some_list)
                swapped = True
    return some_list

def my_insertion_sort(some_list):
    for i in range(1,len(some_list)):
        j = i
        while j > 0 and some_list[j-1][0] > some_list[j][0]:
            some_list[j],some_list[j-1]=some_list[j-1],some_list[j]
            j-=1
            sense.set_pixels(some_list)
    return some_list

def my_selection_sort(some_list):
    for i in range(len(some_list)):
        smallest_position = i
        for j in range(i+1,len(some_list)):
            if some_list[j][0] < some_list[smallest_position][0]:
                smallest_position = j
        some_list[smallest_position],some_list[i] = some_list[i],some_list[smallest_position]
        sense.set_pixels(some_list)
    

def my_quick_sort(some_list):
    small = []
    equal = []
    large = []
    if len(some_list) > 1:
        pivot = some_list[len(some_list)//2]
        for i in some_list:
            if i[0] > pivot[0]:
                large.append(i)
            elif i[0] < pivot[0]:
                small.append(i)
            else:
                equal.append(i)
        return my_quick_sort(small) + equal + my_quick_sort(large)
    else:
       return some_list     

    
#bubbleSort(randomise())

#insertionSort(randomise())

#selectionSort(randomise())

#quickSort(randomise())

#x = my_bubble_sort(randomise())
#sleep(2)
#y = my_insertion_sort(randomise())
#sleep(2)
#z = my_selection_sort(randomise())

a = my_quick_sort(randomise())
