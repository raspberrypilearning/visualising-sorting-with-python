# Visualising Sorting With Python 4 - Selection Sort

The selection sort algorithm is probably one of the easiest algorithms to understand, as it's very similar in nature to the way a human would sort a list.

The selection sort algorithm steps through an unordered list, keeping track of the smallest value it encounters, and once it has iterated through the entire list, it moves this value to the start of the list. This is repeated until the list is sorted.

With a small list such as:

    `[4,3,6,2]`

the first value `4` is assumed to be the smallest value. The next item in the list `3` is looked at and as this is smaller than `4`, it becomes the smallest value. Next, `6` is looked at. It's larger than `3`, so `3` remains the smallest value. Finally, for this iteration the value `2` is looked at. As it's smaller than `3` it now becomes the smallest value. As the algorithm has reached the end of the list, `2` is swapped with `4`:

    `[2,3,6,4]`

Next, the algorithm makes `3` the smallest value. This is compared to `6` and then `4` but as it's always smaller, it's left alone:

    `[2,3,6,4]'

Lastly, `6` is made the smallest value. It's compared with `4`, which is smaller, so `4` becomes the smallest value. As the algorithm has reached the end of the list, `6` and `4` are swapped:

    `[2,3,4,6]`

The list is now sorted.

## Starting off

1. Load up your *sorting.py* file from the previous lesson.
1. Comment out any function calls you might have from previous lessons:

	```python
	#my_bubble_sort(create_random_list(20))
	#my_insertion_sort(create_random_list(20))
	```

## Sorting a single item

1. As you've done in previous lessons, start by creating a small list:

  ```python
  some_list = [4,3,6,2]
  ```

1. You can begin your selection sort algorithm by manually setting the starting position to 0:

	```python
	some_list = [4,3,6,2]

	i = 0
	```

1. Next, you need to make that initial starting value the `smallest_value`:

	```python
	some_list = [4,3,6,2]

	i = 0
	smallest_value = i
	```

1. Now you can use a `for` loop to iterate over the entire list (excluding the 0th element), and find which one is the smallest:

	```python
	some_list = [4,3,6,2]

	i = 0
	smallest_value = i

	for j in range(i+1,len(some_list)):
		if some_list[j] < some_list[smallest_value]:
			smallest_value = j
	```

1. Test your script to make sure it's correctly reporting the *smallest value* by running it and then typing `smallest_value` into the interpreter. Given the list above, you should get back the value `3` indicating the *3rd* element of the list. Try `some_list[smallest_value]` to see the actual value.

1. Now that you know the smallest value, you can now use the same swapping mechanism as you have used in previous sorts:

	```python
	some_list = [4,3,6,2]

	i = 0
	smallest_value = i

	for j in range(i+1,len(some_list)):
		if some_list[j] < some_list[smallest_value]:
			smallest_value = j

	some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
	```

1. By putting a couple of `display()` calls and a `sleep()` in the script, you can see the swap taking place:

	```python
	some_list = [4,3,6,2]

	display(some_list)

	i = 0
	smallest_value = i

	for j in range(i+1,len(some_list)):
		if some_list[j] < some_list[smallest_value]:
			smallest_value = j

	some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
	sleep(1)	
	display(some_list)	
	```

## Running through the entire list

You now need to iterate over the entire list, starting from *position 0* up to the length of the list. Place all your code in a `for` loop and remove the setting of `i` to 0:

```python
some_list = [4,3,6,2]

for i in range(len(some_list)):
	smallest_value = i

	for j in range(i+1,len(some_list)):
		if some_list[j] < some_list[smallest_value]:
			smallest_value = j

	some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
	sleep(1)	
	display(some_list)
```

## Wrapping it all up

1. As before, place your code inside a function and call it with a random list. It's probably best to remove the `sleep()` as well:

	```python
	def my_selection_sort(some_list):
		for i in range(len(some_list)):
			smallest_value = i

			for j in range(i+1,len(some_list)):
				if some_list[j] < some_list[smallest_value]:
					smallest_value = j

			some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
			display(some_list)	

		return some_list

	my_selection_sort(create_random_list(20))

	```

1. Because the selection sort is pretty quick, you might want to adjust the size of the list up to 100:

	```python
	my_selection_sort(create_random_list(100))
	```

1. It's also quite nice to visualise this one as a scatter plot:

	```python
	def display(some_list):
		plt.clf()
		plt.scatter(range(len(some_list)),some_list)
		plt.draw()
	```

