# Lesson 6 - Quicksort

The quicksort algorithm uses recursion and is a very efficient way of sorting a list. Given a list such as:

```python
[39, 30, 45, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 4, 5]
```

sorting this list can be achieved by using a *divide and conquer* technique, breaking the problem up into smaller problems. 

1. First you need to choose a single item from the list. It doesn't matter which one so it might as well be the first item in the list, in this case `39`. 

1. Next, you move from left to right along the list, looking for an item that is greater than or equal to the pivot. In this case, as the pivot is `39` and the first item is `39`, you've found it.

1. Then you move from the far right of the list, looking for an item that is smaller than the pivot; in this case it's `5`. Then the two items are swapped:

  ```python
  [5, 30, 45, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 4, 39]
  ```

1. The process now continues. From the left, `30` is smaller than the pivot, so it's ignored. `45` is greater than the pivot. From the right, `4` is smaller than the pivot, so the two items are swapped:

	```python
	[5, 30, 4, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 45, 39]
	```

1. Continuing on, you get:

	```python
	[5, 30, 4, 33, 20, 2, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 61, 71, 45, 39]
	[5, 30, 4, 33, 20, 2, 36, 5, 31, 27, 22, 10, 21, 25, 80, 86, 63, 64, 85, 61, 71, 45, 39]
	```

1. Now the list has been sorted, with every item greater or equal to `39` on the right, and everything smaller than `39` on the left.

1. Next comes the recursion. The left and right sides of the list are both run through the algorithm again.

1. This continues, running smaller and smaller sections of the list through the algorithm, until the size of the segment is one or zero. At this point the list will be sorted:

	```python
	[2, 4, 5, 5, 10, 20, 21, 22, 25, 27, 30, 31, 33, 36, 39, 45, 61, 63, 64, 71, 80, 85, 86]
	```

## Implementing a quicksort algorithm in Python

### Starting out - the base case

To begin with, you want to create an algorithm that chooses a pivot and moves items in the list around, so that all the items equal to or larger than the pivot are on the right, and all the items smaller than the pivot are on the left.

1. The quicksort algorithm has to work on whole lists and portions of a list, so it will need to know the start and end points of the list:

	```python
	def my_quicksort(some_list, start, stop):
	```
	
1. You can define the *base case* first. If the difference between the starting and ending position is less than 1 (i.e. you're trying to sort a section of a list that contains less than one item), the function should stop:

	```python
	def my_quicksort(some_list, start, stop):
		if stop - start < 1:
			return some_list
	```

### Moving items

1. You now need to choose a pivot, and also choose items from the list that you're going to compare. The `pivot` will be the first item in the segment of the list. The most `left` and `right` items will be the start and end points of the segment of the list:

  ```python
  def my_quicksort(some_list, start, stop):
	  if stop - start < 1:
		  return some_list
	  else:
		  pivot = some_list[start]
		  left = start
		  right = stop

  ```

1. The first thing to do is, starting with the item on the far left, check if it's smaller than the pivot and keep going until you find one larger than the pivot:

	```python
	def my_quicksort(some_list, start, stop):
		if stop - start < 1:
			return some_list
		else:
			pivot = some_list[start]
			left = start
			right = stop
			while left <= right:
				while some_list[left] < pivot:
					left += 1


	```

1. This will find the first item from left to right that's equal to or larger than the pivot.

1. You can now do the same from the right-hand side, looking for a value that's larger than the pivot:

  ```python
  def my_quicksort(some_list, start, stop):
	  if stop - start < 1:
		  return some_list
	  else:
		  pivot = some_list[start]
		  left = start
		  right = stop
		  while left <= right:
			  while some_list[left] < pivot:
				  left += 1
			  while some_list[right] > pivot:
				  right -= 1
  ```

1. So now the algorithm has found an item smaller than the pivot on the right-hand side, and larger than or equal to the pivot on the left. They can now be swapped, and the next items looked at:

	```python
	def my_quicksort(some_list, start, stop):
		if stop - start < 1:
			return some_list
		else:
			pivot = some_list[start]
			left = start
			right = stop
			while left <= right:
				while some_list[left] < pivot:
					left += 1
				while some_list[right] > pivot:
					right -= 1
				if left <= right:
					some_list[left], some_list[right] = some_list[right], some_list[left]
					left += 1
					right -= 1
	```

1. Let's check to see if the algorithm is working so far, by using some `print` statements:

  ```python
  def my_quicksort(some_list, start, stop):
	  if stop - start < 1:
		  return some_list
	  else:
		  pivot = some_list[start]
		  print('The pivot is:',pivot)
		  left = start
		  right = stop
		  while left <= right:
			  while some_list[left] < pivot:
				  left += 1
			  while some_list[right] > pivot:
				  right -= 1
			  if left <= right:
				  some_list[left], some_list[right] = some_list[right], some_list[left]
				  print("Swapping", some_list[left], "with", some_list[right])
				  left += 1
				  right -= 1
				  print('So the list becomes:')
				  print(some_list)

  my_list = [39, 30, 45, 33, 20, 61, 36, 5, 31, 64]
  my_quicksort(my_list, 0, len(my_list) - 1)
  ```

1. You can visualise the initial part by using your `display` function, perhaps with a barchart:

	```python
	def my_quicksort(some_list, start, stop):
		if stop - start < 1:
			return some_list
		else:
			pivot = some_list[start]
			print('The pivot is:',pivot)
			left = start
			right = stop
			while left <= right:
				while some_list[left] < pivot:
					left += 1
				while some_list[right] > pivot:
					right -= 1
				if left <= right:
					some_list[left], some_list[right] = some_list[right], some_list[left]
					print("Swapping", some_list[left], "with", some_list[right])
					left += 1
					right -= 1
					print('So the list becomes:')
					print(some_list)
					display(some_list)

	my_list = [39, 30, 45, 33, 20, 61, 36, 5, 31, 64]
	my_quicksort(my_list, 0, len(my_list) - 1)
	```

### Adding in the recursion

1. Now that the list has been sorted into two halves, you can run both halves back through the `my_quicksort()` function.

1. To sort the left-hand side of the list, you need to begin at `start` and end at whatever is now `right`. To sort the right-hand side of the list, you need to begin at whatever is now `left` and end at `stop`:

	```python
	def my_quicksort(some_list, start, stop):
		if stop - start < 1:
			return some_list
		else:
			pivot = some_list[start]
			left = start
			right = stop
			while left <= right:
				while some_list[left] < pivot:
					left += 1
				while some_list[right] > pivot:
					right -= 1
				if left <= right:
					some_list[left], some_list[right] = some_list[right], some_list[left]
					print("Swapping", some_list[left], "with", some_list[right])
					left += 1
					right -= 1

			my_quicksort(some_list, start, right)
			my_quicksort(some_list, left, stop)
	```

1. Finally, you can use the `display` and `create_random_list` functions from previous lessons to view the algorithm working on large lists:

	```python
	def my_quicksort(some_list, start, stop):
		if stop - start < 1:
			return some_list
		else:
			pivot = some_list[start]
			left = start
			right = stop
			while left <= right:
				while some_list[left] < pivot:
					left += 1
				while some_list[right] > pivot:
					right -= 1
				if left <= right:
					some_list[left], some_list[right] = some_list[right], some_list[left]
					print("Swapping", some_list[left], "with", some_list[right])
					left += 1
					right -= 1

			display(some_list)

			my_quicksort(some_list, start, right)
			my_quicksort(some_list, left, stop)

	my_list = create_random_list(200)
	my_quicksort(my_list, 0, len(my_list) - 1)
```

## Optimising quicksort

Quicksort is pretty fast, but can be made faster when a list is already partially sorted. This can be done by careful choice of a pivot value. The best pivot to choose is the median value of the first, last and middle items in the list, resulting in the middle value of the three. Can you alter your code so that you use this optimisation?
