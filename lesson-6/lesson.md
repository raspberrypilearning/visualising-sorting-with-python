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
- This uses **quicksort in place** which can be a little more confusing than a quicksort where additional lists are created.

## Starter

- Ask students for a quick reminder as to what is meant by recursion.
- Ask if they can possibly think of a single operation that could be applied to a list that might eventually allow it to be sorted.

## Main development

- Students can work through the worksheet to implement a quicksort algorithm
- It might be worth having the students add comments to their code, describing what the process is actually doing, to help gauge understanding.

## Plenary

- Ask students to race against each other, each choosing their favourite sorting algorithm, to see which one is fastest. (Note - take out the `display()` calls to speed up the algorithms, and they can sort pretty big lists.)

## Extension

- The extension is to optimise quicksort by picking a median value for the pivot.
- This is quite a tricky task, and designed for the more able.
- One possible solution would be to do the following when the pivot is chose.

```python
        middle = (stop - start) // 2
        if some_list[start] > some_list[middle] > some_list[stop]:
            pivot = some_list[middle]
        elif some_list[start] > some_list[stop] > some_list[middle]:
            pivot = some_list[stop]
        else:
            pivot = some_list[start]
```


