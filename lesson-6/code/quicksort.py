from random import shuffle

def create_random_list(length):
    '''create a random list of given length'''
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return(some_list)

def my_quick_sort(some_list):
    small = []
    equal = []
    large = []
    if len(some_list) > 1:
        if some_list[0] > some_list[len(some_list)//2] > some_list[-1]:
            pivot = some_list[len(some_list)//2]
        elif some_list[len(some_list)//2] > some_list[-1] > some_list[0]:
            pivot = some_list[-1]
        else:
            pivot = some_list[0]	
        for i in some_list:
            if i > pivot:
                large.append(i)
            elif i < pivot:
                small.append(i)
            else:
                equal.append(i)
        return my_quick_sort(small) + my_quick_sort(equal) + my_quick_sort(large)
    else:
        return some_list

sorted_list = my_quick_sort(create_random_list(50))
