# Visualising Sorting With Python 3 - Insertion Sort

The insertion sort algorithm sorts an unordered list by stepping through the list, removing the unordered item, and then shuffling the other items forward in the list until the correct position is found for the removed item.

With a small list such as:

    `[4,3,6,2]`

the first value `4` is ignored. The next value `3` is looked at and compared to the first value `4`. As `4` is larger than `3`, they are swapped:

    `[3,4,6,2]`

Next, `6` is looked at. It's larger than 4 so it's left in place. Finally, `2` is looked at. As `6` is larger, the two numbers are swapped:

    `[3,4,2,6]`

`2` is also smaller than `4`, so again, they are swapped:
    `[3,2,4,6]`

Finally, `3` is larger than `2` so again, they are swapped:

	`[2,3,4,6]`

## Starting off

1. Load up your *sorting.py* file from the previous lesson.
1. You can comment out the last line of the file, so that the `my_bubble_sort()` function isn't called:

	```python
	#my_bubble_sort(create_random_list(20))
	```

## Sorting one item

1. You can start off coding the insertion sort algorithm by sorting a single item in a list.
1. Start by creating the list you want to sort:

	```python
	some_list = [4,1,3,2]
	```

1. Now you can pick an item to sort:

	```python
	i = 3
	```

1. Here position 2 has been picked, which is the value `2` in the list. The value `2` needs to be moved down the list until the item to its left is smaller than it. This can be achieved with a `while` loop:

	```python
	some_list = [4,1,3,2]

	i = 3

	while some_list[i-1] > some_list[i]:
		some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
	```

1. Next, `i` needs to be reduced by 1 each time:
	
	```python

	some_list = [4,1,3,2]

	i = 3

	while some_list[i-1] > some_list[i]:
		some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
		i -= 1
	```

1. Run the code and then type `some_list` into the interpreter to check that the item has been moved.

## Out of range!

1. The algorithm you have coded so far appears to move an item to the correct position in the list. To be sure, you can try with a different list. Edit the file so the list is now:

	```python
	some_list = [4,2,3,1]
	```

1. Run the code and see what happens. You should get the error:

	```python
	IndexError: list index out of range
	```

1. Why did this happen? Type `i` into the interpreter to see its value.

1. Let's use the `display()` function to actually see what's happening. Edit your code so that the list is displayed each time there is a move:

	```python
	some_list = [4,2,3,1]

	i = 3

	while some_list[i-1] > some_list[i]:
		some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
		display(some_list)
	```

1. If it runs too quickly you can place a `sleep(1)` in your file. You'll need to import the `time` module at the top of your file as well:

	```python
	from time import sleep

	# All your code

	some_list = [4,2,3,1]

	i = 3

	while some_list[i-1] > some_list[i]:
		some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
		display(some_list)
		i -= 1
		sleep(1)
	```

1. Can you see that the value `1` gets moved to the start of the list, then all the way back round to the end, and back to the start again? It looks as if it's being sorted twice! This occurs because of the way lists can be indexed in Python. Once an item has been moved to *position 0* (when `i` is `0`), `i` is decreased by `1` and so becomes `-1`. 

1. In Python the *-1st* item of a list is the last item. Similarly, as `i` continues to reduce it starts referencing the *-2nd*, *-3rd*, and *-4th* items. In this list the *-4th* is also the *0th*. In Python, you can't cycle around again, so when the program attempts to reference the *-5th* item, an error is thrown. To avoid this error, you can just make sure the `while` loop only runs while `i > 0`:

	```python
	some_list = [4,2,3,1]

	i = 3

	while i > 0 and some_list[i-1] > some_list[i]:
		some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
		display(some_list)
		i -= 1
		sleep(1)
	```

## Finishing the insertion sort

1. Now that you have code that can shift any given item in a list from right to left until it meets an item smaller than it, you can easily finish off the insertion sort. All you need to do is use the algorithm you have written on every item of the list, from the first to the last. A `for` loop is the perfect way of doing this:

	```python
	some_list = [4,2,3,1]

	for i in range(1,len(some_list)):
			while i > 0 and some_list[i-1] > some_list[i]:
				some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
				i -= 1
				display(some_list)
	```

1. Run this to watch your insertion sort working.

1. Now you can wrap it all in a function and call it, just like you did with the bubble sort:

	```python
	def my_insertion_sort(some_list):
		for i in range(1,len(some_list)):
			while i > 0 and some_list[i-1] > some_list[i]:
				some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
				i-=1
				display(some_list)
		return some_list

	my_insertion_sort(create_random_list(100))
	```

1. You can also speed up the visualisation by shifting the `display()` call:

	```python
	def my_insertion_sort(some_list):
		for i in range(1,len(some_list)):
			while i > 0 and some_list[i-1] > some_list[i]:
				some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
				i-=1
			display(some_list)
		return some_list

	my_insertion_sort(create_random_list(100))
	```

