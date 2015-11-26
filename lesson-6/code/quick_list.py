import matplotlib.pyplot as plt
from random import shuffle
from time import sleep
from collections import defaultdict

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

def my_quick_sort(some_list,results):
    '''Simplified Quick Sort with data being stored in a tree'''
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
        results['small']=small
        results['equal']=equal
        results['large']=large
        results['left']={}
        results['right']={}
        results['centre']={}
        return my_quick_sort(small,results['left']) + my_quick_sort(equal,results['centre']) + my_quick_sort(large,results['right'])
    else:
        return some_list

def render(a_dict):
    if not a_dict['right'] and not a_dict['left'] and not a_dict['centre']:
        print('recursing')
        return a_dict['small']+a_dict['equal']+a_dict['large']
    else:
        return render(a_dict['left'])+render(a_dict['centre'])+render(a_dict['right'])

        
    
some_dict = {}
sorted_list = my_quick_sort(create_random_list(50),some_dict)




