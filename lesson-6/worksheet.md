# Lesson 6 - Quicksort

- The Quicksort algorithm uses recursion and is a very efficient way of sorting a list.
- Given a list such as:

```python
[39, 30, 45, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 4, 5]
```

- Sorting this list can be achieved by using a *divide and conqueor* technique. That is, breaking the problem up into a smaller problems.

- First you need to choose a single item from the list. It doesn't matter which one, so pick a random item - `22`. This is called the *pivot*

- Now you create three empty lists. The first list will hold all values less than `22` and the second list will hold the value `22` and the third will hold values greater than `22`

```python
small = [20, 5, 10, 21, 2, 4, 5]
middle = [22]
large = [39, 30, 45, 33, 61, 36, 31, 25, 80, 86, 63, 27, 85]
```

- You now have two lists, that both need sorting. So you can pick a random item from each list and again divide them into two lists. This process can be continued, until the final lists only have one element in them.

- This is best visualised in a *tree* data structure.

```python
    [39, 30, 45, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 4, 5]

   [20, 5, 10, 21, 2, 4, 5]               [22]            [39, 30, 45, 33, 61, 36, 31 25, 80, 86, 63, 27, 85]

  [5, 2, 4]   [10]   [20, 21]                          [30, 31, 22, 25, 27] [33] [39, 45, 61, 35, 80, 86, 63, 85]

 [2] [4] [5]         [20] [21]                       [22] [30, 31, 25, 27]        [39, 35] [45] [61, 80, 86, 62, 85]

                                                          [30, 25, 27] [31]       [39] [35]     [61, 62] [80], [86, 85]

                                                          [25] [27] [30]                        [61] [62]      [85] [86]     
```
