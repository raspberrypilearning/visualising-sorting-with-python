# Visualising Sorting with Python - Quick Sort

Depending on the exam board you are following, you might want to change this lesson to use an alternative recursive sorting algorithm.

## Learning objectives

- To understand and implement the quicksort algorithm in Python

## Learning outcomes

### All students are able to

- Describe the basic workings of the Quicksort algorithm

### Most students are able to

- Implement a Quicksort algorithm in Python
- Describe in detail the mechanics of the Quicksort algorithm

### Some students are able to

- Critically analyse the performance of the algorithm and identify it's weaknesses 

## Lesson Summary

- In this lesson students will implement the Quicksort algorithm.
- Unlike previous lessons, students will not be visualising the algorithm with matplotlib, as this complicates the code significantly.

## Starter

- Ask students for a quick reminder as to what is meant by recursion.
- Ask if they can possibly think of a single operation that could be applied to a list that might eventually allow it to be sorted.

## Main development

- Students can work through the worksheet to implement a quicksort algorithm

## Plenary

- Ask students why it might be difficult to visualise the performance of the quicksort algorithm using matplotlib.
- They can put in a `display()` call into their function at various points, to see what the output is, or you can demonstrate it to them. 

## Extension

- The extension is to optimise quicksort by picking a median value for the pivot.
- A basic way of doing this is shown below.

```python
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

```
