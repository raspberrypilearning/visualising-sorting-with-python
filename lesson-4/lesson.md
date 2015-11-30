# Visualising Sorting With Python 4 - Selection Sort

In this lesson students will implement a selection sort in Python and visualise its action using matplotlib.

## Learning objectives

- To understand the mechanics and performance of the selection sort algorithm
- To be able to program a selection sort algorithm in Python

## Learning outcomes

### All students are able to

- Describe the basic mechanics of the selection sort algorithm

### Most students are able to

- Implement a selection sort in Python
- Describe the mechanics of the selection sort algorithm in detail

### Some students are able to

- Critically analyse the performance of the algorithm and identify its weaknesses 

## Lesson summary

- Students use matplotlib to visualise a single element being sorted using the algorithm
- Students implement the full sorting algorithm

## Starter

- Selection sort can easily be visualised using a pack of cards:

![animation](images/selection_sort.gif)

- The first card is looked at and assumed to be the lowest
- All the cards are iterated through, with the actual lowest value card being stored
- The lowest value card is swapped with the first card
- The second card is looked at and assumed to be the lowest
- All succeeding cards are iterated through, with the actual lowest being stored
- The lowest of the succeeding cards is swapped with the second card
- This continues until the cards are sorted

## Main development

- The students can work their way through the worksheet, slowly building up the selection sort algorithm until it is complete.

## Plenary

- Have students compare the speed of their bubble sort, insertion sort and selection sort algorithms.
- They can remove their `display()` function calls and provide the algorithms with very large lists - 5000 items should do.


## Extension

- Have students research optimisation for the selection sort algorithm.
