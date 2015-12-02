# Visualising Sorting With Python 6 - Quicksort

The quicksort algorithm uses recursion and is a very efficient way of sorting a list. Given a list such as:

```python
[39, 30, 45, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 4, 5]
```

sorting this list can be achieved by using a *divide and conquer* technique, breaking the problem up into smaller problems.

- First you need to choose a single item from the list. It doesn't matter which one, so pick a random item: `22`. This is called the *pivot*.

- Now you create three empty lists. The first list will hold all values less than `22`, the second list will hold the value `22`, and the third will hold values greater than `22`:

	```python
	small = [20, 5, 10, 21, 2, 4, 5]
	middle = [22]
	large = [39, 30, 45, 33, 61, 36, 31, 25, 80, 86, 63, 27, 85]
	```

- You now have two lists that must be sorted, so you can pick a random item from each list and again divide them into two lists. This process can be continued, until the final lists only have one element in them. This is best visualised in a *tree* data structure:

	```python
		[39, 30, 45, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 4, 5]
					/                 |                                  \
	   [20, 5, 10, 21, 2, 4, 5]      [22]        [39, 30, 45, 33, 61, 36, 31 25, 80, 86, 63, 27, 85]
		   /        |        \                        /         |                \
	  [5, 2, 4, 5] [10]   [20, 21]            [30, 31, 25, 27] [33] [39, 45, 61, 35, 80, 86, 63, 85]
	   /  |  \             /   \             /       |                  /     |           \
	 [2] [4] [5, 5]      [20] [21]         [25] [30, 31, 27]        [39, 35] [45] [61, 80, 86, 62, 85]
													/    \           /   \           /     |       \
												[30 27] [31]       [35] [39]     [61, 62] [80], [86, 85]
												 /   \                            /   \          /   \
											   [27] [30]                        [61] [62]      [85] [86]
	```

- If you now read *left to right* across the tree, looking at the last item(s) in each branch, called *leaf nodes*, you'll see that they are all in order. Now the leaf nodes must be assembled back into a single list.

## Implementing a quicksort algorithm in Python

Now you know what the quicksort algorithm is, you can try and code it. You'll need another method from the `random` library to do this, so edit the lines at the top of your file to read:

```python
from random import shuffle, choice

some_list = [39, 30, 45, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 4, 5]
```

1. Start by creating the three empty lists:

	```python
	small = []
	medium = []
	large = []
	```

1. Once a list only has one item, it is sorted. This is our *base case*, so you need to identify lists with more than one item:

	```python
	small = []
	medium = []
	large = []
	if len(some_list) > 1:
	```

1. Next, you choose a pivot. For now, it doesn't matter which item you choose as a pivot, so it may as well be random:

	```python
	small = []
	medium = []
	large = []
	if len(some_list) > 1:
		pivot = choice(some_list)
	```

1. If an item is smaller than the pivot, it goes in the `small` list. If it's larger than the pivot, it goes in the `large` list. Otherwise, it can go in the `medium` list:

	```python
	small = []
	medium = []
	large = []
	if len(some_list) > 1:
		pivot = choice(some_list)
		for i in some_list: # Divide the list into three new lists
				if i < pivot:
					small.append(i)
				elif i > pivot:
					large.append(i)
				else:
					medium.append(i)
	```

1. You can now check that your code is working. Save and run it, then use the interpreter to have a look at the contents of `small`, `medium`, and `large`.

## Making a recursive function

1. Now that the main list has been divided, you need to run `small` and `large` back through the algorithm. To do this you'll need to turn it into a function:

	```python
	def my_quicksort(some_list):
		small = []
		medium = []
		large = []
		if len(some_list) > 1:
			pivot = choice(some_list)
			for i in some_list: # Divide the list into three new lists
					if i < pivot:
						small.append(i)
					elif i > pivot:
						large.append(i)
					else:
						medium.append(i)
	```

1. The `small` and `large` lists can be recursed back through the algorithm in the `return`:

	```python
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
			return my_quicksort(small) + medium + my_quicksort(large)
	```				

1. Finally, you need to handle the *base case* and return lists with only one item:

	```python
	def my_quicksort(some_list):
		small = []
		medium = []
		large = []
		if len(some_list) > 1:
			pivot = choice(some_list)
			for i in some_list: # Divide the list into three new lists
					if i < pivot:
						small.append(i)
					elif i > pivot:
						large.append(i)
					else:
						medium.append(i)
			return my_quicksort(small) + medium + my_quicksort(large)
		return some_list			
	```

1. Try your new recursive quicksort function by calling it:

	```python
	print(my_quicksort(some_list))
	```

1. Or try it with a larger list:

	```python
	print(my_quicksort(create_random_list(100)))
	```

## Optimising quicksort

- Quicksort is pretty fast, but can be made faster when a list is already partially sorted. This can be done by careful choice of a pivot value. The best pivot to choose is the *median* value of the first, last and middle items in the list, resulting in the middle value of the three. Can you alter your code so that you use this optimisation?
