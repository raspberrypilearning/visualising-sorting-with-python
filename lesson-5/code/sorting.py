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

def my_bubble_sort(some_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(some_list)-1):
            if some_list[i] > some_list[i + 1]:
                some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
                #display(some_list)
                swapped = True
        display(some_list)
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

#my_bubble_sort(create_random_list(250))
# #my_insertion_sort(create_random_list(250))
# #my_selection_sort(create_random_list(250))

# tree = []
# parent = 1

# def my_quick_sort(some_list):
#     global parent
#     small = []
#     equal = []
#     large = []
#     if len(some_list) > 1:
#         pivot = some_list[len(some_list)//2]
#         for i in some_list:
#             if i > pivot:
#                 large.append(i)
#             elif i < pivot:
#                 small.append(i)
#             else:
#                 equal.append(i)
#         tree.append({'parent':parent,'data':small})
#         tree.append({'parent':parent,'data':equal})
#         tree.append({'parent':parent,'data':large})
#         parent += 1
#         new_list = my_quick_sort(small) + my_quick_sort(equal) + my_quick_sort(large)
#         #display(some_list) ##Visualising what is happening but not exactly clear
#         #tree.append([level, new_list])
#         return new_list
#     else:
#         #tree.append([level, some_list])
#         return some_list     

# #my_bubble_sort(create_random_list(250))
# #my_insertion_sort(create_random_list(250))
# #my_selection_sort(create_random_list(250))
# data = create_random_list(50)
# tree.append({'parent':0,'data':data})
# my_quick_sort(data)

# count = 0
# hold = [i['data'] for i in tree if i['parent'] == count]        

# class Node(object):
#     def __init__(self, parent):
#         self.parent = parent
#         self.data = None
#         self.children = []

#     def add_child(self, obj):
#         self.children.append(obj)

#     def add_data(self, obj):
#         self.data = obj

# tree = []

# def my_quick_sort(some_list,node):
#     n = Node(some_list)
#     small = []
#     equal = []
#     large = []
#     if len(some_list) > 1:
#         pivot = some_list[len(some_list)//2]
#         for i in some_list:
#             if i > pivot:
#                 large.append(i)
#             elif i < pivot:
#                 small.append(i)
#             else:
#                 equal.append(i)
#         n.add_data(small+equal+large)
#         n.add_child(small)
#         n.add_child(equal)
#         n.add_child(large)
#         tree.append(n)
#         return my_quick_sort(small) + my_quick_sort(equal) + my_quick_sort(large)
#     else:
#         tree.append(n)
#         return some_list

# sorted_list = my_quick_sort(create_random_list(50))

# def find_parent(child):
#     for i in tree:
#         if child in i.children:
#             return i.parent

class Node(object):
    def __init__(self, parent):
        self.parent = None
        self.data = None
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def add_data(self, obj):
        self.data = obj

def my_quick_sort(some_list,node):
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
        return my_quick_sort(small,n) + my_quick_sort(equal,n) + my_quick_sort(large,n)
    else:
        n.add_data(some_list)
        n.add_child(None)
        return some_list

tree = Node(None)
sorted_list = my_quick_sort(create_random_list(50),tree)
