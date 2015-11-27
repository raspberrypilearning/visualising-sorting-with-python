import matplotlib.pyplot as plt
from random import shuffle
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

class Node(object):
    '''Class to create a tree'''
    def __init__(self, parent):
        self.parent = parent
        self.data = None
        self.children = []
        self.direction = None

    def add_child(self, obj):
        self.children.append(obj)

    def add_data(self, obj):
        self.data = obj

def my_quick_sort(some_list,node):
    '''Simplified Quick Sort with data being stored in a tree'''
    n = Node(node)
    node.add_child(n)
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
        n.add_data(small+equal+large)
        display(my_quick_sort(small,n) + my_quick_sort(equal,n) + my_quick_sort(large,n))
        return my_quick_sort(small,n) + my_quick_sort(equal,n) + my_quick_sort(large,n)
    else:
        n.add_data(some_list)
        return some_list

def render_leaves(obj,some_list):
    '''Assemble leaf node's data and visualise'''
    if not obj.children:
        some_list.append(obj.data)
        del(obj)
        return some_list
    else:
        return render_leaves(obj.children[(len(obj.children)-1)],some_list)
        
tree = Node(None)
sorted_list = my_quick_sort(create_random_list(50),tree)
data = render_leaves(tree,[])


