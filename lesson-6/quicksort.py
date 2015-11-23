from random import choice, shuffle

def create_random_list(length):
    '''create a random list of given length'''
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return(some_list)

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
        return my_quick_sort(small) + medium + my_quick_sort(large)
    return some_list			
